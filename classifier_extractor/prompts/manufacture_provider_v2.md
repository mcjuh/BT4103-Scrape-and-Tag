You are writing source material for a Singapore gig marketplace's test data.

Below is a GIG a Singapore client has posted. Invent ONE fictional freelance specialist who could
take it on, and write the profile page a professional-services firm or an expert directory would
publish about them. An extraction system will read the page exactly as it reads a real one, so
write it the way a real profile page reads.

STEP 1: READ THE GIG
Work out two things from the gig's text, the way a hirer would. If the gig's notes state a level,
use it.
- gig_level: the seniority the work needs.
  mid = well-defined, lower-stakes work with a clear method (mapping a process, setting up a
  standard tool, routine documents).
  senior = owns the outcome, advises management, handles some ambiguity or regulation (a
  compliance gap review, a cost-reduction study).
  expert = high stakes, a scarce specialism or a formal opinion (an expert-witness report, M&A due
  diligence, a safety case for a regulator).
- gig_mode: the mode of work, read from the deliverable and the verbs.
  execution = hands-on production: completed documents, a working build, finished files.
  advisory = judgement for management: an assessment, a recommendation, a roadmap, an opinion.
  mixed = clearly both.

STEP 2: WHO TO INVENT
{variant_instruction}
Whatever the variant, the person matches the gig on both terms:
- Seniority. Same level as gig_level. Give them a number of years in the field inside the band
  for that level, and a title and past roles a person at that level would hold:
  mid = 6-9 years, a practitioner or consultant, no team leadership beyond a small project;
  senior = 12-18 years, has led a team or a function, advises management;
  expert = 22-30 years, a partner, director, former regulator or court-accepted expert.
  Never put "Senior", "Lead", "Principal", "Partner" or "Director" in the title of a mid-level
  person, and never describe an expert as junior to anyone.
- Mode of work. Write what they did with verbs of that mode:
  execution: drafted, built, prepared, implemented, configured, ran the analysis, hands-on;
  advisory: advised, reviewed, diagnosed, recommended, set the strategy, steered;
  mixed gig: show both kinds of work.
  An execution person must not read as someone who only advises and oversees others; an advisory
  person must not read as someone who only produces to someone else's brief.

THE PAGE
- 220-350 words of plain prose, third person, optionally ending with a short list of highlights.
  Call the person "they" or "the consultant". Never give them a name.
- State their years in the field once, as a number ("has 14 years of experience in ...").
- A plain job title for what they do now, two or three past roles described generically (shape:
  "a [kind of organisation]'s [team or practice]", "a Singapore-based [kind of organisation]"),
  and their degrees.
- Professional credentials, registrations or memberships, named in full where they are normal for
  this field and level (e.g. "Chartered Accountant (ISCA)", "registered Professional Engineer
  (Civil)"). None at all is fine where the field has none.
- What they offer now: one body of work, described as engagements one small or mid-sized client
  could hire them for alone. A second, clearly separate service only if it fits their career.
- Three to five specific past outcomes they personally produced, each with a figure (a size, a
  percentage, a timeframe or a count), each for a different kind of client.
- The tools, methods, standards and regulations they work with, named.
- Set the career in Singapore and the region: Singapore regulators and rules where they apply,
  amounts in S$, Singapore English spelling.
- They now work independently, taking on engagements one at a time.
- Do not state a fee, day rate, availability, start date or days a week: those are set elsewhere.
- Never name a real company, client, firm, product line or person.
- Describe a career, not this gig. Never mention this client, never describe doing this exact
  piece of work, and do not reuse the gig's title or its sentences. The fit should show through
  their experience, the way a real profile matches a gig it was never written for.

Return ONLY valid JSON in exactly this shape:
{{"gig_level": "mid" | "senior" | "expert", "gig_mode": "execution" | "advisory" | "mixed",
"profile_page": "<the page text>"}}

GIG:
{gig}
