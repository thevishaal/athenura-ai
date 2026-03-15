from groq import Groq
from social_media.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_social_media_content(topic, platform, tone):

    prompt = f"""
    Generate social media content for:

    Topic: {topic}
    Platform: {platform}
    Tone: {tone}

    Return JSON in this exact format:

{{
  "carousel": {{
    "title": "Catchy carousel title",
    "slides": [
      "Hook slide",
      "Point 1",
      "Point 2",
      "Point 3",
      "Call to action"
    ]
  }},
  "reel": {{
    "hook": "Scroll stopping hook",
    "script": [
      "Scene 1 description",
      "Scene 2 description",
      "Scene 3 description"
    ],
    "cta": "Call to action for viewers"
  }},
  "poll": {{
    "question": "Interactive poll question",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ]
  }},
  "educational": {{
    "title": "Educational post title",
    "post": "Detailed educational caption"
  }},
  "engagement": {{
    "post": "Community engagement post encouraging comments",
    "suggested_time": "Best time to post"
  }}
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", #generates ideas
        messages=[{
            "role": "system",
            "content": "You are an API that ONLY returns valid JSON. Never include explanations, markdown, or text outside JSON."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
        response_format={"type": "json_object"}  
    )

    return response.choices[0].message.content