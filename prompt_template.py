from langchain_anthropic.chat_models import ChatAnthropic
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
chat_model = ChatAnthropic(api_key=api_key, model="claude-3-7-sonnet-20250219")

template = """
You're a QA engineer. Generate a short, clear bug title from the following report description.
"""
human_template = "{description}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

messages = chat_prompt.format_messages(
    description="App crashes when clicking 'Submit' after filling the form on mobile."
)

result = chat_model.invoke(messages)
print(result.content)