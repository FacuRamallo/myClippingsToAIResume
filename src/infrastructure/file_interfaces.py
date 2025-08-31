from abc import ABC, abstractmethod

class FileReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> str:
        pass

class FileWriter(ABC):
    @abstractmethod
    def write(self, file_path: str, content: str):
        pass
