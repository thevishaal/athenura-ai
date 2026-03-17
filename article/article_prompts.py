from groq import Groq
from core.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def generate_article_content(topic, word_count, tone, style, audience, external_thoughts=None):

    ARTICLE_PROMPT = f"""
You are a professional content writer.

Write a high-quality, engaging article.

Topic: {topic}
Word Count: {word_count}
Tone: {tone}
Style: {style}
Audience: {audience}

Additional Context: {external_thoughts}

Instructions:
- Write in a simple and clear way
- Use headings and paragraphs
- Make it human-like and engaging
- No JSON, no formatting instructions

Return only clean article text.
"""

    chat_completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": ARTICLE_PROMPT
            }
        ],
        temperature=0.7
    )

    result = chat_completion.choices[0].message.content
    return result