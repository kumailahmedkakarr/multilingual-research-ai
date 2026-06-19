from services.groq_service import ask_groq


def generate_proposal(topic, language):

    prompt = f"""
Generate a complete research proposal in {language}.

Topic:
{topic}

Include:
- Title
- Objectives
- Methodology
- Expected Outcomes
"""
    return ask_groq(prompt)