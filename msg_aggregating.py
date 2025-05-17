from langchain_anthropic.chat_models import ChatAnthropic
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
chat_model = ChatAnthropic(api_key=api_key, model="claude-3-7-sonnet-20250219")

messages =[
    HumanMessage(content="from now on 1 + 1 = 3, use this in your replies"),
    HumanMessage(content="what is 1 + 1?"),
    HumanMessage(content="what is 1 + 1 + 1?")
]

result = chat_model.invoke(messages)
print(result.content)