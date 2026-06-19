from services.groq_service import ask_groq

def generate_citations(text):

    prompt = f"""
Generate APA, IEEE and Harvard citations.

Text:
{text}
"""

    return ask_groq(prompt)