# -*- coding: utf-8 -*-
"""
Deterministic check for a record that still reads as set outside Singapore.

The extraction prompts ask the model to move every record's setting to Singapore, but
the pool's models follow that unevenly (on a smoke test qwen3.6:35b left "Latin America",
"a US health system" and a company name in a provider profile whose prompt told it not
to), and a model can't be trusted to grade its own compliance. So extract.py checks the
finished text with these patterns, and a provider with hits gets one targeted repair
pass (prompts/repair_localise_provider.md) given the exact phrases to fix.

The patterns are deliberately broad: a hit is a CANDIDATE, not a verdict, because some
foreign mentions are right to keep -- a membership ("INSOL Europe"), a credential
("CPA"), or a specialism that IS a foreign market ("German contract law") -- and the
repair prompt says so. A false positive therefore costs one extra call; a miss leaves a
foreign-set profile in a Singapore marketplace.

No LLM calls and no imports from the rest of the pipeline, so it can be tested alone.
"""

import re

# (label, pattern). Case-sensitive unless the pattern says otherwise: "US" the country
# and "us" the pronoun are different words.
_PATTERNS = [
    ("foreign currency", r"(?<![A-Za-z])(?:US|C|A|NZ|HK)\$|\bUSD\b|\bEUR\b|\bGBP\b|\bCAD\b|\bAUD\b|[€£]"
                         r"|(?<![A-Za-z$])\$\s?\d"),
    ("US", r"\bU\.?S\.?A?\b(?! ?\$)|\bUnited States\b|\bAmerican\b"),
    ("UK/Europe", r"\bUK\b|\bU\.K\.|\bUnited Kingdom\b|\bBritain\b|\bBritish\b|\bEurope(?:an)?\b|\bEMEA\b"
                  r"|\bNordic\b|\bScandinavia\w*\b|\bGermany\b|\bGerman\b|\bFrance\b|\bFrench\b|\bIreland\b"
                  r"|\bIrish\b|\bNetherlands\b|\bDutch\b|\bSwitzerland\b|\bSwiss\b|\bSpain\b|\bItaly\b"),
    ("Americas", r"\bNorth America\w*\b|\bLatin America\w*\b|\bSouth America\w*\b|\bCanada\b|\bCanadian\b"
                 r"|\bMexico\b|\bBrazil\w*\b|\bCaribbean\b|\bArgentin\w+\b|\bChile\w*\b|\bColombia\w*\b"),
    ("Middle East/Africa/Oceania", r"\bMiddle East\b|\bGulf\b|\bAfrica\w*\b|\bAustralia\w*\b|\bNew Zealand\b"),
    ("US place", r"\b(?:Texas|California|Florida|Illinois|Massachusetts|Pennsylvania|New York|New Jersey"
                 r"|Washington,? D\.?C\.?|Chicago|Boston|Houston|Dallas|Atlanta|Silicon Valley)\b"),
    ("foreign law/regulator", r"\bfederal\b|\bChapter 11\b|\bHMRC\b|\bIRS\b|\bSEC\b|\bFDA\b|\bFCA\b|\bFINRA\b"
                              r"|\bOSHA\b|\bEPA\b|\bGDPR\b|\bCCPA\b|\bHIPAA\b|\bMedicaid\b|\bMedicare\b"
                              r"|\bSarbanes\b|\bSOX\b|\bUS GAAP\b|\bstate (?:and|or) federal\b|\bexaminership\b"
                              r"|\bAICPA\b|\bGAAS\b|\bFCPA\b|\bBribery Act\b|\bDodd-Frank\b|\bPCAOB\b"),
    # Records are anonymised: an employer or client is described, never named. The prompts say
    # so and the models still leave one in ("Arthur Andersen LLP" in a smoke test), so a
    # legal-entity suffix or a well-known firm is flagged and the repair pass describes it.
    ("company name", r"\b[A-Z][\w&.'-]*(?:\s+[A-Z][\w&.'-]*){0,3}\s+(?:LLP|LLC|Inc|Ltd|PLC|GmbH|Corp|Corporation|Co)\b\.?"
                     r"|\b(?:Arthur Andersen|PricewaterhouseCoopers|PwC|Deloitte|KPMG|Ernst & Young|McKinsey|"
                     r"Boston Consulting Group|Accenture|Booz Allen|Grant Thornton|Alvarez & Marsal|FTI Consulting|"
                     r"Goldman Sachs|Morgan Stanley|JPMorgan|J\.P\. Morgan|Citigroup|Citibank|Bank of America|"
                     r"Wells Fargo|Merrill Lynch|Lehman Brothers|Credit Suisse|Barclays|HSBC|Standard Chartered|"
                     r"Lazard|Rothschild|Duff & Phelps|Kroll|Mazars|Thoughtworks|West Monroe)\b"),
]
_COMPILED = [(label, re.compile(p)) for label, p in _PATTERNS]

# Personal credentials and memberships are facts about the person, never localised, so they
# are cut out before the patterns run: "an MBA from the University of Chicago Booth School
# of Business", "American Society of Appraisers", "CPA Australia", "New York-qualified",
# "CPA-registered in New York and Texas". In a sample of the v2 providers these were a large
# share of the hits, and each one cost a pointless repair call and cluttered the log.
_ORG_NOUN = (r"(?:University|College|School|Institute|Institution|Society|Societies|Association|"
             r"Academy|Council|Federation|Foundation|Chamber|Board|Bar)")
_CREDENTIAL = re.compile(
    r"(?:\b[A-Z][\w&'.-]*\s+){0,4}" + _ORG_NOUN + r"(?:\s+(?:of|and|for|in|the|[A-Z][\w&'.-]*)){0,8}"
    r"|\bINSOL Europe\b|\bAICPA\b|\bCPA Australia\b"
    r"|\bChartered Accountants?\s+(?:of|in|from)\s+[A-Z][\w ,&]*?(?=[.;]|$)"
    r"|\b[A-Z]\w*(?:\s[A-Z]\w*)?-(?:qualified|registered|admitted|licensed|licenced|certified)\b"
    r"(?:\s+in\s+[A-Z]\w*(?:\s[A-Z]\w*)?(?:(?:,\s*(?:and\s+)?|\s+and\s+)[A-Z]\w*(?:\s[A-Z]\w*)?)*)?"
    r"|\b(?:qualified|registered|admitted|licensed|licenced|certified)\s+(?:to\s+practi[sc]e\s+)?in\s+"
    r"[A-Z]\w*(?:\s[A-Z]\w*)?(?:(?:,\s*(?:and\s+)?|\s+and\s+)[A-Z]\w*(?:\s[A-Z]\w*)?)*"
    r"|\b(?:US\s+|U\.S\.\s+)?(?:CPA|CFA|CMA|CIA|JD|Esq|Bar)\b[^.;]{0,50}")

# What makes a record read as Singapore-set rather than merely free of foreign phrases:
# Singapore itself, S$, or a Singapore regulator, law or scheme.
_ANCHOR = re.compile(
    r"Singapore|\bS\$|\bSG\b|\b(?:MAS|IRAS|ACRA|MOM|PDPA|PDPC|NEA|SFA|BCA|LTA|URA|HSA|MOH|CSA|IMDA|SGX|IRDA|"
    r"JTC|PUB|MPA|CAAS|EMA|MSF|NCSS|IPOS|SFRS|CPF|HDB|EDG|PSG)\b|NParks|Enterprise Singapore|"
    r"WSH Act|bizSAFE|Employment Act|Companies Act|Security of Payment Act|PSSCOC|Healthcare Services Act|"
    # the old area roll in extract_variations.json named these, and a gig set in "a clinic in Bedok"
    # is set in Singapore without the word
    r"\b(?:Punggol|Tuas|Jurong|Toa Payoh|Paya Lebar|Bedok|Pasir Panjang|Woodlands|Tampines|Changi|Sentosa|"
    r"Orchard|Marina Bay|Raffles Place|Ang Mo Kio|Yishun|Sengkang|Clementi|Kallang|Bishan|Serangoon|"
    r"Hougang|Bukit Merah|Bukit Timah|Queenstown|Geylang|Novena|Tanjong Pagar|Shenton Way|Kranji)\b")


def singapore_anchor(texts) -> bool:
    """Whether any of `texts` (a string or an iterable of them) names Singapore, S$ or a
    Singapore regulator, law or scheme."""
    if isinstance(texts, str):
        texts = [texts]
    return any(isinstance(t, str) and _ANCHOR.search(t) for t in texts)


def foreign_residue(texts) -> list:
    """The distinct foreign-setting phrases found in `texts` (a string or an iterable of
    them), in order of first appearance, ignoring credentials and memberships. Empty when
    the text reads as Singapore-set."""
    if isinstance(texts, str):
        texts = [texts]
    found = []
    for text in texts:
        if not isinstance(text, str):
            continue
        text = _CREDENTIAL.sub(" ", text)
        for _, rx in _COMPILED:
            for m in rx.finditer(text):
                phrase = m.group(0).strip()
                if phrase and phrase not in found:
                    found.append(phrase)
    return found


# ---------------------------------------------------------------------------
# Singapore English spelling
# ---------------------------------------------------------------------------
# The prompts ask for "organisation, specialising, programme" and the pool's models
# often write "organization, specialize, optimization" anyway (seen in a smoke test), so
# it's fixed here. An explicit list of stems, not "-ize -> -ise" in general, which
# would turn "size", "prize" and "seize" into nonsense. "program" is left alone: in
# Singapore English it is a computer program, and "programme" a scheme.

_IZE_STEMS = ("organi|speciali|optimi|prioriti|recogni|utili|standardi|finali|centrali|minimi|maximi|"
              "moderni|customi|harmoni|digiti|digitali|capitali|summari|visuali|categori|authori|"
              "synchroni|normali|formali|operationali|institutionali|rationali|stabili|mobili|"
              "personali|globali|locali|commerciali|industriali|moneti|materiali|reali|emphasi|"
              "critici|apologi|jeopardi|memori|sympathi|coloni|characteri|generali|neutrali|"
              "familiari|legali|sociali")
_IZE = re.compile(rf"\b((?:{_IZE_STEMS}))z(e|es|ed|ing|er|ers|ation|ations|ational)\b", re.IGNORECASE)
_ANALYZE = re.compile(r"\banalyz(e|es|ed|ing|er|ers)\b", re.IGNORECASE)
_WORDS = {"behavior": "behaviour", "behaviors": "behaviours", "behavioral": "behavioural",
          "labor": "labour", "center": "centre", "centers": "centres", "defense": "defence",
          "fulfill": "fulfil", "fulfillment": "fulfilment", "catalog": "catalogue", "favor": "favour",
          "honor": "honour", "color": "colour", "enrollment": "enrolment"}
_WORDS_RE = re.compile(r"\b(" + "|".join(_WORDS) + r")\b", re.IGNORECASE)


def _match_case(old: str, new: str) -> str:
    return new.upper() if old.isupper() and len(old) > 1 else (new[0].upper() + new[1:] if old[:1].isupper() else new)


def singapore_spelling(text):
    """`text` with the common US spellings in Singapore English ("organization" ->
    "organisation", "optimizing" -> "optimising", "center" -> "centre"). Not a string:
    returned unchanged."""
    if not isinstance(text, str):
        return text
    text = _IZE.sub(lambda m: m.group(0)[:len(m.group(1))] + ("S" if m.group(0)[len(m.group(1))].isupper() else "s")
                    + m.group(0)[len(m.group(1)) + 1:], text)
    text = _ANALYZE.sub(lambda m: m.group(0).replace("z", "s").replace("Z", "S"), text)
    return _WORDS_RE.sub(lambda m: _match_case(m.group(0), _WORDS[m.group(0).lower()]), text)
