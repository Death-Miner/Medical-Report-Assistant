import os

from dotenv import load_dotenv
from google import genai

from src.safety import (
    detect_sensitive_question,
    safety_message
)


load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing from .env"
    )


client = genai.Client(
    api_key=API_KEY
)


SYSTEM_INSTRUCTION = """
You are a Medical Report Explanation Assistant.

Your purpose is to help users understand information
that appears in their uploaded medical report.

RULES:

1. Do not diagnose diseases.
2. Do not prescribe medicines.
3. Do not recommend medication dosage.
4. Do not recommend treatment.
5. Do not invent values.
6. Do not invent reference ranges.
7. Do not invent findings.
8. Use the provided report as the primary source.
9. Clearly distinguish report information from general
   educational explanations.
10. If the report does not contain enough information,
    explicitly say that it cannot be determined.
11. Explain medical terminology in simple language.
12. Encourage consultation with a qualified healthcare
    professional when medical decisions are involved.

Never present an abnormal laboratory result as proof
of a disease.
"""


def ask_question(
    report_data,
    question,
    chat_history=None
):

    if chat_history is None:
        chat_history = []

    # Safety check

    if detect_sensitive_question(question):

        return safety_message()


    history = ""

    for message in chat_history:

        history += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )


    prompt = f"""
{SYSTEM_INSTRUCTION}

REPORT:

{report_data}


CONVERSATION HISTORY:

{history}


USER QUESTION:

{question}


Answer clearly and simply.
Use only information supported by the report
when discussing the user's specific results.
"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text