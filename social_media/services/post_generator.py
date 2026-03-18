from groq import Groq
from core.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)


def generate_social_media_content(topic, platform, tone):

    prompt = f"""
Act as a social media strategist, content creator, and platform-specific growth expert.

Your task is to generate HIGH-QUALITY, ENGAGING, and PLATFORM-OPTIMIZED social media content ideas.

INPUT:
Topic: {topic}
Platform: {platform}
Tone: {tone}

CRITICAL TONE ENFORCEMENT:

You MUST strictly follow the given tone:

- professional → formal, authoritative, structured
- casual → conversational, relatable, light tone
- persuasive → emotional, strong hooks, CTA-focused
- storytelling → narrative-driven, engaging flow
- technical → precise, informative, expert-level
- friendly → warm, supportive, approachable

IMPORTANT:
- Tone MUST be clearly visible in EVERY content type.
- Do NOT default to neutral tone.

PLATFORM ADAPTATION:

Adapt content style based on platform:

- Instagram → visual, hooks, short impactful text
- LinkedIn → professional, insights, value-driven
- Twitter → concise, punchy, high engagement
- Facebook → conversational, community-driven

CONTENT STRATEGY REQUIREMENTS:

- Each idea must be UNIQUE
- Focus on engagement + value
- Include strong hooks
- Keep content actionable
- Make it audience-focused

OUTPUT STRUCTURE (STRICT JSON ONLY):

{{
  "carousel": {{
    "title": "Catchy title",
    "slides": [
      "Hook slide",
      "Value point",
      "Value point",
      "Value point",
      "Call to action"
    ]
  }},
  "reel": {{
    "hook": "Scroll-stopping hook",
    "script": [
      "Scene 1",
      "Scene 2",
      "Scene 3"
    ],
    "cta": "Call to action"
  }},
  "poll": {{
    "question": "Engaging question",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ]
  }},
  "educational": {{
    "title": "Educational post title",
    "post": "Valuable educational content"
  }},
  "engagement": {{
    "post": "Community engaging content",
    "suggested_time": "Best time to post"
  }}
}}

FINAL RULES:
- Output ONLY valid JSON
- NO markdown, NO explanation
- NO extra text
- Maintain strict structure
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an API that only returns valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )

    return response.choices[0].message.content