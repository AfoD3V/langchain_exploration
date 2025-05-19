from langchain_anthropic.chat_models import ChatAnthropic
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
chat_model = ChatAnthropic(api_key=api_key, model="claude-3-7-sonnet-20250219")

class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")
    

template = """
You're helpful assistant who generated comma separated lists.
A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more.
Outcomes have to be random.
"""
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template), 
])

# Chain -> -> ->
chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()
result = chain.invoke({"text": "minerals"})
print(result)