import importlib.util
import pathlib
import random

_spec = importlib.util.spec_from_file_location("day06", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
contains_duplicate = sol.Solution().containsDuplicate


def test_leetcode_examples():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_video_example():
    assert contains_duplicate([3, 1, 4, 2, 1]) is True


def test_single_element():
    assert contains_duplicate([7]) is False


def test_negatives_and_zero():
    assert contains_duplicate([0, -1, 1, -0]) is True  # 0 == -0
    assert contains_duplicate([-1, -2, -3]) is False


def test_large_values():
    assert contains_duplicate([10**9, -(10**9), 10**9]) is True


def test_large_input_unique():
    assert contains_duplicate(list(range(100_000))) is False


def test_large_input_duplicate_at_the_end():
    assert contains_duplicate(list(range(100_000)) + [99_999]) is True


def test_random_against_set_size():
    rng = random.Random(6)
    for _ in range(2000):
        nums = [rng.randint(-20, 20) for _ in range(rng.randint(1, 25))]
        assert contains_duplicate(nums) == (len(set(nums)) != len(nums)), nums
