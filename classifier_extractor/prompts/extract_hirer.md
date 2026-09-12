Create one realistic freelance or specialist consulting gig from the source material below, as a
HIRER record for a gig marketplace.

The source will usually be a completed case study, portfolio entry, or press release, not an
open job post. Treat a completed engagement as evidence of what the original hirer could have
requested before the work began.

A qualifying gig requires both:
1. A concrete problem, requirement, or project need in the source.
2. A matching technical or professional scope that was implemented.

If either is missing, return exactly: {{}}

Otherwise return ONLY valid JSON with exactly these keys, and no others:
{field_block}

in exactly this shape:
{skeleton}

hire_title
At most 25 words, stated plainly. Name either the role wanted or the task itself, whichever reads
more naturally for this gig. No generic filler such as "Help Needed" or "Project Opportunity", and
don't default to the pattern "<Role> for <Project>".

hire_description
Write it the way a real client posts work on a freelance marketplace, before the work begins:
plain, specific, and slightly informal. State the need, then only the source-backed scope,
deliverables, tools, standards, and constraints.

Voice and opening: {voice_instruction}

Choose the most natural compact form:
- For simple work, one short paragraph.
- When there are several distinct requirements, a short opening followed by 2-5 concise bullet
  points.
- Do not add headings merely to create structure.
- Mention each requirement once; use bullets rather than restating a task in different words.
Length: {detail_instruction} Never more than 220 words.

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
concise connecting language, and generic request framing needed to make the source read
naturally as a gig.

All matchable content must be source-backed: role, tasks, technologies, standards,
industry-specific requirements, deliverables, qualifications, project constraints, and expected
outcomes. When in doubt, omit a detail rather than infer it.

- Select one coherent specialist scope. If the source describes several unrelated services,
  choose the single clearest one; do not combine them into a catch-all role.
- Do not add employment type, staffing level, location or onsite requirements, duration,
  budget, proposal instructions, qualifications, or certifications unless the source explicitly
  states them.
- Do not add historic project dates, completed work, prior failures, remedial work, new
  incidents, urgency, or business problems unless explicitly established as the original need.
- Anonymise hire_title and hire_description: never name the publishing firm, the client, or any
  other company, government body, division, practice, or team. Use a generic description instead
  (e.g. "a regional insurer", "a county government", "the finance operations team"). Keep named
  tools, standards, and technologies only when they are genuine source-backed requirements.
- Keep the scope realistic for one specialist or a small focused engagement.
- Prefer concrete requirements over background, promotional language, or repeated explanations
  of why the work matters.

Return {{}} for non-qualifying material. Never add keys such as "status", "reason", "error",
"role", or "required_skills".

SOURCE FILE: {source_file}
