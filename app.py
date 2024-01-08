# Tasrif Nur Himel

from flask import Flask, request, jsonify,render_template
import requests

app = Flask(__name__)

@app.route('/')
def render_html():
    return render_template('index.html')

@app.route('/api/gpt-response', methods=['POST'])
def get_gpt_response():
    prompt = request.json['prompt']
    url = "https://open-ai21.p.rapidapi.com/conversationgpt35"

    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "web_access": False,
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "Use Your Api",
        "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    result = response.json().get("result", "Sorry, I couldn't understand that.")

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
