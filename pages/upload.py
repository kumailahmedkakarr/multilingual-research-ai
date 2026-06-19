import gradio as gr

def analyze_paper(file):

    if file is None:
        return "Please upload PDF"

    return f"Analysis completed for {file.name}"


def page():

    file = gr.File(
        label="Upload Research Paper"
    )

    btn = gr.Button(
        "Analyze Research",
        variant="primary"
    )

    output = gr.Textbox(
        lines=15
    )

    btn.click(
        fn=analyze_paper,
        inputs=file,
        outputs=output
    )