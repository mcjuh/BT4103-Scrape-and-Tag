You are writing test data for a Singapore gig marketplace. Below is a GIG a Singapore client posted. Invent ONE fictional freelance specialist and write their marketplace PROFILE as JSON. How well this person fits the gig is set by the ROUTE below; write the fit exactly as the route says, no better and no worse.

GIG
<<gig>>

THE PERSON (fixed; do not change)
- Seniority: <<seniority>>. Years in the field: exactly <<years>>. <<seniority_rule>>
- Mode of work: <<mode>>. <<mode_rule>>

THE ROUTE (how the person relates to the gig)
Route <<route>>: <<route_meaning>>.
Make this fit true through the person's career and what they now offer. Do not mention the gig, its client or its title, never describe doing this exact piece of work, and do not reuse the gig's sentences or any run of six or more of its words in a row. A real profile fits a gig it was never written for.
- If the route says "a different industry", "a different kind of problem" or "a neighbouring sub-focus", invent that other industry, problem or sub-focus, and keep it concrete.
- Invent one body of work with one coherent career. Do not blend in the gig's own domain beyond what the route allows.

THE PROFILE (a JSON object with exactly these keys)
- "title": a plain job title, 2-8 words ("Forensic Accountant"). <<title_rule>>
- "credentials": 0-2 registrations, certifications or memberships named in full where normal for the field and level (e.g. "Chartered Accountant (ISCA)"). Many people in many fields have none: use an empty list unless a credential is normal for this field and level.
- "years_experience": <<years>> (an integer).
- "about_headline": one line, at most 20 words. Not a sales hook.
- "about_bio": 70-85 words, first person. State the years once as a number. A plain current title, two or three past roles described generically ("a Singapore-based [kind of organisation]'s [team]"), degrees, and the Singapore setting. Now independent.
- "services": EXACTLY ONE item, {"service_title": 3-10 words, "service_detail": 40-50 words: who it is for (small and mid-sized Singapore businesses where the expertise suits them), "Services include ..." with 3-5 concrete services, optionally the Singapore laws or standards, optionally one scope-limit sentence}. It is ONE engagement a single client could hire them for alone.
- "achievements": 3-5 outcomes the person personally produced, each ONE short sentence of 8-14 words, each with a figure (a size, a percentage, a timeframe or a count), each for a different kind of client.
- "technical_proficiency": 1-3 groups {"category": 1-3 words, "skills": 2-6 named tools, methods or standards}.
- "how_i_work": 25-40 words, first person: how they run an engagement. An approach only; no credential, client or figure.
- "availability": null
- "rate": null

RULES
- Mode of work shows in what the person offers (their services and how_i_work), not in the first word of every achievement. Vary how the achievements open: some name the work (Wrote, Built, Prepared, Ran, Advised, Reviewed, Led), some name a result (Cut, Reduced, Cleared, Raised). An advisory person has one or two achievements that open with a production verb; an execution person has one or two that open with an advising or leading verb; a mixed person has both. No profile may have all its achievements open with the same kind of verb. An execution person must not read as someone who only advises and oversees; an advisory person must not read as someone who only produces to someone else's brief.
- Never use em dashes or en dashes. Use a comma, a colon, brackets or start a new sentence. Write ranges with a hyphen ("1-2 weeks").
- Singapore regulators and rules where they apply, amounts in S$, Singapore English spelling.
- Never give a name. Never name a real company, client, firm, product line or person. Never state a fee, day rate, availability or start date.
- Do not make the profile longer, more detailed or more credentialed because the fit is better; the same length and detail whatever the route.
- Avoid stock phrases: "comprehensive", "robust", "cutting-edge", "end-to-end", "seamless", "leverage", "seasoned", "proven track record".

Return ONLY the JSON object, no other text.
