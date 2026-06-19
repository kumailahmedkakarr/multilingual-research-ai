import gradio as gr

def page():

    with gr.Column():

        gr.HTML("""
        <div class="hero">
            <h1>🚀 ResearchMate X</h1>
            <h2>AI Research Operating System</h2>
            <p>Multilingual Research Intelligence Platform</p>
        </div>
        """)

        gr.Markdown("## 📊 Dashboard")

        with gr.Row():

            gr.HTML("""
            <div class="card">
            <h1>🌍</h1>
            <h2>24</h2>
            <p>Languages</p>
            </div>
            """)

            gr.HTML("""
            <div class="card">
            <h1>📚</h1>
            <h2>120K+</h2>
            <p>Papers</p>
            </div>
            """)

            gr.HTML("""
            <div class="card">
            <h1>🤖</h1>
            <h2>5</h2>
            <p>Models</p>
            </div>
            """)

            gr.HTML("""
            <div class="card">
            <h1>🔎</h1>
            <h2>E5</h2>
            <p>Embeddings</p>
            </div>
            """)

        gr.Markdown("""
## 🚀 Demo Workflow

📄 Chinese Research Paper

➡ AI Analysis

➡ Research Gap Detection

➡ Urdu Summary

➡ Balochi Proposal

➡ Pashto Viva
""")