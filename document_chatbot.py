import os
import random
import time
import subprocess
import requests
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain import HuggingFaceHub


from os import environ

    
class DocumentChatbot:
    
    def __init__(self):
        self.llm = None
        self.chain = None
        self.embeddings = None
        self.metadata = {"source": "internet"}
        self.init_mes = ["According to the document, ", "Based on the text, ", "I think, ", "According to the text, ", "Based on the document you provided, "]
        
    
    def load_token_and_model(self, api_key, model_name):
        result = None
        if api_key[:2] == "hf":
            os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_key
            result = subprocess.run(["curl", "https://huggingface.co/api/whoami-v2", "-H", f"Authorization: Bearer {api_key}"], capture_output=True).stdout.decode()
        if result == '{"error":"Invalid username or password."}':
            return  "Invalid API token"
        else:
            self.llm = HuggingFaceHub(repo_id=model_name, model_kwargs={"temperature":0, "max_length":512})
            self.chain = load_qa_chain(self.llm, chain_type="stuff")
            self.embeddings = HuggingFaceEmbeddings()
            return "Model and Token successfully loaded"
        

    def respond(self, text_input, question, chat_history):
        if not question or question.isspace():
            return "Please enter a valid question.", chat_history
        if text_input.startswith("http"):
            response = requests.get(text_input)
            text_var = response.text
            if text_var is None:
                raise ValueError("No document is given")
        else:
            text_var = text_input
            


        time.sleep(0.5)

        documents = [Document(page_content=text_var, metadata=self.metadata)]
        text_splitter = CharacterTextSplitter(chunk_size=750, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        if self.llm is None:
            raise ValueError("Model not loaded")
            


        db = FAISS.from_documents(docs, self.embeddings)
        query = question
        
        try:
            docs = db.similarity_search(query)
            answer = self.chain.run(input_documents=docs, question=query)
            bot_message = random.choice(self.init_mes) + answer + "."
        except ValueError as e:
            bot_message = f"An error occurred: {str(e)}"
        chat_history.append((question, bot_message))

        time.sleep(1)
        
        return "", chat_history
