import importlib.util
import pathlib
import random
from collections import Counter

_spec = importlib.util.spec_from_file_location("day09", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
top_k = sol.Solution().topKFrequent


def is_valid(nums, k, ans):
    """Any valid answer: k distinct numbers, and none of the left-out numbers is more frequent."""
    cnt = Counter(nums)
    if len(ans) != k or len(set(ans)) != k or any(a not in cnt for a in ans):
        return False
    weakest_in = min(cnt[a] for a in ans)
    strongest_out = max((c for x, c in cnt.items() if x not in ans), default=0)
    return weakest_in >= strongest_out


def test_leetcode_examples():
    assert sorted(top_k([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k([1], 1) == [1]
    assert sorted(top_k([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)) == [1, 2]


def test_k_equals_number_of_distinct_values():
    assert sorted(top_k([4, 4, 5, 6, 6, 6], 3)) == [4, 5, 6]


def test_negatives():
    assert top_k([-1, -1, -2, -3, -3, -3], 1) == [-3]


def test_all_same_number():
    assert top_k([7] * 1000, 1) == [7]


def test_order_is_most_frequent_first():
    assert top_k([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_large_input():
    nums = [i % 1000 for i in range(100_000)] + [42] * 50
    assert top_k(nums, 1) == [42]


def test_random_against_counter():
    rng = random.Random(9)
    for _ in range(2000):
        nums = [rng.randint(-10, 10) for _ in range(rng.randint(1, 40))]
        k = rng.randint(1, len(set(nums)))
        ans = top_k(nums, k)
        assert is_valid(nums, k, ans), (nums, k, ans)
