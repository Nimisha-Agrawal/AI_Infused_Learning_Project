# # pip install gradio
# import gradio as gr
# from summarizer import summarize

# gr.Interface(
#     fn=summarize,                                  # your function
#     inputs=gr.Textbox(label="Website URL"),
#     outputs=gr.Markdown(label="Summary"),
#     title="🔎 AI Website Summarizer",
# ).launch(share=True)   # share=True → a public link you can post! 🎉

import gradio as gr
from agent import agent              # the function you just wrote

def chat(message, history):          # ① Gradio fills these two in for you
    return agent(message)

gr.ChatInterface(fn=chat, title="🛍️ Smart Shop Assistant").launch(share=True)  # ②