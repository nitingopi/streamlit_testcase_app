from strategies.base_strategy import LLMStrategy
import google.generativeai as genai
from config.config import GEMINI_API_KEY

class GeminiStrategy(LLMStrategy):
    def __init__(self) -> None:
        genai.configure(api_key=GEMINI_API_KEY)


    def get_response(self, prompt: str) -> str:
        # Implement the Gemini API call here
        model = genai.GenerativeModel("gemini-pro")
        config = {
        "temperature": 0,
        "top_p": 1
        }
        output = model.generate_content(prompt, generation_config=config )
        return output
