You are a programmatic data transformation engine.

The PROVIDER record below must read as the profile of a Singapore-based specialist on a gig
marketplace that serves Singapore. A check found phrases in it that still place the person's work
outside Singapore. Fix those, and change nothing else.

FLAGGED PHRASES (each appears in the record):
{residue}

This is a narrow edit, not a rewrite. Keep every sentence that has no flagged phrase word for word,
including its voice (first person or not), tense, length and wording, and keep each field's
length within about 10% of what it is now. Change only the words a rule below names.

HOW TO FIX A FLAGGED PHRASE
- An employer, client or place. Make it a Singapore-based version of the SAME kind of
  organisation, keeping its industry, type and scale ("a US regional health system" -> "a Singapore
  regional healthcare group"; "a Nordic subsidiary" -> "the Singapore subsidiary"). Work in a
  foreign region or several foreign countries becomes regional: "across Southeast Asia", "for APAC
  clients" ("in Europe and the Middle East" -> "across Asia Pacific"). A global organisation stays
  global ("a global strategy consultancy").
- A foreign regulator, law or court becomes the Singapore counterpart that covers the same thing:
  FDA -> HSA; SEC, FINRA, FCA -> MAS; EPA -> NEA; OSHA -> MOM and the WSH Act; IRS, HMRC -> IRAS;
  GDPR, CCPA, HIPAA -> PDPA; US GAAP -> SFRS(I); Sarbanes-Oxley -> SGX listing rules and
  internal-control requirements; Chapter 11, examinership -> judicial management under the IRDA;
  "state and federal courts" -> "the courts". If there is no clear counterpart (Medicaid, federal
  tax guidance, state licensing boards), delete the phrase when the sentence stands without it.
- An amount of money is stated in S$, converted approximately and rounded (US$1 = S$1.35, EUR1 =
  S$1.45, GBP1 = S$1.70). A bare "$" amount is US dollars. Keep every other number as it is.
- Use Singapore English spelling (organisation, specialising, programme).

KEEP A FLAGGED PHRASE ONLY WHEN IT IS ONE OF THESE
- A credential, membership, degree, university, licence or award (CPA, AICPA member, INSOL Europe,
  an MBA from a US business school). These are personal facts and are never localised, and never
  swapped for a Singapore one.
- The person's specialism, when their expertise IS a foreign market or jurisdiction (e.g. Latin
  American due diligence, US tax, German contract law). Keep it, and word the service for Singapore
  businesses that deal with that market ("for Singapore companies expanding into Latin America").
- A government body or regulator the person worked for: keep it generic ("a national financial
  regulator"); never name it.

ALSO
- The record must stay anonymous. If any real company, client, product-owning firm or programme
  name appears (not a tool, standard or certification), replace it with a generic description
  of that kind of organisation, as you would a flagged place.
- Do not add anything: no new Singapore regulator, licence, client, project, certification or
  achievement, and no new facts. A null field stays null. Never write a name or "[CANDIDATE_NAME]".
- Never leave a field empty that has text now.

Return ONLY valid JSON with exactly these keys, and no others:
{field_block}

in exactly this shape:
{skeleton}

PREVIOUS RECORD:
```json
{previous_record}
```
