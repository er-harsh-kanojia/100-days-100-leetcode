import importlib.util
import pathlib
import random

_spec = importlib.util.spec_from_file_location("day04", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
max_profit = sol.Solution().maxProfit


def brute_force(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


def test_leetcode_examples():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_single_day_cannot_trade():
    assert max_profit([5]) == 0


def test_flat_prices():
    assert max_profit([3, 3, 3, 3]) == 0


def test_must_buy_before_selling():
    # the lowest price comes after the highest one
    assert max_profit([9, 2, 4, 1]) == 2


def test_new_minimum_later_gives_better_profit():
    assert max_profit([3, 8, 1, 10]) == 9


def test_returns_int():
    assert isinstance(max_profit([1, 2]), int)


def test_large_input():
    prices = list(range(100_000, 0, -1))  # strictly falling
    assert max_profit(prices) == 0
    assert max_profit(prices[::-1]) == 99_999


def test_random_against_brute_force():
    rng = random.Random(4)
    for _ in range(2000):
        prices = [rng.randint(0, 10_000) for _ in range(rng.randint(1, 40))]
        assert max_profit(prices) == brute_force(prices), prices
