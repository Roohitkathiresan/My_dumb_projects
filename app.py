import gradio as gr
from models import ModelManager
from ragpipeline import build_context

tutor = ModelManager()
chat_history = []

def chat(user_input):
    global chat_history
    context = build_context(user_input)
    response = tutor.ask(user_input, context)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": response})
    return chat_history, chat_history

with gr.Blocks() as demo:
    gr.Markdown(" EduGenie - AI Tutor ")
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(placeholder="Ask a question...")
    msg.submit(chat, inputs=msg, outputs=[chatbot, chatbot])

if __name__ == "__main__":
    demo.launch()