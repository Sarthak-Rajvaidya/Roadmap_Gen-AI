from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()

model = ChatOpenAI()


#schema
class Review(TypedDict):
    summary : Annotated[str,"A brif summary of review"]
    
    sentiment : Annotated[str,"Return sentiment of review either negative, positive or neutral"]
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""""")

print(result)