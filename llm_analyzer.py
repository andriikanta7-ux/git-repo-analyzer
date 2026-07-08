from google import genai
from dotenv import load_dotenv
import os
import json
import re


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_repository(context):

    prompt = f"""
Analyze this GitHub repository.

Repository context:

{context}

Return ONLY valid JSON.
No markdown.
No explanations.

JSON format:

{{
    "summary": "",
    "technologies": [],
    "strengths": [],
    "issues": [],
    "recommendations": []
}}
"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )


    text = response.text.strip()


    try:
        return json.loads(text)

    except json.JSONDecodeError:

    
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass


        return {
            "summary": text,
            "technologies": [],
            "strengths": [],
            "issues": [],
            "recommendations": []
        }