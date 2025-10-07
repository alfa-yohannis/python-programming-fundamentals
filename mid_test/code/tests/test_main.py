# tests/test_main.py
import builtins
import importlib
from types import SimpleNamespace
import re


def feed_inputs(monkeypatch, inputs):
    """Monkeypatch input() to yield a sequence of answers, then raise EOFError."""
    it = iter(inputs)

    def _fake_input(prompt=""):
        try:
            return next(it)
        except StopIteration:
            # Stop the loop if code asks for more inputs than provided
            raise EOFError

    monkeypatch.setattr(builtins, "input", _fake_input)


def test_menu_calls_run_exercises_once_then_exit(monkeypatch, capsys):
    """
    Flow:
      1. Choose Exercises
      2. Exit
    Expect run_exercises called exactly once.
    """
    main_mod = importlib.import_module("main")

    # Avoid clearing during quiz
    monkeypatch.setattr(main_mod, "clear_console", lambda: None, raising=False)

    # Count calls
    counters = SimpleNamespace(run_exercises=0, show_quiz=0)

    def fake_run_exercises():
        counters.run_exercises += 1  # return immediately

    def fake_show_quiz():
        counters.show_quiz += 1

    # Patch functions used inside main.py
    monkeypatch.setattr(main_mod, "run_exercises", fake_run_exercises, raising=False)
    monkeypatch.setattr(main_mod, "show_quiz", fake_show_quiz, raising=False)

    # Inputs: "1" -> Exercises, "3" -> Exit
    feed_inputs(monkeypatch, ["1", "3"])

    # Run
    main_mod.main()

    # Assertions
    assert counters.run_exercises == 1
    assert counters.show_quiz == 0

    out = capsys.readouterr().out
    assert "Flash Card App" in out
    assert "Exercises" in out
    assert "Quiz" in out
    assert "Exit" in out


def test_menu_calls_show_quiz_once_then_exit(monkeypatch, capsys):
    """
    Flow:
      1. Choose Quiz
      2. Exit
    Expect show_quiz called exactly once.
    """
    main_mod = importlib.reload(importlib.import_module("main"))
    monkeypatch.setattr(main_mod, "clear_console", lambda: None, raising=False)

    counters = SimpleNamespace(run_exercises=0, show_quiz=0)

    def fake_run_exercises():
        counters.run_exercises += 1

    def fake_show_quiz():
        counters.show_quiz += 1

    monkeypatch.setattr(main_mod, "run_exercises", fake_run_exercises, raising=False)
    monkeypatch.setattr(main_mod, "show_quiz", fake_show_quiz, raising=False)

    # Inputs: "2" -> Quiz, "3" -> Exit
    feed_inputs(monkeypatch, ["2", "3"])

    main_mod.main()

    assert counters.run_exercises == 0
    assert counters.show_quiz == 1

    out = capsys.readouterr().out
    assert "Flash Card App" in out


def test_invalid_option_then_exit(monkeypatch, capsys):
    """
    Flow:
      1. Invalid input
      2. Press Enter to continue
      3. Exit
    Expect invalid message printed once.
    """
    main_mod = importlib.reload(importlib.import_module("main"))
    monkeypatch.setattr(main_mod, "clear_console", lambda: None, raising=False)

    # Stub called functions so they don't run real UI
    monkeypatch.setattr(main_mod, "run_exercises", lambda: None, raising=False)
    monkeypatch.setattr(main_mod, "show_quiz", lambda: None, raising=False)

    # Inputs: invalid -> Enter to continue -> Exit
    feed_inputs(monkeypatch, ["x", "", "3"])

    main_mod.main()

    out = capsys.readouterr().out
    assert "Invalid option" in out


def test_exit_immediately(monkeypatch, capsys):
    """
    Flow:
      1. Exit
    Expect the program to print exit message and return.
    """
    main_mod = importlib.reload(importlib.import_module("main"))
    monkeypatch.setattr(main_mod, "clear_console", lambda: None, raising=False)

    # Inputs: "3" -> Exit
    feed_inputs(monkeypatch, ["3"])

    main_mod.main()

    out = capsys.readouterr().out
    assert "Exiting the app" in out
   

def test_student_id_format():
    main_mod = importlib.import_module("main")
    sid = getattr(main_mod, "STUDENT_ID", None)
    assert isinstance(sid, str)
    assert re.fullmatch(r"\d{8}", sid), f"Invalid STUDENT_ID '{sid}': must start with '25' and be 10 digits (e.g., 2510101075)."
    assert sid.strip() == sid, "STUDENT_ID must not have leading or trailing spaces."


def test_student_name_valid():
    main_mod = importlib.import_module("main")
    sname = getattr(main_mod, "STUDENT_NAME", None)
    assert isinstance(sname, str)
    assert len(sname.strip()) > 2, f"Invalid STUDENT_NAME '{sname}': must be longer than 2 characters."
    assert sname.strip() == sname, "STUDENT_NAME must not have leading or trailing spaces."

