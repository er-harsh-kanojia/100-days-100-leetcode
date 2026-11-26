import importlib.util
import math
import pathlib
import random

_spec = importlib.util.spec_from_file_location("day10", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
product_except_self = sol.Solution().productExceptSelf


def brute_force(nums):
    return [math.prod(nums[:i] + nums[i + 1 :]) for i in range(len(nums))]


def test_leetcode_examples():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_elements():
    assert product_except_self([5, 7]) == [7, 5]


def test_single_zero():
    assert product_except_self([2, 0, 4]) == [0, 8, 0]


def test_two_zeros_make_everything_zero():
    assert product_except_self([0, 3, 0, 5]) == [0, 0, 0, 0]


def test_negatives():
    assert product_except_self([-2, -3, 4]) == [-12, -8, 6]


def test_large_input_of_ones():
    nums = [1] * 100_000
    assert product_except_self(nums) == nums


def test_random_against_brute_force():
    rng = random.Random(10)
    for _ in range(2000):
        nums = [rng.randint(-5, 5) for _ in range(rng.randint(2, 12))]
        assert product_except_self(nums) == brute_force(nums), nums
