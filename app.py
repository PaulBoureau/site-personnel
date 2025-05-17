from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Ta clé API Together.ai
API_KEY = "46aeebb6c697d1ac9b0c180b977df331bc135ed8a0284d9d7b11cf741f99a8ac"  # Remplace par ta clé API

@app.route("/api", methods=["POST"])
def api():
    user_prompt = request.json.get("prompt", "")

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/Mistral-7B-Instruct-v0.1",
            "messages": [{"role": "user", "content": user_prompt}],
            "temperature": 0.7,
            "max_tokens": 300
        }
    )

    data = response.json()
    reponse = data["choices"][0]["message"]["content"]
    return jsonify({"reponse": reponse})

# Partie essentielle pour Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render fournit PORT dans l'environnement
    app.run(host="0.0.0.0", port=port)

