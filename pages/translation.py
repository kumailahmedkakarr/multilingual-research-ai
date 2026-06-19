import gradio as gr
from services.translation_service import translate_text


def page():

    text = gr.Textbox(
        lines=10,
        label="Research Text"
    )

    language = gr.Dropdown(
        [
            "English",
            "Urdu",
            "Pashto",
            "Punjabi",
            "Sindhi",
            "Balochi"
        ],
        value="Urdu"
    )

    btn = gr.Button(
        "Translate",
        variant="primary"
    )

    output = gr.Textbox(
        lines=15
    )

    btn.click(
        fn=translate_text,
        inputs=[text, language],
        outputs=output
    )