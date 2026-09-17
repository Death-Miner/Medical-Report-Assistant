MEDICAL_DECISION_KEYWORDS = [
    "diagnose",
    "diagnosis",
    "medicine",
    "medication",
    "tablet",
    "drug",
    "prescription",
    "dose",
    "dosage",
    "treatment",
    "cure",
    "should i take",
    "what should i take"
]


def detect_sensitive_question(question):

    question_lower = question.lower()

    for keyword in MEDICAL_DECISION_KEYWORDS:

        if keyword in question_lower:
            return True

    return False


def safety_message():

    return (
        "I can explain information contained in your "
        "report, but I cannot diagnose a condition, "
        "prescribe medication, recommend a dosage, or "
        "replace a qualified healthcare professional. "
        "Please consult a doctor or other qualified "
        "healthcare professional for medical decisions."
    )