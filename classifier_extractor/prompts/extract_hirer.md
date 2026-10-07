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
A gig here is small: ONE specialist working ALONE, usually for 1-8 weeks and never more than 6
months, on ONE problem with ONE deliverable. Case studies almost always describe work a whole
team did across a whole building, organisation or programme. Never turn that into one gig. Cut it
down to one slice, narrowing on all three of these:
- ONE place or thing: a single site, space, system, process or asset (from "four theatres": one
  theatre; from "a group-wide ERP rollout": one finance team's month-end close).
- ONE task: a single discipline or workstream (from "speech clarity, immersive audio, sound
  insulation and modelling": just one of them).
- ONE deliverable: a single report, plan, model, document or working build.
Size check before you write: could one person do this alone, with no team, in about 1-8 weeks?
If the gig still covers several sites, spaces, workstreams, disciplines or deliverables, it is
too big; cut it again. A diagnosis, review, assessment or targeted fix is usually the right size;
designing, setting up or delivering a whole facility, function, department, platform or programme
is not (from "set up a finance function": one process in it, such as the month-end close).

WHO IS HIRING
The marketplace's hirers are mostly small and mid-sized Singapore organisations that bring in one
outside specialist because they have nobody in-house for the problem: SMEs, family businesses,
clinics, F&B operators, contractors, startups, charities and social enterprises, plus a few listed
SMEs and single teams inside larger organisations. The source is usually about a large enterprise.
Restate its need as it would arise at the SMALLEST kind of organisation in the same industry that
would plausibly face it:
- Keep the industry and the kind of work; shrink the organisation. From "a global insurer": "a
  general insurance agency with 40 staff". From "a national retailer's store network": "a
  six-outlet retail chain". From "a multinational manufacturer": "a precision components maker
  with 35 workers".
- If the need only exists at a large organisation (e.g. a core banking system, a national rail
  network, a hospital cluster), keep it large but write as the one team posting the gig ("We're
  the finance operations team at a ...").
- A local government body becomes a statutory board, town council or government agency team.
- Give the organisation an approximate size (staff, outlets, sites, vessels, clients or
  beneficiaries). Size and area are setting, not requirements, and size is the only figure you
  may add. Area: {area_instruction}
- A smaller hirer never means a bigger task. Keep the slice as small as KEEP IT SMALL says: if
  the source's work was a build or rollout, the gig is usually the assessment, design or one
  fix that comes before it.
- Drop source figures that only fit enterprise scale (e.g. "22 million customer records", "a
  S$400M programme", "2,000 stores"). Keep the figures that describe the slice itself: rates,
  targets, amounts and counts that still make sense for the organisation you describe.

SINGAPORE CONTEXT
The marketplace serves Singapore, so set the gig in Singapore whenever the scope allows, even when
the source is set somewhere else. It must read as a gig a Singapore business owner could really
post:
- The setting must exist here. Some kinds of organisation and structure have no Singapore version:
  US counties, states, school districts and municipalities, short-line or regional railways, dairy
  and grain farms. Restate the need for the nearest kind that does exist at that size (a town
  council, a statutory board team, a rail operator's maintenance team, a vertical farm), or return
  {{}} if the work only makes sense abroad. Likewise, public
  roads, rail, water and parks are commissioned by Singapore agencies, not private developers: a
  private firm's gig is about its own site.
- Foreign regulators, jurisdiction-specific rules and public bodies become the Singapore
  counterpart that covers the same requirement: FDA -> HSA; SEC, FCA -> MAS; EPA -> NEA; OSHA ->
  MOM workplace safety rules; IRS, HMRC -> IRAS; GDPR, CCPA, HIPAA -> PDPA; FAA, EASA -> CAAS;
  FCC, Ofcom -> IMDA; US GAAP -> SFRS(I) (or the SFRS for Small Entities); Chapter 11 -> judicial
  management under the IRDA. Federal, state, county and city bodies and grants become the
  Singapore ministry, statutory board or funder that does the same job (a federal health grant ->
  an MOH- or NCSS-funded programme), or are left out. If there is no clear counterpart, leave the
  foreign rule out (e.g. the ADA, Medicaid, a US state code) rather than invent a local one,
  unless the work is about that rule itself.
- When the work itself, or the hirer's business, is regulated or governed in Singapore, name the
  regulator, law, licence, standard or scheme involved, the way a local business owner would, even
  if the source names none. Examples: food hygiene -> SFA licence or NEA grading; workplace safety
  -> MOM, the WSH Act or bizSAFE; banks, insurers, payment and financing firms -> MAS; building
  works -> BCA and the Building Control Act; building contract disputes -> the Security of Payment
  Act, SIA or PSSCOC conditions; roads, rail, buses and taxis -> LTA; water and drainage -> PUB;
  parks and biodiversity -> NParks; land use and planning -> URA; industrial estates -> JTC;
  electricity and gas -> EMA; telecoms, media and digital services -> IMDA; cyber security -> CSA;
  customer or patient data -> PDPA; company filings and directors' duties -> ACRA and the
  Companies Act; restructuring and insolvency -> the IRDA; vessels and port operations -> MPA;
  airports and airlines -> CAAS; clinics and healthcare -> MOH licensing and the Healthcare
  Services Act; medicines and health products -> HSA; social services -> MSF or NCSS; charity
  reporting -> the Commissioner of Charities; staff contracts -> the Employment Act; tax -> IRAS;
  listed-company reporting -> SGX rules and SFRS(I); standards and certification -> Enterprise
  Singapore; patents and trademarks -> IPOS. Mention it once, as context for the work (e.g. "as an
  MAS-licensed financing company, ..."); never add a separate compliance task, and never claim an
  inspection, audit or funding condition happened unless the source says so.
- Never name a real company, Singapore or foreign. The hirer stays a described kind of
  organisation, never a named one.
- Keep international standards, frameworks and tools as they are (e.g. ISO 27001, IFRS, SAP,
  Salesforce); they already apply in Singapore.
- State every source-backed amount in S$ (never US$, EUR or another currency), converted
  approximately and rounded.
- Use Singapore English spelling (organisation, programme, licence).
A swap like this restates a source-backed requirement; it does not count as adding one. Do not
add grants, schemes or requirements that the work does not fall under.

A qualifying gig requires both:
1. A concrete problem, requirement, or project need in the source.
2. A matching technical or professional scope that was implemented.

If either is missing, return exactly: {{}}

Otherwise return ONLY valid JSON with exactly these keys, and no others:
{field_block}

in exactly this shape:
{skeleton}

gig_title
3-10 words, stated plainly, naming the TASK, not a job title or a person. Good: "Food Safety
Audit for Central Kitchen", "Review Franchise Agreement Before Signing", "Map Service Gaps for
Elderly Residents". Bad: "Senior Food Safety Consultant", "Experienced Lawyer Needed". No generic
filler such as "Help Needed" or "Project Opportunity".

short_description
Write it the way a real client posts a gig on a freelance marketplace, before the work begins:
plain, specific, and slightly informal. Cover, in this order:
1. The situation: what kind of organisation this is (see WHO IS HIRING), the problem or need it
   has, and why it needs the work now. Use the trigger the source gives (e.g. a failed
   inspection, an insurer or customer requirement, a new regulation); if it gives none, use the
   plain reason the work itself implies (an upcoming audit for audit-readiness work, an expiring
   licence for a renewal). Never invent incidents, failures, disputes or figures.
2. The work: what the specialist has to do -- only the source-backed scope, tools, standards and
   constraints. Describe tasks, not the ideal candidate's personality or career.
3. A sentence starting "Deliverable:" naming the concrete output handed over at the end (e.g.
   "Deliverable: written gap analysis and prioritised action list."). It must be source-backed.
4. A sentence starting "Engagement duration:" with a realistic estimate for one specialist doing
   the scoped slice, usually 1-8 weeks and never more than 6 months (e.g. "Engagement duration:
   3-4 weeks."). Don't reuse the source's timeline for the whole programme; it describes the
   team's work, not this slice.

Example of the target shape (a different business, for form only -- never copy its details):
"We run three physiotherapy clinics in Singapore and our appointment no-show rate has climbed to about 18%.
We need someone to look at our booking and reminder process, pull the last six months of
appointment data, and recommend changes we can make with our existing booking software.
Deliverable: short report with the no-show analysis and a ranked list of fixes. Engagement
duration: 3-4 weeks."

Voice and opening: {voice_instruction}

Be specific. Carry over every concrete figure the source gives for this slice of work: volumes,
error or failure rates, targets, and amounts (apart from enterprise-scale figures, which WHO IS
HIRING says to drop). Name the systems, tools and local rules involved. A gig with no specifics
reads as generic; never invent a figure other than the organisation's size.

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

additional_notes
Budget, timeline, seniority, or other constraints ONLY if the source explicitly states them.
Otherwise null.

source_company and source_company_team
source_company is the organisation that PUBLISHED the source page -- for a consulting firm's
case study or press release, that's the consulting firm, NOT its client (e.g. an Accenture case
study about work for a bank -> "Accenture"). The domain at the start of the source file name
below is usually the publisher. source_company_team is the publisher's own team or practice
named on the page as doing the work (e.g. "Accenture Song"), or null if none is named. These two
fields are metadata only: never name any real company inside gig_title or short_description.

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
  Duration is the one exception: always give the estimated engagement duration. The hirer's
  Singapore setting, size and area (see WHO IS HIRING) are setting, not requirements.
- Do not add historic project dates, completed work, prior failures, remedial work, new
  incidents, urgency, or business problems unless explicitly established as the original need.
  The plain reason the work itself implies (see short_description, point 1) is allowed.
- Anonymise gig_title and short_description: never name the publishing firm, the client, or any
  other company, government body, division, practice, or team. Use a generic description instead
  (e.g. "a Singapore-based [kind of organisation]", "the finance operations team"). Keep named
  tools, standards, and technologies only when they are genuine source-backed requirements. A
  regulator may be named only as the source of a rule the work must meet (e.g. "HSA medical
  device registration"), never as the hirer or client.
- Keep the scope to one slice one specialist could do alone in about 1-8 weeks (see KEEP IT
  SMALL). Slicing is not inventing: every task in the slice must still come from the source.
- Prefer concrete requirements over background, promotional language, or repeated explanations
  of why the work matters.

Return {{}} for non-qualifying material. Never add keys such as "status", "reason", "error",
"role", or "required_skills".

SOURCE FILE: {source_file}
