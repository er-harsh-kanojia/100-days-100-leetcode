import importlib.util
import pathlib
import random
import time

_spec = importlib.util.spec_from_file_location("day11", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
longest = sol.Solution().longestConsecutive


def brute_force(nums):
    s = sorted(set(nums))
    best = run = 0
    for i, x in enumerate(s):
        run = run + 1 if i and x == s[i - 1] + 1 else 1
        best = max(best, run)
    return best


def test_leetcode_examples():
    assert longest([100, 4, 200, 1, 3, 2]) == 4
    assert longest([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest([1, 0, 1, 2]) == 3


def test_empty():
    assert longest([]) == 0


def test_single():
    assert longest([42]) == 1


def test_duplicates_do_not_extend_the_train():
    assert longest([1, 2, 2, 3]) == 3


def test_negatives():
    assert longest([-3, -1, -2, 5]) == 3


def test_large_consecutive_is_linear_time():
    nums = list(range(100_000, 0, -1))
    t = time.perf_counter()
    assert longest(nums) == 100_000
    assert time.perf_counter() - t < 2.0


def test_random_against_sorting():
    rng = random.Random(11)
    for _ in range(2000):
        nums = [rng.randint(-15, 15) for _ in range(rng.randint(0, 25))]
        assert longest(nums) == brute_force(nums), nums
