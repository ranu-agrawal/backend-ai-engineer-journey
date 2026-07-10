from dotenv import load_dotenv
# from openai import OpenAI
from groq import Groq
import os

load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

resume = """
Name: Ranu Sharma
Experience: 2 years at EY
Skills: Java, SQL, Python, Spring Boot, Boomi
"""

job_description = """
We are looking for a Backend Engineer with:
- Strong Java and Spring Boot experience
- SQL and database knowledge
- Docker and Kubernetes experience
- REST API development
- CI/CD pipeline knowledge
"""

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

print(response.choices[0].message.content)
