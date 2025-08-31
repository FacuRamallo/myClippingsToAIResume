from abc import ABC, abstractmethod

class FileReader(ABC):
    """
    Abstract base class for reading files.
    """

    @abstractmethod
    def read(self, file_path: str) -> str:
        pass

class FileWriter(ABC):
    """
    Abstract base class for writing files.
    """

    @abstractmethod
    def write(self, file_path: str, content: str):
        pass
