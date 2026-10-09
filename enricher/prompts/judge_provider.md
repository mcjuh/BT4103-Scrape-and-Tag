You are sizing one independent specialist's profile on a Singapore marketplace where companies
hire specialists for short gigs. Read the profile below and judge a few things about it. The values
feed a matching engine, so pick the most likely answer even when the profile doesn't say; there
is no "unknown".

seniority -- the specialist's level:
- "mid": a solid practitioner (roughly 5-10 years), e.g. consultant, analyst, manager, engineer.
- "senior": an experienced lead (roughly 10-20 years), e.g. senior manager, associate director,
  director, practice or team lead.
- "expert": a recognised authority (roughly 20+ years), e.g. partner, managing director, C-level,
  former regulator, court-accepted expert, named industry leader.
Use stated years first; use titles when years aren't given.

price_tier -- how the market prices this specialist's kind of work, compared with other
specialists at the same seniority:
- "premium": scarce, regulated or high-stakes specialisms (legal, M&A, regulatory, actuarial,
  forensic, cyber incident response, specialist engineering sign-off).
- "standard": typical professional or technical advisory.
- "lean": common, generalist or lower-stakes work (content, admin, basic web or marketing,
  simple training).

price_score -- the same judgement on a finer 1-10 scale, used to rank specialists against each
other: 1-3 lean, 4-7 standard, 8-10 premium. Use the whole range. Most experienced consultants
are standard (4-7); save 9-10 for the scarcest, highest-stakes specialisms.

used_in_ml -- true if the specialist's service involves building, training, deploying or applying
machine learning or AI models (data science, ML engineering, computer vision, NLP, AI strategy
built on models); false otherwise.

sector and track -- where this specialist's SERVICE sits in Singapore's SkillsFuture skills
framework, chosen from the list below. Pick the sector whose work they do, then one track inside
that sector. Judge by what they offer, not by their clients' industry: a data-privacy adviser
to banks is Infocomm Technology, not Financial Services; an auditor of hospitals is Accountancy.
If no sector fits exactly, pick the closest one. Copy both names exactly as listed, and the
track must be one listed under the sector you picked.
{taxonomy}

Return ONLY valid JSON in exactly this shape:
{{"seniority": "mid" | "senior" | "expert", "price_tier": "lean" | "standard" | "premium", "price_score": 1-10, "used_in_ml": true | false, "sector": "<sector>", "track": "<track>", "reason": "one short sentence"}}

PROFILE:
{record}
