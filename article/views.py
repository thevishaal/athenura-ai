import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from groq import Groq
from dotenv import load_dotenv

# create client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Article Prompt
ARTICLE_PROMPT = """
You are a professional content writer.

Write a high-quality, engaging article.

Topic: {topic}
Word Count: {word_count}
Tone: {tone}
Style: {style}
Audience: {audience}

Additional Context: {external_thoughts}

Instructions:
- Write in simple and clear language
- Use headings and paragraphs
- Make it engaging and human-like
- Do NOT return JSON
- Return clean article text only
"""


# View
@login_required
def article(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        word_count = int(request.POST.get("word_count"))
        tone = request.POST.get("tone")
        style = request.POST.get("style")
        audience = request.POST.get("audience")
        external_thoughts = request.POST.get("external_thoughts")

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": ARTICLE_PROMPT.format(
                        topic=topic,
                        word_count=word_count,
                        tone=tone,
                        style=style,
                        audience=audience,
                        external_thoughts=external_thoughts or "None"
                    )
                }
            ],
            model=os.getenv("GROQ_MODEL"),
            temperature=0.7
        )

        result = chat_completion.choices[0].message.content

        # optional: markdown to html
        html_article = markdown.markdown(result)

        return render(
            request,
            "article/partials/article_result.html",
            {"article": html_article}
        )

    return render(request, "article/article.html")