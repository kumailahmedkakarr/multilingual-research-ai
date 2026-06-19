import gradio as gr
from services.viva_service import generate_viva


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
        "Generate Viva",
        variant="primary"
    )

    output = gr.Textbox(
        lines=20
    )

    btn.click(
        fn=generate_viva,
        inputs=[topic, lang],
        outputs=output
    )