# tests/test_exercises.py
import csv
import builtins
import importlib
from pathlib import Path

import pytest


def write_csv(path: Path, rows, fieldnames=("id", "question", "answer")):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def feed_inputs(monkeypatch, inputs):
    """Monkeypatch input() to yield a sequence of answers, then raise EOFError to stop loops."""
    it = iter(inputs)

    def _fake_input(prompt=""):
        try:
            return next(it)
        except StopIteration:
            # Stop any further reads (prevents infinite loops in tests)
            raise EOFError

    monkeypatch.setattr(builtins, "input", _fake_input)


@pytest.fixture()
def mod(tmp_path, monkeypatch):
    """
    Import app.exercises and point its DATA_FILE to a temp CSV location.
    Also neutralize clear_console and random.shuffle for deterministic behavior.
    """
    ex_mod = importlib.import_module("app.exercises")

    # Point to a per-test CSV path
    data_file = tmp_path / "data" / "flashcards" / "python.csv"
    monkeypatch.setattr(ex_mod, "DATA_FILE", str(data_file), raising=False)

    # Avoid terminal clearing during tests
    monkeypatch.setattr(ex_mod, "clear_console", lambda: None, raising=False)

    # Make random.shuffle deterministic (no-op)
    def no_shuffle(x):
        # leave the list order as-is
        return None

    monkeypatch.setattr(ex_mod.random, "shuffle", no_shuffle, raising=True)

    return ex_mod, data_file


def test_load_flashcards_reads_rows(mod):
    ex_mod, data_file = mod
    write_csv(
        Path(data_file),
        rows=[
            {"id": "1", "question": "What defines a function?", "answer": "def"},
            {"id": "2", "question": "First index in list?", "answer": "0"},
            {"id": "3", "question": "Equality operator?", "answer": "=="},
        ],
    )

    cards = ex_mod._load_flashcards()
    assert len(cards) == 3
    assert {"question", "answer"} <= set(cards[0].keys())
    assert any(c["answer"] == "def" for c in cards)


def test_run_exercises_no_cards_prints_message_and_returns(monkeypatch, capsys, mod):
    ex_mod, data_file = mod
    # Ensure file doesn't exist
    if Path(data_file).exists():
        Path(data_file).unlink()

    # The function will ask for "Press Enter to go back..."
    feed_inputs(monkeypatch, [""])

    ex_mod.run_exercises()
    out = capsys.readouterr().out
    # Check substring that is independent of emojis
    assert "No flashcards found." in out
    assert "Expected:" in out


def test_run_exercises_show_next_back_flow(monkeypatch, capsys, mod):
    ex_mod, data_file = mod
    # Prepare 2 questions
    write_csv(
        Path(data_file),
        rows=[
            {"id": "1", "question": "Q1?", "answer": "A1"},
            {"id": "2", "question": "Q2?", "answer": "A2"},
        ],
    )

    # Inputs: show (toggle answer) -> next -> back (return)
    feed_inputs(monkeypatch, ["s", "n", "b"])

    ex_mod.run_exercises()
    out = capsys.readouterr().out

    # It should have shown Q1 (hidden), then after 's' the answer appears, then go to Q2
    assert "Q: Q1?" in out
    assert "A: (hidden)" in out
    assert "A: A1" in out
    assert "Q: Q2?" in out
    # Menu text presence
    assert "[S] Show/Hide   [N] Next   [B] Back" in out


def test_run_exercises_invalid_then_back(monkeypatch, capsys, mod):
    ex_mod, data_file = mod
    write_csv(
        Path(data_file),
        rows=[
            {"id": "1", "question": "Q1?", "answer": "A1"},
        ],
    )

    # invalid input -> press Enter to continue -> back
    feed_inputs(monkeypatch, ["x", "", "b"])

    ex_mod.run_exercises()
    out = capsys.readouterr().out
    # Ensure the invalid path was exercised
    assert "Invalid option." in out
    # And the prompt/menu was shown
    assert "[S] Show/Hide   [N] Next   [B] Back" in out
