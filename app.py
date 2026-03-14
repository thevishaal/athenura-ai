from flask import Flask, request, jsonify
import json
from services.post_generator import generate_social_media_content

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running"

@app.route("/generate_content", methods=["POST"]) #api endpoint
def generate():

    data = request.json

    topic = data.get("topic")
    platform = data.get("platform")
    tone = data.get("tone")

    # Validation
    if not topic or not platform or not tone:
        return jsonify({"error": "Missing required fields"}), 400

    content = generate_social_media_content(topic, platform, tone) #fn call
    
    # print("RAW AI RESPONSE:")
    # print(content)


    try:
        cleaned = content.replace("```json", "").replace("```", "")
        ideas_json = json.loads(cleaned)
    except json.JSONDecodeError:
        return jsonify({"error": "AI response parsing failed"}), 500


    # print("Generate route hit")

    return jsonify(ideas_json)

if __name__ == "__main__":
    app.run(debug=True)