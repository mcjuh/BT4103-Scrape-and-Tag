# -*- coding: utf-8 -*-
"""Takes em and en dashes out of GLM text without leaving a fragment (16OCT_TODO.md, section 4).

The base set (Claude) has no dashes; GLM uses them in about a third of its gigs, which tells the two authors apart.
A dash is never swapped for a hyphen when it breaks a sentence. By case, in this order:

  1. no space round it ("English–Chinese", "S$5,000–S$7,000", "1–2 weeks")  -> hyphen
  2. two spaced dashes in one sentence (an aside)                            -> brackets if it holds a comma, else commas
  3. the text after it starts a relative or joining clause ("whose", "and")  -> comma
  4. the text after it starts a new clause ("we ...", "Services include")    -> full stop, capital
  5. the text after it holds a comma (a list or an explanation)              -> colon
  6. anything else                                                           -> comma

The "Deliverable:" sentence has to stay one sentence with one colon, so there a break is always a comma.
`notes` (a list) collects what was changed, for the mend script's review sample.
"""

import re

DASHES = "—–"
_DASH = re.compile(rf"[{DASHES}]")
_COMPOUND = re.compile(rf"(?<=\S)[{DASHES}](?=\S)")  # no space on either side
_SPACED_NUM = re.compile(rf"(?<=\d)\s+[{DASHES}]\s+(?=[\d$S])")
_SPACED = re.compile(rf"\s*[{DASHES}]\s*")
_SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
_JOIN = {"who", "whose", "whom", "which", "that", "where", "when", "while", "with", "without", "so", "but", "and", "or",
         "because", "as", "not", "for", "to", "from", "in", "on", "at", "by", "of", "if", "then", "yet"}
_CLAUSE = {"i", "we", "it", "this", "these", "those", "they", "there", "he", "she", "you", "services", "our", "my"}


def has_dash(value) -> bool:
    """True when any string inside value (str, list or dict) holds an em or en dash."""
    if isinstance(value, str):
        return bool(_DASH.search(value))
    if isinstance(value, dict):
        return any(has_dash(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return any(has_dash(v) for v in value)
    return False


def _first_word(s: str) -> str:
    m = re.match(r"\W*([A-Za-z']+)", s)
    return m.group(1) if m else ""


def _break(before: str, after: str, deliverable: bool):
    """(replacement, rule) for one spaced dash with the text on either side of it, up to the sentence ends."""
    word = _first_word(after)
    low = word.lower()
    if deliverable:
        return ", ", "comma (deliverable)"
    if low in _JOIN:
        return ", ", "comma (joins a clause)"
    if low in _CLAUSE:
        return ". ", "full stop"
    if "," in after and ":" not in before:
        return ": ", "colon (list or explanation)"
    return ", ", "comma"


def _fix_sentence(s: str, notes: list) -> str:
    deliverable = s.lstrip().startswith("Deliverable:")
    s = _COMPOUND.sub("-", s)
    s = _SPACED_NUM.sub("-", s)
    spaced = list(_SPACED.finditer(s))
    if len(spaced) == 2 and not deliverable:  # an aside: brackets when it is a list, else commas
        a, b = spaced
        aside = s[a.end():b.start()]
        if "," in aside:
            rest = s[b.end():].lstrip()
            low = _first_word(rest).lower()
            glue = " "
            if low in _CLAUSE and rest[:1] not in ",.;:":  # the closing dash was a sentence break
                glue, rest = ". ", rest[:1].upper() + rest[1:]
            out = s[:a.start()] + " (" + aside + ")" + (glue if not rest[:1] in ",.;:" else "") + rest
        else:
            out = s[:a.start()] + ", " + aside + ", " + s[b.end():]
        notes.append(("aside", s, out))
        return out
    out, pos = "", 0
    for m in spaced:
        end = s.find(".", m.end())
        after = s[m.end(): end if end >= 0 else len(s)]
        text, rule = _break(s[pos:m.start()], after, deliverable)
        tail = s[m.end():]
        if text == ". ":  # capitalise the new sentence
            tail = tail[:1].upper() + tail[1:]
            s = s[:m.end()] + tail
        out += s[pos:m.start()] + text
        notes.append((rule, s[max(0, m.start() - 30): m.end() + 30], None))
        pos = m.end()
    return out + s[pos:]


def _tidy(s: str) -> str:
    s = re.sub(r"\s+([,.;:])", r"\1", s)
    s = re.sub(r"([,;:])\s*([,;:])", r"\2", s)
    s = re.sub(r",\s*\.", ".", s)
    s = re.sub(r"\.\s*\.", ".", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.strip()


def strip_dashes(text: str, notes: list = None) -> str:
    """text with every em and en dash replaced by the rules above. Unchanged when it has none."""
    if not isinstance(text, str) or not _DASH.search(text):
        return text
    notes = notes if notes is not None else []
    parts = _SENTENCE.split(text)
    seps = _SENTENCE.findall(text)
    out = ""
    for i, part in enumerate(parts):
        out += _fix_sentence(part, notes) + (seps[i] if i < len(seps) else "")
    return _tidy(out)


SKIP = ("source_file", "extracted_by_model", "hirer_ref", "replaces")


def apply_to_record(rec, notes: list = None, _key: str = ""):
    """A copy of a gig or provider record with every string stripped of dashes (identifiers are left alone).
    notes gets (field, before, after) for each string that changed."""
    if isinstance(rec, dict):
        return {k: (v if k in SKIP else apply_to_record(v, notes, k)) for k, v in rec.items()}
    if isinstance(rec, list):
        return [apply_to_record(v, notes, _key) for v in rec]
    if isinstance(rec, str):
        out = strip_dashes(rec)
        if out != rec and notes is not None:
            notes.append((_key, rec, out))
        return out
    return rec
