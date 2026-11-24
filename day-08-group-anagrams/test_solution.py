import importlib.util
import pathlib
import random
from collections import defaultdict

_spec = importlib.util.spec_from_file_location("day08", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
group_anagrams = sol.Solution().groupAnagrams


def normalise(groups):
    # order of groups and of words inside a group doesn't matter on LeetCode
    return sorted(sorted(g) for g in groups)


def brute_force(strs):
    by_sorted = defaultdict(list)
    for w in strs:
        by_sorted["".join(sorted(w))].append(w)
    return list(by_sorted.values())


def test_leetcode_examples():
    assert normalise(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == normalise(
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
    assert normalise(group_anagrams([""])) == [[""]]
    assert normalise(group_anagrams(["a"])) == [["a"]]


def test_empty_strings_group_together():
    assert normalise(group_anagrams(["", "", "a"])) == normalise([["", ""], ["a"]])


def test_duplicates_stay_in_same_group():
    assert normalise(group_anagrams(["abc", "abc", "cba"])) == [["abc", "abc", "cba"]]


def test_same_letters_different_counts_are_different_families():
    assert normalise(group_anagrams(["aab", "abb", "bba", "baa"])) == normalise([["aab", "baa"], ["abb", "bba"]])


def test_every_word_alone():
    words = ["abc", "abd", "abe"]
    assert normalise(group_anagrams(words)) == normalise([[w] for w in words])


def test_large_input():
    words = ["".join(random.Random(i).sample("abcdefghij", 10)) for i in range(10_000)]
    out = group_anagrams(words)
    assert len(out) == 1 and len(out[0]) == 10_000


def test_random_against_sorted_key():
    rng = random.Random(8)
    for _ in range(1000):
        strs = ["".join(rng.choice("abc") for _ in range(rng.randint(0, 4))) for _ in range(rng.randint(1, 15))]
        assert normalise(group_anagrams(strs)) == normalise(brute_force(strs)), strs
