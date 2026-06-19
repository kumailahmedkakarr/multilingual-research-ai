# services/research_intelligence_service.py

from services.groq_service import ask_groq


def generate_research_intelligence(text):
    """
    Generate complete research intelligence from a research paper.
    """

    if not text or len(text.strip()) == 0:
        return "No research paper text provided."

    prompt = f"""
You are an expert academic research analyst.

Analyze the following research paper and generate a professional report.

RESEARCH PAPER:
{text[:12000]}

Provide the following sections:

1. Executive Summary

2. Research Domain

3. Research Problem

4. Research Objectives

5. Keywords

6. Methodology Analysis

7. Dataset / Data Sources Used

8. Key Findings

9. Strengths of the Research

10. Limitations of the Research

11. Novel Contributions

12. Practical Applications

13. Future Research Directions

14. Final Evaluation

Use professional academic language.
Use clear headings.
Make the response detailed and well structured.
"""

    try:
        return ask_groq(prompt)

    except Exception as e:
        return f"Research Intelligence Error: {str(e)}"