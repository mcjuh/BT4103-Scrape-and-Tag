You are writing test data for a Singapore gig marketplace. Write ONE realistic GIG, as its hirer would post it.

A gig is a short, fixed piece of work with a clear deliverable, posted by a hirer for one independent specialist to take on alone. It is NOT a job vacancy or a long-running programme. It describes the WORK -- the task and what gets handed over -- not the person who would do it.

WHAT THIS GIG IS
- Field: <<sector>> > <<track>><<generic_line>>
- Seniority the work implies: <<level>> -- <<level_hint>>. Never write the word "<<level>>" or any years of experience; let the stakes and the ambiguity of the work imply it.
- Mode of work: <<mode>> -- <<mode_hint>>.
- Opening: <<opening>>.<<industry_line>>
- Length of short_description: about <<words>> words (never under 55, never over 120).
- Engagement duration: <<weeks>> weeks.
- Hirer notes: <<notes_line>>

KEEP IT SMALL
One specialist working alone, usually 1-8 weeks, on ONE place or thing, ONE task and ONE deliverable. A diagnosis, review, assessment or targeted fix is usually the right size; building a whole function or programme is not.

WHO IS HIRING
Mostly small and mid-sized Singapore organisations that have nobody in-house for the problem: SMEs, family businesses, clinics, F&B operators, contractors, startups, charities and social enterprises, or a single team inside a larger organisation. Pick the kind of organisation that would plausibly post this gig. Give its approximate size (staff, outlets, sites) only when it tells a specialist how big the job is. Never name a real company or person; the hirer is a described kind of organisation.

SINGAPORE CONTEXT
Set it in Singapore. Where the work or the business is regulated, name the Singapore regulator, law, licence or standard once, as context for the work (MAS, MOM, IRAS, PDPA, SFA, BCA, IMDA, CSA ...). Keep international standards and tools as they are (ISO 27001, IFRS, SAP, Xero). Amounts in S$. Singapore English spelling (organisation, programme, licence).

PUBLIC POST
The gig is read by every specialist browsing the marketplace. Be specific about the WORK and general about the ORGANISATION. Keep: the kind of organisation, the task, the systems, tools and standards, and figures that size the work (volumes, counts, targets). Leave out: the story behind the need (who resigned, what broke, what was tried), insiders, counterparties, contract terms, money at stake, exact locations, internal deadlines. A hard start date or deadline goes in additional_notes, not the description.

short_description, in this order:
1. One short opening sentence, in the opening style above. No backstory.
2. The ask and the work: what kind of specialist is wanted and what they have to do. Describe tasks, not the ideal person.
3. A sentence starting "Deliverable:" naming the concrete output handed over. It is the SECOND-LAST sentence.
4. A sentence starting "Engagement duration:" with the duration above (e.g. "Engagement duration: 3-4 weeks."). It is the LAST sentence. Always use exactly this label.
One or two short paragraphs, no headings. Plain, specific, slightly informal, like a real client on a freelance marketplace. Vary sentence length. Do not use stock phrases such as "comprehensive", "robust", "cutting-edge", "end-to-end", "seamless", "leverage", "seasoned", "we are seeking", "help us". No sales pitch, no praise, no closing call to action.

gig_title: 3-10 words naming the TASK, not a job title or person (e.g. "Food Safety Audit for Central Kitchen").

additional_notes: <<notes_rule>>

Return ONLY valid JSON, no other text:
{"gig_title": "...", "short_description": "...", "additional_notes": <string or null>}
