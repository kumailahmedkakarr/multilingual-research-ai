from services.groq_service import ask_groq

def generate_literature_review(topic):

    prompt = f"""
Generate a detailed literature review.

Topic:
{topic}

Include:

1. Introduction
2. Existing Studies
3. Comparative Analysis
4. Research Gaps
5. Conclusion
"""

    return ask_groq(prompt)