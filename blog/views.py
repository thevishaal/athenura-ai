import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .blog_prompts import BLOG_PROMPT
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import markdown

# create client 
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Create your views here.
@login_required
def blog(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        word_count = int(request.POST.get("word_count"))
        tone = request.POST.get("tone")
        style = request.POST.get("style")
        audience =  request.POST.get("audience")
        external_thoughts = request.POST.get("external_thoughts")

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": BLOG_PROMPT.format(
                        topic=topic,
                        word_count=word_count,
                        tone=tone,
                        style=style,
                        audience=audience,
                        external_thoughts=external_thoughts or "None"
                    )
                }
            ],
            model=os.getenv("GROQ_MODEL")
        )

        result = chat_completion.choices[0].message.content
        html_blog = markdown.markdown(result)
        return render(request, "blog/partials/blog_result.html", {"blog": html_blog})
    return render(request, "blog/blog.html")