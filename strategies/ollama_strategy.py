from strategies.base_strategy import LLMStrategy

class OllamaStrategy(LLMStrategy):
    def get_response(self, prompt: str) -> str:
        # Implement the Ollama API call here
        return "Response from Ollama for prompt: " + prompt
