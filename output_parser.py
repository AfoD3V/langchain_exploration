from langchain_anthropic.chat_models import ChatAnthropic
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
chat_model = ChatAnthropic(api_key=api_key, model="claude-3-7-sonnet-20250219")

class AnswerOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split("answer =")
    

template = """
You are helpfull assistant that solves math problems and shows your work.
Output each step then return the answer in the following format: answer = <answer here>.
Make sure to output answer in all lowercases and to have exactly one space and one equal sign following it.
"""
human_template = "{problem}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template), 
])

messages = chat_prompt.format_messages(problem="2x^2 - 5x + 3 = 0")
result = chat_model.invoke(messages)
parsed = AnswerOutputParser().parse(str(result.content))
steps, answer = parsed
print(answer)
print(steps)