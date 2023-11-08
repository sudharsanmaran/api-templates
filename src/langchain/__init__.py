import os

from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path='D:/api-templates/.env')


api_key = os.environ.get("OPENAI_API_KEY")

openai_llm = OpenAI(openai_api_key=api_key, temperature=0.5)
