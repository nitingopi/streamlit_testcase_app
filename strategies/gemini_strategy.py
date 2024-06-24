from strategies.base_strategy import LLMStrategy

class GeminiStrategy(LLMStrategy):
    def get_response(self, prompt: str) -> str:
        # Implement the Gemini API call here
        return "Response from Gemini for prompt: " + prompt
