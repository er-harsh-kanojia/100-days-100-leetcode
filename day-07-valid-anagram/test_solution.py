import importlib.util
import pathlib
import random
import string

_spec = importlib.util.spec_from_file_location("day07", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
is_anagram = sol.Solution().isAnagram


def test_leetcode_examples():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False


def test_video_examples():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("dormitory", "dirtyroom") is True
    assert is_anagram("abc", "abcd") is False


def test_same_letters_different_counts():
    assert is_anagram("aab", "abb") is False
    assert is_anagram("aabb", "abab") is True


def test_single_letters():
    assert is_anagram("a", "a") is True
    assert is_anagram("a", "b") is False


def test_every_letter():
    s = string.ascii_lowercase
    assert is_anagram(s, s[::-1]) is True


def test_large_input():
    s = "abcdefghijklmnopqrstuvwxyz" * 2000  # 52,000 letters
    t = "".join(reversed(s))
    assert is_anagram(s, t) is True
    # swap the last letter of t for a different one -> counts no longer match
    broken = t[:-1] + ("b" if t[-1] != "b" else "c")
    assert is_anagram(s, broken) is False


def test_random_against_sorting():
    rng = random.Random(7)
    for _ in range(3000):
        s = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 12)))
        if rng.random() < 0.5:
            t = "".join(rng.sample(s, len(s)))  # a real shuffle
        else:
            t = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 12)))
        assert is_anagram(s, t) == (sorted(s) == sorted(t)), (s, t)
