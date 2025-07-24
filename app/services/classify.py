import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

# open_ai key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def classify_message(message: str) -> str:

    system_prompt = """You are an AI assistant that classifies customer messages into one of the following categories. You must return ONLY a valid JSON response with no additional text.

CATEGORIES:
- bug_report
- feature_request
- general_inquiry

 for bug report:
  {
  "message_type": "bug_report",
  "confidence_score": 0.0-1.0,
  "response_data": {
    "ticket": {
      "id": "BUG-1001",
      "title": "Brief description of the issue",
      "severity": "Low|Medium|High|Critical",
      "affected_component": "Component or feature affected",
      "reproduction_steps": ["Step 1", "Step 2", "Step 3"],
      "priority": "Low|Medium|High|Critical",
      "assigned_team": "Engineering|QA|DevOps"
    }
  },
  "customer_response": "Thank you for reporting this issue."
}

for feature request :

    {
  "message_type":"feature_request",
  "confidence_score": 0.0-1.0,
  "response_data": {
    "product_requirement": {
      "id": "FR-2001",
      "title": "Brief feature title",
      "description": "Detailed feature description",
      "user_story": "As a [user type], I want [functionality] so that [benefit]",
      "business_value": "High|Medium|Low - explanation of value",
      "complexity_estimate": "Low|Medium|High|Complex",
      "affected_components": ["Component 1", "Component 2"],
      "status": "Under Review"
    }
  },
  "customer_response": "Thank you for your feature suggestion."
}

}

For GENERAL INQUIRIES:
{
  "message_type": "general_inquiry",
  "confidence_score": 0.0-1.0,
  "response_data": {
    "inquiry_category": "Account Management|Billing|Usage Question|Technical Support|Other",
    "requires_human_review": true,
    "suggested_resources": [
      {"title": "Resource Name", "url": "https://example.com/help"}
    ]
  },
  "customer_response": "Thank you for your inquiry. We'll get back to you shortly with the information you need."
}

ID GENERATION RULES:
- Bug reports: BUG-XXXX (where XXXX is 4-digit number)
- Feature requests: FR-XXXX (where XXXX is 4-digit number)
- Use unique sequential numbers for each type

IMPORTANT:
- Return ONLY valid JSON, no markdown formatting or additional text
- Ensure all JSON brackets and commas are properly placed
- Use realistic confidence scores between 0.7-1.0
- Make customer responses helpful and professional
- Classify ambiguous messages as general_inquiry with lower confidence"""

    user_prompt = f"Customer message: '{message}'\n\nClassify this message and return the JSON response:"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )

    # Validate JSON response
    try:
        json_response = response.choices[0].message.content
        json.loads(json_response)
        return json_response
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response from OpenAI")
