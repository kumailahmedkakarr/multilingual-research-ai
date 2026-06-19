from services.groq_service import ask_groq


def generate_viva(topic, language):

    prompt = f"""
Generate 15 viva questions in {language}.

Research Topic:
{topic}

Also provide:
- Difficulty Level
- Expected Answers
"""
    return ask_groq(prompt)