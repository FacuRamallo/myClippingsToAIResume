from abc import ABC, abstractmethod
from typing import List

class LLMClient(ABC):
    """
    Abstract base class for LLM clients.
    """

    @abstractmethod
    def generate_summary(self, highlights: List[str]) -> str:
        """
        Generate a summary from a list of highlights.

        Args:
            highlights (List[str]): List of book highlights.

        Returns:
            str: Generated summary.
        """
        pass

    @abstractmethod
    def handle_rate_limit(self):
        """
        Handle API rate limits gracefully.
        """
        pass

    @abstractmethod
    def handle_errors(self, error: Exception):
        """
        Handle errors during API calls.

        Args:
            error (Exception): The exception raised during the API call.
        """
        pass
