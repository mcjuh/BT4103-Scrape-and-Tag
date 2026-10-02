You are sizing one gig on a Singapore marketplace where companies hire independent specialists.
Read the gig below and judge four things about it. The values feed a matching engine, so pick the
most likely answer even when the gig doesn't say; there is no "unknown".

seniority_needed -- the level of specialist the hirer would need to do this work well:
- "mid": a solid practitioner (roughly 5-10 years). Well-defined, lower-stakes work with a clear
  method, e.g. mapping a process, setting up a standard tool, preparing routine documents.
- "senior": an experienced lead (roughly 10-20 years). Owns the outcome, advises management,
  handles some ambiguity or regulation, e.g. a compliance gap review, a cost-reduction study.
- "expert": a recognised authority (roughly 20+ years, former partner, regulator, C-level or
  court-accepted expert). High stakes, scarce specialism or formal opinion, e.g. an expert witness
  report, M&A due diligence, a safety case for a regulator.

price_tier -- how the market prices this kind of specialism, compared with other work at the
same seniority:
- "premium": scarce, regulated or high-stakes (legal, M&A, regulatory, actuarial, cyber incident,
  specialist engineering sign-off).
- "standard": typical professional or technical advisory.
- "lean": common, generalist or lower-stakes work (content, admin, basic web or marketing,
  data entry, simple training).

urgency -- how soon the work has to start:
- "asap": the gig names an imminent trigger or deadline (an audit, inspection, renewal, filing,
  launch or regulation coming into force soon).
- "soon": some time pressure, but no hard near-term date.
- "flexible": no time pressure stated.

days_per_week -- how many days a week (1-5) one specialist would spend on it, given the scope and
the "Engagement duration" line: intensive build or on-site work is 4-5; a review or advisory
piece spread over several weeks is 1-3.

sector and track -- where this WORK sits in Singapore's SkillsFuture skills framework, chosen
from the list below. Pick the sector whose specialists would do the work, then one track inside
that sector. Judge by the work itself, not by the hirer's industry: a cybersecurity review for a
hospital is Infocomm Technology, not Healthcare; a tax filing for a shipping company is
Accountancy. If no sector fits exactly, pick the closest one. Copy both names exactly as listed,
and the track must be one listed under the sector you picked.
{taxonomy}

Return ONLY valid JSON in exactly this shape:
{{"seniority_needed": "mid" | "senior" | "expert", "price_tier": "lean" | "standard" | "premium", "urgency": "asap" | "soon" | "flexible", "days_per_week": 1-5, "sector": "<sector>", "track": "<track>", "reason": "one short sentence"}}

GIG:
{record}
