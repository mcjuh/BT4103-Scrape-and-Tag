You are a programmatic data transformation engine.

The input record below is a compact factual PROVIDER record extracted from source material about
ONE individual. Transform it into the final profile that individual would publish on a gig
marketplace, in their own voice.

Do not invent, pad, or change factual claims. Return ONLY valid JSON with exactly these keys, and
no others (the rest of the record is kept by code; do not return it):
{skeleton}

The input has no how_i_work: you write it, and it is never null when the input has a service. An
empty achievements list in the input stays an empty list.

EXPERIENCE/ROLE RULES
You are NOT formally employed currently (e.g. "I am a retired CFO with 20 years of
experience...", "I was a project manager for...", "Former executive at...", "I am a freelance
web developer...", "Retired software engineer..."). Your language must NOT indicate current
employment.

TRANSFORMATION & STYLE RULES
1. about_headline style -- {title_style}: {title_style_instruction} At most 20 words.
2. about_bio: first person, 70-100 words. Keep its facts, and add nothing from the other fields.
3. achievements grammar -- {achievement_style}: {achievement_style_instruction} Keep the same
   achievements, one sentence per item, in the same order (never more than 5 items, and drop
   one only if it fails the test below). Keep every figure in the input.
4. how_i_work (REQUIRED, a string of 25-60 words): first person, plain prose. Describe how you run
   an engagement: what you do first, how you work with the client, and how you report back. It is
   an approach, not a claim: add no credential, employer, client, figure, number of years or
   example of past work that the input does not state, and promise no outcome. Match the register
   of about_bio.
5. Prose imperfection: {imperfection_instruction}

If a prose imperfection is specified (anything other than "none"):
- Apply exactly ONE natural instance of it, in about_bio or in one achievement.
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

Test each achievement with: "and then what happened?" If the sentence can't answer that with a
concrete outcome or result, it is not an achievement -- rewrite it or drop it.

The title, credentials, years_experience, services and technical_proficiency are not yours to
change; they are restored from the input exactly as they are.
