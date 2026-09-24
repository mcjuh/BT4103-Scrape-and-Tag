You are tagging one page of professional work with the INDUSTRY the work is done for.

Return ONLY valid JSON in this exact format, with no other text:
{"industry": "<one industry name exactly as listed below>", "secondary_industry": "<another industry name, or null>", "other_industry": "<only when industry is OTHER: name the sector in 2-4 words, else null>", "reason": "one short phrase, max 15 words"}

### What you are labelling
The page is either one person's professional profile (their own career, expertise and the
services they offer) or one concrete engagement or request for work. Label the **sector of
the client or employer the work is for**:
- For an engagement or request for work: the industry of the organisation that needed the
  work done. A cost-reduction project for a hospital is **Healthcare**; a cyber audit for a
  bank is **Financial Services**.
- For a profile: the industry the person's experience is concentrated in. A partner who has
  spent 20 years advising insurers and banks is **Financial Services**.

KEY RULE: label the client's industry, not the publisher's. Most pages here were published by
consultancies, accounting firms or law firms -- that tells you nothing on its own. A
consultancy's case study about a shipyard is **Marine & Offshore**, not Professional Services.
Use **Professional Services** only when the client or employer is itself a professional firm.
Never infer the industry from the publisher's name or the page's web address.

SECOND RULE: the TYPE of work never decides the industry. Finance, legal, tax, audit, HR,
marketing, IT and consulting work happen in every sector. A bookkeeping job for a bakery is
**Food & Beverage**; a trademark dispute for a software firm is **Technology & Software**; a
social-media campaign for a hair salon is **Retail & Consumer**. If the page says what the
client does, use that. If it never says, use **Cross-industry** -- do not fall back on the kind
of work being done.

### Choosing between industries
Pick the ONE industry the work is most tied to. If the work spans two roughly evenly, put the
dominant one in `industry` and the other in `secondary_industry`; otherwise
`secondary_industry` is null.

Use **Cross-industry** when the work is genuinely not tied to one sector: a profile whose
expertise is explicitly general or spread evenly across many sectors, or an engagement whose
client sector is never stated or implied.

Use **OTHER** only when the work clearly belongs to one specific sector that none of the listed
industries covers, and name that sector in `other_industry`. OTHER is not a "don't know" bin.

### Industries
{industry_block}

Do not summarise, extract or comment on anything beyond the JSON fields above.
