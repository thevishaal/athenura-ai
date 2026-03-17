from groq import Groq
from core.config import GROQ_API_KEY, GROQ_MODEL


client = Groq(api_key=GROQ_API_KEY)

def generate_blog_content(topic, word_count, tone, style, audience, external_thoughts=None):

    BLOG_PROMPT = f"""

You are a professional SEO content writer and expert blogger.

Your task is to generate a high-quality, engaging, and SEO-optimized blog post.

USER INPUT

Topic: {topic}
Target Word Count: {word_count}
Tone: {tone}
Writing Style: {style}
Target Audience: {audience}

Additional Context (Optional): {external_thoughts}

IMPORTANT RULES

1. Write a complete blog post close to the requested word count.
2. Maintain the requested tone and writing style.
3. Write in a natural, human-like style.
4. Use SEO best practices.
5. Use headings, subheadings, and bullet points where helpful.
6. Provide practical insights, tips, and examples.

SPECIAL INSTRUCTION ABOUT ADDITIONAL CONTEXT

If "Additional Context" is provided:
- Use the information naturally in the blog.
- Expand upon those ideas.

If no additional context is provided:
- Generate the blog using your own knowledge and expertise.

BLOG STRUCTURE

1. Title
Generate an engaging SEO-friendly blog title.

2. Meta Description
Write a 150–160 character meta description.

3. Introduction
Write an engaging introduction that hooks the reader.

4. Main Sections
Create structured sections using H2 headings and detailed content.

5. Tips / Best Practices
Add actionable tips related to the topic.

6. Key Takeaways
Summarize the most important insights.

7. FAQ Section
Generate 3–5 relevant questions with answers.

8. Conclusion
Write a strong concluding paragraph.

IMPORTANT OUTPUT RULES

- Return the response ONLY in valid JSON format.
- Do NOT include markdown.
- Do NOT include explanations outside JSON.
- Ensure the JSON is properly structured and valid.

OUTPUT FORMAT

{{
  "title": "",
  "meta_description": "",
  "introduction": "",
  "sections": [
    {{
      "heading": "",
      "content": ""
    }},
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
    }},
    {{
      "question": "",
      "answer": ""
    }}
  ],
  "conclusion": ""
}}
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
        temperature=0.7
    )

    result = chat_completion.choices[0].message.content
    return result