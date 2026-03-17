from groq import Groq
from core.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def generate_caption_content(topic, platform, tone):
    CAPTION_PROMPT = f"""
You are an expert social media content creator.

Your task is to generate engaging captions along with relevant hashtags based on user input.

User Input:
- Topic: {topic}
- Platform: {platform}
- Tone: {tone}

Instructions:
1. Generate exactly 5 captions.
2. Each caption must be short (max 1–2 lines, under 20 words).
3. Match the tone strictly (e.g., inspirational, funny, professional, casual).
4. Adapt captions based on platform:
   - Instagram → catchy + emojis + emotional
   - LinkedIn → professional + insight-driven
   - Twitter → concise + punchy
   - Facebook → conversational + relatable
   - YouTube → curiosity-driven
5. For each caption, generate 3–5 relevant hashtags.
6. Hashtags must be:
   - lowercase
   - no spaces
   - relevant to topic + platform
7. Avoid generic or repeated captions.
8. Do NOT include explanations.

Output Format (STRICT JSON):
{{
  "captions": [
    {{
      "text": "caption here",
      "hashtags": ["#tag1", "#tag2", "#tag3"]
    }},
    {{
      "text": "caption here",
      "hashtags": ["#tag1", "#tag2", "#tag3"]
    }}
  ]
}}
"""
    chat_completion = client.chat.completions.create(
        model = GROQ_MODEL,
        messages = [
            {
                "role": "system",
                "content": "You are an expert social media content creator."
            },
            {
                "role": "user",
                "content": CAPTION_PROMPT
            }
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )

    result = chat_completion.choices[0].message.content
    return result