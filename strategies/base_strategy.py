from abc import ABC, abstractmethod

class LLMStrategy(ABC):
    @abstractmethod
    def get_response(self, prompt: str) -> str:
        pass
