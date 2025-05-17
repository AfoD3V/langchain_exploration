from langchain_anthropic.chat_models import ChatAnthropic
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("API_KEY")
chat_model = ChatAnthropic(api_key=api_key, model_name='claude-3-haiku-20240307')

result = chat_model.predict("Write haiku about AI and tech in polish")
print(result)