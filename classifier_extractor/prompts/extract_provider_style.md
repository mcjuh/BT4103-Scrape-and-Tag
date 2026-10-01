You are a programmatic data transformation engine.

The input record below is a compact factual PROVIDER record extracted from source material about
ONE individual. Transform it into the final profile that individual would publish on a gig
marketplace, in their own voice.

Do not invent, pad, or change factual claims. Keep every null field null. Return ONLY valid JSON
with exactly the same keys as the input, and no others:
{skeleton}

EXPERIENCE/ROLE RULES
You are NOT formally employed currently (e.g. "I am a retired CFO with 20 years of
experience...", "I was a project manager for...", "Former executive at...", "I am a freelance
web developer...", "Retired software engineer..."). Your language must NOT indicate current
employment.

TRANSFORMATION & STYLE RULES
1. about_title style -- {title_style}: {title_style_instruction} At most 20 words.
2. about_description: first person, 70-100 words.
3. relevant_experience grammar -- {achievement_style}: {achievement_style_instruction} Keep it
   as 2-4 sentences of plain prose, 30-60 words (never more than 60, even if the input is
   longer), with no bullets or line breaks.
4. Prose imperfection: {imperfection_instruction}

If a prose imperfection is specified (anything other than "none"):
- Apply exactly ONE natural instance of it, in about_description or in one relevant_experience
  sentence.
- Do not introduce any other grammatical, spelling, or punctuation errors.

Never write the person's name or "[CANDIDATE_NAME]" in any field. Keep the record anonymised: never
reintroduce a company, client, division, or team name, and keep the input's generic descriptions.

Keep the input's Singapore setting: its Singapore-based organisation descriptions, Singapore
regulators and rules, and S$ amounts stay as they are. Use Singapore English spelling
(organisation, specialising, programme).

ACHIEVEMENT VERBS
Prefer past-tense, telic verbs that name a bounded outcome: Led, Delivered, Launched, Built,
Shipped, Won, Secured, Reduced, Grew, Cut, Saved, Redesigned, Migrated, Negotiated.

Causal-role verbs (Facilitated, Enabled, Supported, Contributed to, Collaborated with) are allowed
ONLY when the sentence names a specific object and a bounded scope or result:
  OK:  "Facilitated the migration of 40 services off mainframe, unblocking the Q3 release."
  BAD: "Facilitated digital transformation initiatives for clients."

Pure instrumentals (Leveraged, Utilized, Used, Employed, Applied) are never achievement verbs.
The real verb is downstream -- promote it:
  BAD: "Leveraged Salesforce to cut processing time."
  OK:  "Cut processing time by rebuilding the workflow in Salesforce."

The opening tenure sentence in relevant_experience (e.g. "18 years in construction claims ...")
is not an achievement: keep it first and unchanged apart from the grammar style above. Keep every
figure in the input. Leave services_offered_title and services_offered_description as they are,
apart from spelling, including any closing sentence on what the service does not cover.

Test each achievement with: "and then what happened?" If the sentence can't answer that with a
concrete outcome or result, it is not an achievement -- rewrite it or drop it (the tenure
sentence and past roles stay). If relevant_experience is null in the input, keep it null.
