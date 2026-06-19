from services.groq_service import ask_groq

def detect_gap(text):

    if not text or len(text.strip()) == 0:
        return "No paper content found."

    text = text[:6000]

    prompt = f"""
You are a research analyst.

Analyze the following research paper and identify:

1. Existing Work
2. Research Gaps
3. Missing Areas
4. Future Research Opportunities
5. Novel Research Directions

Paper Content:
{text}
"""

    return ask_groq(prompt)