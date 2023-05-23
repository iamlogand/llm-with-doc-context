# LLM Q&A script that uses a document for context
A simple console script that uses a large language model (LLM) to answer questions specifically related to a given document. Uses the [langchain](https://github.com/hwchase17/langchain) framework and the OpenAI API.

The included sample document is the Republic of Rome rule book.


## Limitations

- It's not conversational - each question is unaware of previous questions and answers.
- It can only use one PDF at a time.

## How to run this

1. Create a python virtual environment (I used Python 3.11) and install the requirements within that environment.
3. Create a `.env` file. Within this file define a value for `OPENAI_API_KEY`, which needs to be a valid OpenAI API key.
4. Run the script. Here's how I run it:

   ```
   ./env/Scripts/python.exe ./app.py
   ```
