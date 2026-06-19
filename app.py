import os
import gradio as gr

from services.translation_service import translate_text
from services.proposal_service import generate_proposal
from services.viva_service import generate_viva
from services.pdf_service import extract_pdf_text

try:
    from services.research_gap_service import detect_gap
except:
    def detect_gap(text):
        return "Research Gap Service Not Found"

try:
    from services.literature_review_service import generate_literature_review
except:
    def generate_literature_review(topic):
        return "Literature Review Service Not Found"

try:
    from services.citation_service import generate_citations
except:
    def generate_citations(text):
        return "Citation Service Not Found"

try:
    from services.workflow_service import generate_workflow
except:
    def generate_workflow(topic):
        return "Workflow Service Not Found"


# ==========================================
# LOAD CSS
# ==========================================

css = ""

if os.path.exists("assets/style.css"):
    with open("assets/style.css", "r", encoding="utf-8") as f:
        css = f.read()


# ==========================================
# PDF ANALYSIS
# ==========================================

def analyze_paper(file):

    if file is None:
        return "Please upload a PDF."

    try:

        text = extract_pdf_text(file.name)

        preview = text[:3000]

        return f"""
PDF Loaded Successfully

File:
{file.name}

==================================

{preview}
"""

    except Exception as e:
        return str(e)


# ==========================================
# PAGE SWITCH
# ==========================================

def show_workspace(page):

    return (
        gr.update(visible=page=="research"),
        gr.update(visible=page=="translation"),
        gr.update(visible=page=="proposal"),
        gr.update(visible=page=="viva"),
        gr.update(visible=page=="gap"),
        gr.update(visible=page=="literature"),
        gr.update(visible=page=="citation"),
        gr.update(visible=page=="workflow")
    )


# ==========================================
# APP
# ==========================================

with gr.Blocks(
    title="ResearchMate X"
) as demo:

    # TOPBAR

    with gr.Row(elem_classes="topbar"):

        if os.path.exists("assets/logo.png"):

            gr.Image(
                "assets/logo.png",
                elem_id="main_logo",
                show_label=False,
                container=False
            )

        else:
            gr.Markdown("# ResearchMate X")

    # TITLE

    gr.HTML("""
    <div class='dashboard-header'>
        <h1>ResearchMate X</h1>
        <p>AI Research Operating System</p>
    </div>
    """)

    # DASHBOARD

    with gr.Row():

        research_card = gr.Button(
            "📄 Research Intelligence",
            elem_classes="card-btn"
        )

        translation_card = gr.Button(
            "🌐 Translation Studio",
            elem_classes="card-btn"
        )

        proposal_card = gr.Button(
            "📑 Proposal Builder",
            elem_classes="card-btn"
        )

        viva_card = gr.Button(
            "🎤 Viva Coach",
            elem_classes="card-btn"
        )

    with gr.Row():

        gap_card = gr.Button(
            "🔍 Gap Finder",
            elem_classes="card-btn"
        )

        literature_card = gr.Button(
            "📚 Literature Review",
            elem_classes="card-btn"
        )

        citation_card = gr.Button(
            "🔗 Citation Generator",
            elem_classes="card-btn"
        )

        workflow_card = gr.Button(
            "📝 Workflow Generator",
            elem_classes="card-btn"
        )

    # ==========================================
    # RESEARCH
    # ==========================================

    with gr.Group(visible=True, elem_classes="workspace") as research_section:

        gr.Markdown("## Research Intelligence")

        file = gr.File(file_types=[".pdf"])

        analyze_btn = gr.Button("Analyze Paper")

        result = gr.Textbox(lines=15)



            # TRANSLATION

    with gr.Group(visible=False, elem_classes="workspace") as translation_section:

        text = gr.Textbox(lines=10)

        language = gr.Dropdown(
            ["English","Urdu","Pashto","Punjabi","Sindhi","Balochi"],
            value="Urdu"
        )

        translate_btn = gr.Button("Translate")

        translation_output = gr.Textbox(lines=15)

    # PROPOSAL

    with gr.Group(visible=False, elem_classes="workspace") as proposal_section:

        topic = gr.Textbox()

        lang = gr.Dropdown(
            ["English","Urdu","Pashto","Punjabi","Sindhi","Balochi"],
            value="English"
        )

        proposal_btn = gr.Button("Generate Proposal")

        proposal_output = gr.Textbox(lines=20)

    # VIVA

    with gr.Group(visible=False, elem_classes="workspace") as viva_section:

        viva_topic = gr.Textbox()

        viva_lang = gr.Dropdown(
            ["English","Urdu","Pashto"],
            value="English"
        )

        viva_btn = gr.Button("Generate Viva")

        viva_output = gr.Textbox(lines=20)

    # GAP

    with gr.Group(visible=False, elem_classes="workspace") as gap_section:

        gap_text = gr.Textbox(lines=10)

        gap_btn = gr.Button("Detect Gaps")

        gap_output = gr.Textbox(lines=15)

    # LITERATURE

    with gr.Group(visible=False, elem_classes="workspace") as literature_section:

        literature_topic = gr.Textbox()

        literature_btn = gr.Button("Generate Review")

        literature_output = gr.Textbox(lines=20)

    # CITATION

    with gr.Group(visible=False, elem_classes="workspace") as citation_section:

        citation_text = gr.Textbox(lines=10)

        citation_btn = gr.Button("Generate Citations")

        citation_output = gr.Textbox(lines=15)

    # WORKFLOW

    with gr.Group(visible=False, elem_classes="workspace") as workflow_section:

        workflow_topic = gr.Textbox()

        workflow_btn = gr.Button("Generate Workflow")

        workflow_output = gr.Textbox(lines=15)

    outputs = [
        research_section,
        translation_section,
        proposal_section,
        viva_section,
        gap_section,
        literature_section,
        citation_section,
        workflow_section
    ]

    # NAVIGATION

    research_card.click(lambda: show_workspace("research"), outputs=outputs)
    translation_card.click(lambda: show_workspace("translation"), outputs=outputs)
    proposal_card.click(lambda: show_workspace("proposal"), outputs=outputs)
    viva_card.click(lambda: show_workspace("viva"), outputs=outputs)
    gap_card.click(lambda: show_workspace("gap"), outputs=outputs)
    literature_card.click(lambda: show_workspace("literature"), outputs=outputs)
    citation_card.click(lambda: show_workspace("citation"), outputs=outputs)
    workflow_card.click(lambda: show_workspace("workflow"), outputs=outputs)

    # ACTIONS

    analyze_btn.click(
        analyze_paper,
        inputs=file,
        outputs=result
    )

    translate_btn.click(
        translate_text,
        [text, language],
        translation_output
    )

    proposal_btn.click(
        generate_proposal,
        [topic, lang],
        proposal_output
    )

    viva_btn.click(
        generate_viva,
        [viva_topic, viva_lang],
        viva_output
    )

    gap_btn.click(
        detect_gap,
        gap_text,
        gap_output
    )

    literature_btn.click(
        generate_literature_review,
        literature_topic,
        literature_output
    )

    citation_btn.click(
        generate_citations,
        citation_text,
        citation_output
    )

    workflow_btn.click(
        generate_workflow,
        workflow_topic,
        workflow_output
    )

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        css=css,
        theme=gr.themes.Soft(),
        share=False
    )