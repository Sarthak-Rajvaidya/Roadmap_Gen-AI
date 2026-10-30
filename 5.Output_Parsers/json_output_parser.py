from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = ChatOpenAI(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
    
)

model = ChatOpenAI(llm =llm)

template = PromptTemplate(
    template='Give me the name , age and city of the frictional person \n {format_instruction}',
    partial_variables={'format_instruction'}
)