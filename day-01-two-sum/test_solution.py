import importlib.util
import pathlib
import random

_spec = importlib.util.spec_from_file_location("day01", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
two_sum = sol.two_sum


def is_valid_answer(nums, target, ans):
    return len(ans) == 2 and ans[0] != ans[1] and nums[ans[0]] + nums[ans[1]] == target


def test_leetcode_examples():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


def test_does_not_use_same_element_twice():
    # 3 + 3 = 6, but there is only one 3
    assert two_sum([3, 2, 5], 6) == []
    assert sorted(two_sum([1, 3, 4, 2], 6)) == [2, 3]


def test_negatives_and_zero():
    assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4]
    assert sorted(two_sum([0, 4, 3, 0], 0)) == [0, 3]
    assert sorted(two_sum([-3, 4, 3, 90], 0)) == [0, 2]


def test_large_values():
    assert sorted(two_sum([10**9, -(10**9), 5], 0)) == [0, 1]


def test_no_pair_returns_empty():
    assert two_sum([1, 2, 3], 100) == []
    assert two_sum([], 5) == []
    assert two_sum([5], 10) == []


def test_leetcode_class_wrapper():
    assert sorted(sol.Solution().twoSum([2, 7, 11, 15], 9)) == [0, 1]


def test_random_against_brute_force():
    rng = random.Random(6)
    for _ in range(2000):
        nums = [rng.randint(-50, 50) for _ in range(rng.randint(0, 30))]
        target = rng.randint(-100, 100)
        exists = any(nums[i] + nums[j] == target for i in range(len(nums)) for j in range(i + 1, len(nums)))
        ans = two_sum(nums, target)
        if exists:
            assert is_valid_answer(nums, target, ans), (nums, target, ans)
        else:
            assert ans == []
