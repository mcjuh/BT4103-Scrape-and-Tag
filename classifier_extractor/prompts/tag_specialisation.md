You are a programmatic classification engine.

Place the {entity_label} below on Singapore's SkillsFuture skills framework: choose its
CATEGORY (a sector) and its SPECIALISATION (a track inside that sector) from the list at the end.
These become the search tags a hirer or provider is found by on a gig marketplace.

{subject_rule}

HOW TO CHOOSE
- Classify the WORK, not the client's industry. A cyber security review for a hospital is
  Infocomm Technology > Cyber Security, not Healthcare; a month-end close for a biotech company is
  Accountancy > Financial Accounting, not a manufacturing sector.
- Choose 1 to 3 specialisations, the ones the {entity_label} is mostly about, best fit first. One
  is right when the work is single-focus. Add a second or third only when the text describes
  separate work that belongs in it on its own; a related-sounding topic does not count (due
  diligence and anti-money-laundering compliance is risk and compliance work, not cyber security
  because "risk" appears in both).
- Use at most 2 different sectors across all your choices.
- Copy the sector and track names exactly as listed. A track must be one listed under the sector
  you pick: names such as "Operations", "Management" and "General Management" appear under several
  sectors, so the sector decides which one you mean.
- Match on what the work actually is, not on a shared word. "Operations" in a title does not make
  it Financial Services > Operations.
- Read a track's name for the KIND of work it covers, not narrowly. A small sector still fits: Legal
  Services > Advisory and Advocacy is where legal advice, contract and lease review, legal drafting
  and dispute work all belong, and Accountancy covers tax, audit, valuation and restructuring.
- The framework has no sector for general strategy or management consulting, public-sector policy,
  or pure research and evaluation. Return an empty list only when the record is ONLY that kind of
  work. When it also names concrete work in a domain the framework does cover (digital engineering,
  finance, healthcare operations, retail, environmental health and safety, ...), tag that work: a
  strategy adviser for retail operations is Retail, a healthcare finance restructuring is
  Accountancy or Healthcare, an environmental impact assessment is Environmental Services >
  Environment, Health and Safety.
- Two sectors are often picked wrongly. "Strategy and Governance" under Infocomm Technology is IT
  strategy and governance, not business strategy in general. "Trade Associations and Chambers" is
  for the staff of trade bodies and chambers of commerce, never for advisers to ordinary companies.
- Never force a track on work it doesn't describe. A wrong tag is worse than no tag.

SECTORS AND TRACKS (each line is "Sector: Track | Track | ...")
{taxonomy_block}

Return ONLY valid JSON in exactly this shape:
{{"specialisations": [{{"sector": "<sector>", "track": "<track>"}}], "reason": "one short sentence"}}
