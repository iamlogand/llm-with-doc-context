import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator


# Load the OPENAI_API_KEY environment variable
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# Load the PDF and create a vectorstore
print("Loading document...")
loader = PyPDFLoader("LivingRules_v1.07.pdf")
index = VectorstoreIndexCreator().from_loaders([loader])

print("The data has been loaded. This is a Q&A, not a conversation. You can quit the application at any time using ctrl+c.")

while True:
  query = input("\nYour question: ")
  print("Loading answer...")
  answer = index.query(query)
  print(answer)
