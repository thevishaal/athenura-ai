from groq import Groq
from core.config import GROQ_API_KEY, GROQ_MODEL


client = Groq(api_key=GROQ_API_KEY)

def generate_blog_content(topic, word_count, tone, style, audience, external_thoughts=None):

    BLOG_PROMPT = f"""

Act as a professional SEO content writer, expert blogger, and tone-adaptive copywriter.

Your primary goal is to generate a high-quality, SEO-optimized blog post that STRICTLY adapts to the requested tone and writing style.

INPUT:
Topic: {topic}
Target Word Count: {word_count}
Tone: {tone}
Writing Style: {style}
Target Audience: {audience}
Additional Context: {external_thoughts}

CRITICAL TONE ENFORCEMENT:

You MUST strictly follow the given tone. Use the guidelines below:

- If tone = "professional":
  → Use formal language, structured sentences, no slang, authoritative voice.

- If tone = "casual":
  → Use conversational language, contractions, relatable examples, friendly vibe.

- If tone = "persuasive":
  → Use emotional triggers, strong hooks, compelling arguments, call-to-action.

- If tone = "storytelling":
  → Use narrative flow, real-life examples, descriptive language.

- If tone = "technical":
  → Use precise terminology, concise explanations, data-driven approach.

- If tone = "friendly":
  → Warm, approachable, supportive language.

IMPORTANT:
- The tone MUST be clearly distinguishable throughout the blog.
- Do NOT default to neutral tone.
- Each paragraph should reflect the tone consistently.

WRITING STYLE ENFORCEMENT:

- If style = "short & crisp":
  → Short sentences, minimal fluff.

- If style = "detailed":
  → In-depth explanations, examples, expanded insights.

- If style = "analytical":
  → Break down concepts logically, include comparisons.

- If style = "engaging":
  → Use hooks, rhetorical questions, dynamic flow.

SEO INSTRUCTIONS:

- Naturally include primary + related keywords.
- Optimize headings (H1, H2).
- Keep readability high (avoid long dense paragraphs).
- Use bullet points where helpful.

CONTEXT HANDLING:
- If additional context exists → integrate + expand it.
- Else → generate expert-level content.

OUTPUT STRUCTURE (STRICT JSON ONLY):
{{
  "title": "",
  "meta_description": "",
  "introduction": "",
  "sections": [
    {{
      "heading": "",
      "content": ""
    }}
  ],
  "tips": [
    "",
    "",
    ""
  ],
  "key_takeaways": [
    "",
    "",
    ""
  ],
  "faq": [
    {{
      "question": "",
      "answer": ""
    }}
  ],
  "conclusion": ""
}}

FINAL RULES:

- Output ONLY valid JSON.
- NO markdown, NO explanations.
- Ensure clean formatting.
- Ensure tone difference is OBVIOUS even to a non-expert reader.
"""
    chat_completion = client.chat.completions.create(
        model = GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional SEO content writer and expert blogger."
            },
            {
                "role": "user",
                "content": BLOG_PROMPT
            }
        ],
        response_format={"type": "json_object"},
    )

    result = chat_completion.choices[0].message.content
    return result