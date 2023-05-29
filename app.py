import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator

# Load the OPENAI_API_KEY environment variable
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# If running as a bundled app, the _MEIPASS attribute is defined
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Find a file in the input folder
directory = os.path.join(base_path, 'input')
file_list = os.listdir(directory)
file_list = [file for file in file_list if os.path.isfile(os.path.join(directory, file))]
if file_list:
    file_name = file_list[0]
else:
    print('No files found in the input folder.')
    time.sleep(3)
    sys.exit()

# Load the PDF and create a vectorstore
print(f'Loading file: {file_name}')
loader = PyPDFLoader(os.path.join(directory, file_name))
index = VectorstoreIndexCreator().from_loaders([loader])

print('The data has been loaded. This is a Q&A, not a conversation. You can quit the application at any time using ctrl+c.')

while True:
  query = input('\nYour question: ')
  print('Loading answer...')
  answer = index.query(query)
  print(answer)
