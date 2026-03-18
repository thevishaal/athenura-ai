from groq import Groq
from core.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def generate_article_structure(topic, tone, length, audience):
    ARTICLE_STRUCTURE = f"""
You are an expert content strategist specializing in SEO and long-form articles.

Your task is to generate a high-quality article blueprint based on the user's input.

User Input:
- Core Topic: {topic}
- Tone: {tone}
- Length: {length}
- Target Audience: {audience}

Instructions:
1. Generate an optimized, engaging, and SEO-friendly article title.
2. Create 4–6 structured main sections (like H2 headings).
3. For each section:
   - Add a short description (1–2 lines explaining what will be covered).
4. Generate 4–6 key discussion points (insightful, thought-provoking, slightly opinionated).
5. Make sure the output feels like a professional content blueprint.

Output Format (STRICT JSON):
{{
  "title": "Optimized article title",
  "content_structure": [
    {{
      "heading": "Section title",
      "description": "What this section will cover"
    }}
  ],
  "key_discussion_points": [
    "Insight 1",
    "Insight 2",
    "Insight 3"
  ]
}}
"""
    chat_completion = client.chat.completions.create(
        model = GROQ_MODEL,
        messages = [
            {
                "role": "system",
                "content" : "You are an expert content strategist specializing in SEO and long-form articles."
            },
            {
                "role": "user",
                "content": ARTICLE_STRUCTURE
            }
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )

    return chat_completion.choices[0].message.content


def generate_full_article(title, structure, tone, length, audience):
    FULL_ARTICLE_PROMPT = f"""
You are a professional SEO article writer.

Write a complete long-form article.

Inputs:
- Title: {title}
- Structure: {structure}
- Tone: {tone}
- Target Audience: {audience}
- Length: {length}

Instructions:
1. Write an engaging introduction.
2. Expand each section into detailed content (2–4 paragraphs each).
3. Maintain consistent tone.
4. Make content SEO-friendly and easy to read.
5. Add a strong conclusion.
6. Do NOT include anything outside JSON.
7. Return ONLY valid JSON.
8. Escape all special characters properly.
9. Do not include raw newlines inside JSON values.

Return STRICT JSON:
{{
  "title": "Article title",
  "introduction": "Intro paragraph",
  "sections": [
    {{
      "heading": "Section title",
      "content": "Detailed content..."
    }}
  ],
  "conclusion": "Conclusion paragraph",
  "meta_description": "SEO meta description (max 160 chars)"
}}
"""
    response = client.chat.completions.create(
        model=GROQ_MODEL, 
        messages=[
            {
                "role": "system", 
                "content": "You generate strictly valid json"
            },
            {
                "role": "user", 
                "content": FULL_ARTICLE_PROMPT
            }
        ],
        temperature=0.7,
    )

    content = response.choices[0].message.content.strip()

    return content