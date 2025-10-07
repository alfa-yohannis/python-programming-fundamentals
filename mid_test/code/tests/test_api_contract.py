# tests/test_api_contract.py
import importlib
import inspect


def _is_callable_attr(mod, name):
    assert hasattr(mod, name), f"Missing attribute: {mod.__name__}.{name}"
    attr = getattr(mod, name)
    assert callable(attr), f"{mod.__name__}.{name} must be callable"
    return attr


def test_main_exports_required_symbols():
    main_mod = importlib.import_module("main")

    # functions
    _is_callable_attr(main_mod, "main")

    # required student identity variables
    assert hasattr(main_mod, "STUDENT_ID"), "main.STUDENT_ID missing"
    assert hasattr(main_mod, "STUDENT_NAME"), "main.STUDENT_NAME missing"
    assert isinstance(main_mod.STUDENT_ID, str), "STUDENT_ID must be str"
    assert isinstance(main_mod.STUDENT_NAME, str), "STUDENT_NAME must be str"


def test_utils_exports_required_symbols():
    utils_mod = importlib.import_module("app.utils")
    clear_console = _is_callable_attr(utils_mod, "clear_console")

    # optional: ensure it accepts no required positional params
    sig = inspect.signature(clear_console)
    for p in sig.parameters.values():
        assert p.default is not inspect._empty, "clear_console should have no required params"


def test_exercises_exports_required_symbols():
    ex_mod = importlib.import_module("app.exercises")
    _is_callable_attr(ex_mod, "_load_flashcards")
    _is_callable_attr(ex_mod, "run_exercises")


def test_quiz_exports_required_symbols():
    quiz_mod = importlib.import_module("app.quiz")

    # core helpers
    _is_callable_attr(quiz_mod, "_load_flashcards")
    _is_callable_attr(quiz_mod, "_ensure_results_header")
    _is_callable_attr(quiz_mod, "_save_result")
    _is_callable_attr(quiz_mod, "_build_options")
    _is_callable_attr(quiz_mod, "_ask")

    # public entry
    _is_callable_attr(quiz_mod, "show_quiz")


def test_quiz_function_signatures_light_check():
    """
    Light-touch signature checks to ensure required parameters exist.
    We keep this flexible—only verify parameter names, not types/defaults.
    """
    quiz_mod = importlib.import_module("app.quiz")

    # _build_options(correct_answer, all_answers, k=3)
    sig = inspect.signature(quiz_mod._build_options)
    assert list(sig.parameters.keys())[:2] == ["correct_answer", "all_answers"]

    # _ask(q_number, total, question, options, correct_answer)
    sig_ask = inspect.signature(quiz_mod._ask)
    needed = ["q_number", "total", "question", "options", "correct_answer"]
    assert all(name in sig_ask.parameters for name in needed), "_ask missing required params"
