import gradio as gr
from services.proposal_service import generate_proposal


def page():

    topic = gr.Textbox(
        label="Research Topic"
    )

    lang = gr.Dropdown(
        [
            "English",
            "Urdu",
            "Pashto",
            "Punjabi",
            "Sindhi",
            "Balochi"
        ],
        value="English"
    )

    btn = gr.Button(
        "Generate Proposal",
        variant="primary"
    )

    output = gr.Textbox(
        lines=20
    )

    btn.click(
        fn=generate_proposal,
        inputs=[topic, lang],
        outputs=output
    )