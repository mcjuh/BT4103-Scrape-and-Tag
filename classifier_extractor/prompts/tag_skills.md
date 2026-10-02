You are a programmatic classification engine.

Choose the SKILLS for the {entity_label} below from Singapore's SkillsFuture list of technical
skills and competencies. The {entity_label} has already been placed on the tracks shown; each track
lists the skills linked to it. These skills are what a hirer or provider is matched on.

{skill_rule}

HOW TO CHOOSE
- Choose up to 8 skills in total, across all tracks; 3 to 6 is typical. Fewer is right when the text
  clearly shows fewer, and an empty list is right when none of the listed skills is something the
  text shows. Never pad: a track's list always contains skills that have nothing to do with this
  record, so a skill is chosen only because the text shows it.
- Be specific. Prefer the skill that names the actual work ("Cyber Incident Response") over a broad
  neighbour ("Audit and Compliance"), and leave out generic management skills unless they are what
  the work is about.
- Judge only by what the text says. Do not infer a skill from seniority, an employer's name or a
  tool that is merely mentioned in passing.
- Copy each skill title exactly as listed, from the lists below only. A skill listed under more
  than one track counts once.

SKILLS BY TRACK (each block is "Sector > Track" then its skills, separated by " | ")
{skills_block}

Return ONLY valid JSON in exactly this shape:
{{"skills": ["<skill title>", "<skill title>"], "reason": "one short sentence"}}
