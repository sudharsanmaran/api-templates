import os

from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ["OPENAI_API_KEY"]

openai_llm = OpenAI(openai_api_key=api_key, temperature=0.5)
