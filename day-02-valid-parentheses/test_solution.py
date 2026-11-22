import importlib.util
import itertools
import pathlib
import random

_spec = importlib.util.spec_from_file_location("day02", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
is_valid = sol.Solution().isValid


def brute_force(s):
    # keep deleting adjacent matching pairs; valid strings shrink to ""
    prev = None
    while prev != s:
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""


def test_leetcode_examples():
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([])") is True
    assert is_valid("([)]") is False


def test_nesting():
    assert is_valid("{[()()]}") is True
    assert is_valid("((((((()))))))") is True
    assert is_valid("{[(])}") is False


def test_odd_length_rejected_early():
    assert is_valid("(") is False
    assert is_valid("(()") is False


def test_starts_with_closer():
    assert is_valid(")(") is False
    assert is_valid("]") is False
    assert is_valid("}{") is False


def test_unclosed_openers():
    assert is_valid("((") is False
    assert is_valid("[{") is False


def test_every_string_up_to_length_8():
    for n in range(0, 9):
        for chars in itertools.product("()[]{}", repeat=n):
            s = "".join(chars)
            assert is_valid(s) == brute_force(s), s


def test_random_long_strings():
    rng = random.Random(2)
    for _ in range(500):
        s = "".join(rng.choice("()[]{}") for _ in range(rng.randint(0, 40)))
        assert is_valid(s) == brute_force(s), s


def test_long_valid_input():
    s = "([{" * 3000 + "}])" * 3000
    assert is_valid(s) is True
