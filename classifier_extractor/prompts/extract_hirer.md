Create one realistic GIG from the source material below, as a HIRER record for a gig
marketplace.

A gig is a short, fixed piece of work with a clear deliverable, posted by a hirer for one
independent specialist to take on. It is NOT a job vacancy, a permanent role, or a long-running
programme. The record describes the WORK -- the problem, what has to be done, and what gets
handed over -- not the person who would do it.

The source will usually be a completed case study, portfolio entry, or press release, not an
open job post. Treat a completed engagement as evidence of what the original hirer could have
requested before the work began.

KEEP IT SMALL
The gig must be something one specialist could finish in LESS THAN 1 YEAR -- usually a few weeks
to a few months. Case studies often describe large, multi-year transformation programmes run by a
big team. Do not turn the whole programme into one gig. Instead pick ONE self-contained piece of it
that has its own clear deliverable (e.g. from a group-wide ERP rollout: "review and redesign the
month-end close process for the finance team"), and describe only that piece.

A qualifying gig requires both:
1. A concrete problem, requirement, or project need in the source.
2. A matching technical or professional scope that was implemented.

If either is missing, return exactly: {{}}

Otherwise return ONLY valid JSON with exactly these keys, and no others:
{field_block}

in exactly this shape:
{skeleton}

hire_title
3-10 words, stated plainly, naming the TASK, not a job title or a person. Good: "Food Safety
Audit for Central Kitchen", "Review Franchise Agreement Before Signing", "Map Service Gaps for
Elderly Residents". Bad: "Senior Food Safety Consultant", "Experienced Lawyer Needed". No generic
filler such as "Help Needed" or "Project Opportunity".

hire_description
Write it the way a real client posts a gig on a freelance marketplace, before the work begins:
plain, specific, and slightly informal. Cover, in this order:
1. The situation: what kind of organisation this is and the problem or need it has.
2. The work: what the specialist has to do -- only the source-backed scope, tools, standards and
   constraints. Describe tasks, not the ideal candidate's personality or career.
3. A sentence starting "Deliverable:" naming the concrete output handed over at the end (e.g.
   "Deliverable: written gap analysis and prioritised action list."). It must be source-backed.
4. A sentence starting "Engagement duration:" with a realistic estimate for the scoped work,
   always under 12 months (e.g. "Engagement duration: 3-4 weeks."). Use the source's own
   timeline if it states one for this piece of work and it is under 12 months; otherwise give
   your best estimate for one specialist doing the scoped piece.

Example of the target shape (a different business, for form only -- never copy its details):
"We run three physiotherapy clinics and our appointment no-show rate has climbed to about 18%.
We need someone to look at our booking and reminder process, pull the last six months of
appointment data, and recommend changes we can make with our existing booking software.
Deliverable: short report with the no-show analysis and a ranked list of fixes. Engagement
duration: 3-4 weeks."

Voice and opening: {voice_instruction}

Keep it compact:
- One or two short paragraphs. Use 2-4 bullets only when there are several distinct tasks.
- Do not add headings.
- Mention each requirement once.
Length: {detail_instruction} Never more than 120 words -- the client's own gigs are 60-92 words.

Sound like a person writing a post, not a brochure:
- Vary sentence length and structure, and don't start neighbouring sentences the same way.
- Use plain verbs and everyday words. Avoid stock phrases such as "comprehensive", "robust",
  "cutting-edge", "end-to-end", "seamless", "leverage", "drive transformation", "seasoned",
  "we are seeking", and "help us".
- No sales pitch, no praise of the organisation, and no closing call to action.

hire_description_additional_notes
Budget, timeline, seniority, or other constraints ONLY if the source explicitly states them.
Otherwise null.

source_company and source_company_team
source_company is the organisation that PUBLISHED the source page -- for a consulting firm's
case study or press release, that's the consulting firm, NOT its client (e.g. an Accenture case
study about work for a bank -> "Accenture"). The domain at the start of the source file name
below is usually the publisher. source_company_team is the publisher's own team or practice
named on the page as doing the work (e.g. "Accenture Song"), or null if none is named. These two
fields are metadata only: never name any real company inside hire_title or hire_description.

GROUNDING RULES
This is a realistic simulation, not a literal quotation. You may invent only the hirer's voice,
concise connecting language, generic request framing needed to make the source read naturally
as a gig, and the estimated engagement duration described above.

All matchable content must be source-backed: role, tasks, technologies, standards,
industry-specific requirements, deliverables, qualifications, project constraints, and expected
outcomes. When in doubt, omit a detail rather than infer it.

- Select one coherent specialist scope. If the source describes several unrelated services,
  choose the single clearest one; do not combine them into a catch-all role.
- Do not add employment type, staffing level, location or onsite requirements, budget, proposal
  instructions, qualifications, or certifications unless the source explicitly states them.
  Duration is the one exception: always give the estimated engagement duration.
- Do not add historic project dates, completed work, prior failures, remedial work, new
  incidents, urgency, or business problems unless explicitly established as the original need.
- Anonymise hire_title and hire_description: never name the publishing firm, the client, or any
  other company, government body, division, practice, or team. Use a generic description instead
  (e.g. "a regional insurer", "a county government", "the finance operations team"). Keep named
  tools, standards, and technologies only when they are genuine source-backed requirements.
- Keep the scope realistic for one specialist working for less than a year (see KEEP IT SMALL).
- Prefer concrete requirements over background, promotional language, or repeated explanations
  of why the work matters.

Return {{}} for non-qualifying material. Never add keys such as "status", "reason", "error",
"role", or "required_skills".

SOURCE FILE: {source_file}
