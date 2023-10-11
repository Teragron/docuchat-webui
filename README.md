# docuchat-webui

This project is a web-based chatbot that uses language processing techniques to answer questions based on a given document. It uses the langchain library for question answering, document splitting, and document loading. The web interface is built with Gradio, which allows users to enter text or a URL to a text file, select a model, and ask a question related to the document.

## Demo

[![Open in Spaces](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/teragron/docuchat-webui)

## Installation

1. Clone this repository.

```git clone https://github.com/teragron/docuchat-webui.git```

2. Install the required packages.

```pip install -r requirements.txt```

## Usage

1. Start the application.

```python app.py```

2. Enter a text or an URL to a text file.

3. Pick a model from the dropdown list.

4. Enter a question to ask the model.

The model will respond with an answer based on the input document and question.

You can clear the chat history by clicking the "Clear" button.

## Files

**document_chatbot.py**: contains the DocumentChatbot class that handles loading the model and generating responses.

**app.py**: contains the Gradio interface to interact with the chatbot.

**requirements.txt**: contains the required libraries to run the project.


## Dependencies

This project uses the following libraries:

**langchain**: for question answering, document splitting, and document loading

**huggingface_hub**: for loading models from Hugging Face Hub

**sentence_transformers**: for generating embeddings of documents

**gradio**: for building the web-based interface

**faiss-cpu**: for similarity search in the document vectors


## Acknowledgements

This project was built by Teragron and is based on the LangChain library created by NLP Odyssey. The LangChain library provides an easy-to-use interface for natural language processing tasks such as question answering and document similarity search. The Gradio library provides a simple way to create web-based interfaces for machine learning models.
