import os
import random
import time
import gradio as gr
from document_chatbot import DocumentChatbot

document_chatbot = DocumentChatbot()

with gr.Blocks() as demo:
    title = """<p><h1 align="center" style="font-size: 36px;">Talk with your document</h1></p>"""
    gr.HTML(title)
    with gr.Row():
        text_input = gr.Textbox(label="Enter text or URL to text file")
        with gr.Column():
            with gr.Row():
                api_key_input = gr.Textbox(label="Enter HF Token")
                picked_model = gr.Dropdown(["google/flan-t5-large", "google/flan-t5-base","google/flan-t5-small"], label="Models", interactive=True)
                load_configs = gr.Button("Load configs")
                load_configs.click(document_chatbot.load_token_and_model, inputs=[api_key_input, picked_model], outputs=[api_key_input])
                
            chatbot = gr.Chatbot()

            q_input = gr.Textbox(label="Please write your question")
            clear = gr.Button("Clear")
            q_input.submit(document_chatbot.respond, [text_input, q_input, chatbot], [q_input, chatbot])
            clear.click(lambda: None, None, chatbot, queue=False)
        
        
demo.launch(debug=True)