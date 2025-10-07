# tests/test_quiz.py
import csv
import builtins
import importlib
from pathlib import Path
import pytest


# ----------------- helpers -----------------

def write_csv(path: Path, rows, fieldnames=("id", "question", "answer")):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def feed_inputs(monkeypatch, inputs):
    """Monkeypatch input() to yield a sequence of answers, then EOFError."""
    it = iter(inputs)

    def _fake_input(_prompt=""):
        try:
            return next(it)
        except StopIteration:
            raise EOFError

    monkeypatch.setattr(builtins, "input", _fake_input)


def import_quiz_module():
    """
    Import the quiz module regardless of whether it's named app.tests or app.quiz.
    """
    try:
        return importlib.import_module("app.tests")
    except ModuleNotFoundError:
        return importlib.import_module("app.quiz")


# ----------------- module fixture -----------------

@pytest.fixture()
def temp_env(tmp_path, monkeypatch):
    """
    Prepare a temp environment and return (quiz_mod, cards_path, results_path).
    """
    cards_path = tmp_path / "data" / "flashcards" / "python.csv"
    results_path = tmp_path / "data" / "results" / "results.csv"

    # Minimal flashcards CSV
    write_csv(
        cards_path,
        rows=[
            {"id": "1", "question": "What defines a function?", "answer": "def"},
            {"id": "2", "question": "First index in list?", "answer": "0"},
            {"id": "3", "question": "Equality operator?", "answer": "=="},
            {"id": "4", "question": "Logical AND?", "answer": "and"},
            {"id": "5", "question": "No value in Python?", "answer": "None"},
        ],
    )

    quiz_mod = import_quiz_module()

    # Redirect files/constants AFTER import (no reload)
    monkeypatch.setattr(quiz_mod, "DATA_FILE", str(cards_path), raising=False)
    monkeypatch.setattr(quiz_mod, "RESULTS_FILE", str(results_path), raising=False)
    monkeypatch.setattr(quiz_mod, "NUMBER_OF_QUESTIONS", 3, raising=False)

    # Avoid clearing the console
    monkeypatch.setattr(quiz_mod, "clear_console", lambda: None, raising=False)

    # Deterministic selection/shuffle so test outputs are stable
    monkeypatch.setattr(quiz_mod.random, "sample", lambda pop, k: list(pop)[:k], raising=True)
    monkeypatch.setattr(quiz_mod.random, "shuffle", lambda x: None, raising=True)

    return quiz_mod, cards_path, results_path


# ----------------- unit tests -----------------

def test_load_flashcards(temp_env):
    quiz_mod, _, _ = temp_env
    cards = quiz_mod._load_flashcards()
    assert len(cards) == 5
    assert {"question", "answer"} <= set(cards[0].keys())
    assert any(c["answer"] == "def" for c in cards)


def test_build_options_includes_correct_and_unique(temp_env):
    quiz_mod, _, _ = temp_env
    all_answers = ["def", "0", "==", "and", "None"]
    correct = "def"
    opts = quiz_mod._build_options(correct, all_answers, k=3)

    assert len(opts) == 3
    assert correct in opts
    assert len(set(opts)) == 3
    for o in opts:
        assert o in all_answers


@pytest.mark.parametrize("k", [3, 3])
def test_build_options_handles_small_pools(temp_env, k):
    quiz_mod, _, _ = temp_env
    # Tiny pool still yields k options (duplicates allowed as last resort)
    all_answers = ["only_one"]
    opts = quiz_mod._build_options("only_one", all_answers, k=k)
    assert len(opts) == k
    assert "only_one" in opts


def test_save_result_creates_and_appends(temp_env):
    quiz_mod, _, results_path = temp_env

    # First write
    quiz_mod._save_result(total=3, correct=2)
    assert results_path.exists()
    with results_path.open("r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows[0] == ["timestamp", "total_questions", "correct", "percentage"]
    assert rows[1][1:] == ["3", "2", "66.67"]

    # Second write
    quiz_mod._save_result(total=3, correct=3)
    with results_path.open("r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert len(rows) == 3
    assert rows[2][1:] == ["3", "3", "100.0"]


# ----------------- interaction tests for show_quiz -----------------

def test_show_quiz_no_cards_prints_message_and_returns(monkeypatch, capsys, tmp_path):
    quiz_mod = import_quiz_module()

    # Point DATA_FILE to a non-existent path in tmp
    cards_path = tmp_path / "data" / "flashcards" / "python.csv"
    results_path = tmp_path / "data" / "results" / "results.csv"
    # Ensure parent exists but file doesn't
    cards_path.parent.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(quiz_mod, "DATA_FILE", str(cards_path), raising=False)
    monkeypatch.setattr(quiz_mod, "RESULTS_FILE", str(results_path), raising=False)
    monkeypatch.setattr(quiz_mod, "clear_console", lambda: None, raising=False)

    # Press Enter to go back...
    feed_inputs(monkeypatch, [""])

    quiz_mod.show_quiz()
    out = capsys.readouterr().out
    assert "No flashcards found." in out
    assert "Expected file:" in out


def test_show_quiz_runs_and_saves_results(monkeypatch, capsys, temp_env):
    quiz_mod, cards_path, results_path = temp_env

    # Make a controlled set of 3 cards for NUMBER_OF_QUESTIONS=3
    write_csv(
        Path(cards_path),
        rows=[
            {"id": "1", "question": "Q1?", "answer": "A1"},
            {"id": "2", "question": "Q2?", "answer": "A2"},
            {"id": "3", "question": "Q3?", "answer": "A3"},
        ],
    )

    # Simulate three question outcomes: True, False, True
    outcomes = iter([True, False, True])
    monkeypatch.setattr(quiz_mod, "_ask", lambda *args, **kwargs: next(outcomes))

    # Final "Press Enter to return..."
    feed_inputs(monkeypatch, [""])

    quiz_mod.show_quiz()

    out = capsys.readouterr().out
    assert "Test Summary" in out
    assert "Questions answered : 3" in out
    assert "Correct answers    : 2" in out
    assert "Score              : 66.67%" in out

    assert Path(results_path).exists()
    with Path(results_path).open("r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert len(rows) == 2
    assert rows[1][1:] == ["3", "2", "66.67"]


def test_show_quiz_quit_early_does_not_save(monkeypatch, capsys, temp_env):
    quiz_mod, cards_path, results_path = temp_env

    # Provide at least one card
    write_csv(
        Path(cards_path),
        rows=[{"id": "1", "question": "Q1?", "answer": "A1"}],
    )

    # User quits immediately
    monkeypatch.setattr(quiz_mod, "_ask", lambda *args, **kwargs: None)

    # Defensive input in case of prompts
    feed_inputs(monkeypatch, [""])

    quiz_mod.show_quiz()
    out = capsys.readouterr().out
    assert "Test canceled." in out
    assert not Path(results_path).exists()
