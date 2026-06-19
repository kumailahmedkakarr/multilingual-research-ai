from services.groq_service import ask_groq

def generate_workflow(topic):

    prompt = f"""
Create a complete research workflow.

Topic:
{topic}

Include:

1. Objectives
2. Methodology
3. Data Collection
4. Analysis
5. Results
6. Future Work
"""

    return ask_groq(prompt)