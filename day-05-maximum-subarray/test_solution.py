import importlib.util
import pathlib
import random

_spec = importlib.util.spec_from_file_location("day05", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
max_sub_array = sol.Solution().maxSubArray


def brute_force(nums):
    return max(sum(nums[i:j]) for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))


def test_leetcode_examples():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23


def test_all_negative_picks_the_largest_single_number():
    assert max_sub_array([-3, -1, -2]) == -1
    assert max_sub_array([-5]) == -5


def test_zeros():
    assert max_sub_array([0, 0, 0]) == 0
    assert max_sub_array([-1, 0, -2]) == 0


def test_whole_array_is_best():
    assert max_sub_array([2, 3, 4]) == 9


def test_large_input():
    nums = [10_000] * 100_000
    assert max_sub_array(nums) == 10_000 * 100_000


def test_random_against_brute_force():
    rng = random.Random(5)
    for _ in range(2000):
        nums = [rng.randint(-100, 100) for _ in range(rng.randint(1, 30))]
        assert max_sub_array(nums) == brute_force(nums), nums
