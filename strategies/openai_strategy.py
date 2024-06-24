from strategies.base_strategy import LLMStrategy
import openai
from config.config import OPENAI_API_KEY

class OpenAIStrategy(LLMStrategy):
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def get_response(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
