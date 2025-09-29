import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Allows frontend requests

client = OpenAI(api_key=api_key)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4.1"
            messages=[{"role": "user", "content": user_message}]
        )

        bot_reply = response.choices[0].message["content"]
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
