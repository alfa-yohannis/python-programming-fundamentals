# tests/test_utils.py
import importlib
import pytest

# ---------------------------------------------------------------------------
# UNIT TESTS (cross-platform, safe, no real console clearing)
# ---------------------------------------------------------------------------

class FakeOS:
    """A lightweight fake 'os' module for testing."""
    def __init__(self, name, ret_code=0):
        self.name = name
        self.ret_code = ret_code
        self.called = None

    def system(self, cmd):
        """Record command and return fake exit code."""
        self.called = cmd
        return self.ret_code


def test_clear_console_calls_correct_command(monkeypatch):
    """Ensure the correct system command ('clear' or 'cls') is called."""
    utils_mod = importlib.import_module("app.utils")

    # POSIX simulation
    fake_posix = FakeOS("posix", ret_code=0)
    monkeypatch.setattr(utils_mod, "os", fake_posix)
    result = utils_mod.clear_console()
    assert fake_posix.called == "clear"
    assert result == 0

    # Windows simulation
    fake_nt = FakeOS("nt", ret_code=0)
    monkeypatch.setattr(utils_mod, "os", fake_nt)
    result = utils_mod.clear_console()
    assert fake_nt.called == "cls"
    assert result == 0


def test_clear_console_returns_exit_code(monkeypatch):
    """Ensure the function returns whatever os.system() returns."""
    utils_mod = importlib.import_module("app.utils")

    fake = FakeOS("posix", ret_code=123)
    monkeypatch.setattr(utils_mod, "os", fake)
    result = utils_mod.clear_console()
    assert fake.called == "clear"
    assert result == 123


# ---------------------------------------------------------------------------
# MANUAL TEST (optional: run with pytest -m manual)
# ---------------------------------------------------------------------------

@pytest.mark.manual
def test_clear_console_real_execution():
    """
    Run clear_console() on the real console.
    This actually clears your terminal, so it's marked manual.
    """
    utils_mod = importlib.import_module("app.utils")
    exit_code = utils_mod.clear_console()
    assert isinstance(exit_code, int)
    # exit code is 0 on success; other codes may depend on terminal
