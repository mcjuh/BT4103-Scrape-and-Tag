{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ProviderDocument",
  "type": "object",
  "required": [
    "extracted_by_model"
  ],
  "properties": {
    "extracted_by_model": {
      "type": "string",
      "description": "SOCLAAS model that extracted this record: one of MODEL_POOL in classifier_extractor/llm_pool.py."
    },
    "about_title": {
      "type": [
        "string",
        "null"
      ],
      "description": "Short personal headline, e.g. \"Ex-CTO\"."
    },
    "about_description": {
      "type": [
        "string",
        "null"
      ],
      "description": "Personal \"about me\" narrative describing the provider's own career."
    },
    "services_offered_title": {
      "type": [
        "string",
        "null"
      ],
      "description": "Short name for a service the provider personally offers, e.g. \"CTO Services\"."
    },
    "services_offered_description": {
      "type": [
        "string",
        "null"
      ],
      "description": "What the personally-offered service concretely includes."
    },
    "relevant_experience": {
      "type": [
        "string",
        "null"
      ],
      "description": "Specific past roles, employers, or achievements relevant to the provider's expertise."
    }
  },
  "additionalProperties": false
}
