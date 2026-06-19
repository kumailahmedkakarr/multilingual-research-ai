from services.groq_service import ask_groq


def translate_text(text, language):

    prompt = f"""
Translate the following research text into {language}.

Text:
{text}
"""

    return ask_groq(prompt)