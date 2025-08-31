import os
import pytest
from src.infrastructure.local_file_operations import LocalFileReader, LocalFileWriter

@pytest.fixture

def sample_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Sample content")
    return file_path

def test_local_file_reader(sample_file):
    reader = LocalFileReader()
    content = reader.read(str(sample_file))
    assert content == "Sample content"

def test_local_file_writer(tmp_path):
    writer = LocalFileWriter()
    file_path = tmp_path / "output.txt"
    writer.write(str(file_path), "Test content")
    assert file_path.read_text() == "Test content"
