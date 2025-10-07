import os
import pytest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

EXPECTED_STRUCTURE = {
    "app": [
        "utils.py",
        "quiz.py",
        "exercises.py",
    ],
    "data": [
        os.path.join("flashcards", "python.csv"),
        os.path.join("results", ""),  # directory should exist
    ],
    "tests": [
        "test_main.py",
        "test_quiz.py",
        "test_utils.py",
    ],
    "main.py": None,
}


def test_project_structure_exists():
    for key, items in EXPECTED_STRUCTURE.items():
        path = os.path.join(BASE_DIR, key)
        if items is None:
            assert os.path.exists(path), f"Missing file: {key}"
            continue

        assert os.path.exists(path), f"Missing directory: {key}"
        assert os.path.isdir(path), f"Expected directory but found file: {key}"

        for item in items:
            full_path = os.path.join(path, item)
            if item.endswith("/"):  # directory check
                assert os.path.isdir(full_path), f"Missing directory: {full_path}"
            else:
                assert os.path.isfile(full_path), f"Missing file: {full_path}"


def test_data_directories_writable(tmp_path):
    data_dir = os.path.join(BASE_DIR, "data", "results")
    assert os.access(data_dir, os.W_OK), f"Directory not writable: {data_dir}"
