from openai import OpenAI
from utils.config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

class BaseAgent:
    def __init__(self, memory):
        self.memory = memory

    def think(self, user_input):
        self.memory.add_message("user", user_input)

        messages = self.memory.get_history()

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )

        assistant_reply = response.choices[0].message.content
        self.memory.add_message("assistant", assistant_reply)

        return assistant_reply
