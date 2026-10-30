from langchain_openai import ChatOpeanAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt = PromptTemplate(
    template = 'Generate 5 intresting facts about {topic}',
    input_variables=['topic']
)