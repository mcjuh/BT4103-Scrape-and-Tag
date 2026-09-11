You are classifying a single scraped webpage's content into exactly one category.

Return ONLY valid JSON in this exact format:
{"label": "PROVIDER" | "HIRER" | "IGNORE" | "UNCERTAIN", "reason": "one short phrase, max 15 words"}

### PROVIDER
The page's primary subject is ONE specific, named person, and the content is substantially
about that person's own career, experience, skills, or work history; written as their
personal bio, profile, or portfolio. Required, not just present:
- A specific individual's full name is the primary subject of the page (not a company, a
  team, or a list of multiple names).
- The page is describing THAT person's own roles, background, expertise, or achievements --
  not what a company, team, or client project achieved.
- Reads as "about me" / an individual bio / a personal portfolio -- not "about us" / a case
  study / a deal summary.

KEY RULE: a page about what a COMPANY or TEAM did -- a deal, a case study, a client
engagement, a project outcome -- is NOT PROVIDER even if it names or quotes an individual,
unless that person's own career and background (not the deal or project) is the actual
subject of the page. Such a page is usually HIRER instead (see below) if it describes one
concrete engagement, or IGNORE if it's too generic to pin down as one specific engagement.
Example: a case study titled "Firm X advises on a $9B restructuring" is NOT PROVIDER -- the
subject is the deal and the firm's role in it, not any one person's career, even if a partner
is named or quoted in it. It's HIRER if it describes what was actually done (scope, approach,
outcome); IGNORE if it's just a headline/blurb with no real detail.

### HIRER
The page describes one specific, concrete task, project, or engagement -- not a person's own
career (see KEY RULE) -- concrete enough that a similar task could be posted as a gig. Two
ways a page qualifies:
1. An actual request for work: a job posting, task listing, or brief with a defined scope,
   deliverable, budget, and/or deadline for someone to fulfill.
2. A concrete case study or completed engagement: a specific, named project with a defined
   scope (what was done, for whom, what skills/approach were used) and a concrete outcome or
   result -- even with no stated budget or deadline. Retrospective ("we did X for client Y and
   achieved Z") is fine as long as it's concrete, not generic.
Signals: budget/rate, deadline/timeline, "looking for", skills required for a task, OR a named
client/project with a specific scope and a measurable/described outcome (e.g. "$14.4M saved",
"reduced processing time by 40%", "advised on a $9B restructuring").
A page is NOT HIRER merely for being on a company's services/marketing page in general -- it
must describe ONE specific, concrete engagement, not a generic service offering or industry
capability (that's IGNORE).

### IGNORE
Anything that is not one person's own bio page and not a specific engagement or work request.
This includes, but is not limited to:
- Company/team "About Us," leadership, or "meet the team" pages listing multiple people.
- Marketing, service-description, landing, or category/marketplace pages with no single
  concrete engagement described (generic "we help clients with X" copy, not "here's what we
  did for client Y").
- Press releases or case-study/deal blurbs too generic to count as one concrete engagement
  under HIRER above (see KEY RULE).
- Recruiting, "join us," careers, or generic hiring-marketing pages.
- Legal, contact, privacy, or other boilerplate pages.
- 404/error pages, empty pages, cookie banners, login walls.
If the page is generic, company-level, or not centered on either one named individual's own
career or one concrete engagement, it is IGNORE -- do not default to UNCERTAIN just because
the page is low-value.

### UNCERTAIN
Use only when the page genuinely contains a substantial PROVIDER profile (per the rule above)
that ALSO carries explicit HIRER signals on the same page (e.g. a personal portfolio that also
states a rate, budget, or "hire me"), or you truly cannot decide after applying the rules
above. Do not use UNCERTAIN as a catch-all for pages that are simply generic or low-value;
those are IGNORE.

Do not extract, summarize, or comment on anything beyond the label and reason.
