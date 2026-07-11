from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    resume = data.get("resume")
    job_description = data.get("job_description")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an ATS resume analyzer. Analyze the resume against the job description and provide: 1) ATS match score out of 100, 2) Missing skills, 3) Recommendations. Be concise."
            },
            {
                "role": "user",
                "content": f"Resume: {resume}\n\nJob Description: {job_description}"
            }
        ]
    )
    return jsonify({
        "analysis": response.choices[0].message.content
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
