import importlib.util
import pathlib
import random

_spec = importlib.util.spec_from_file_location("day03", pathlib.Path(__file__).with_name("solution.py"))
sol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sol)
ListNode = sol.ListNode
merge = sol.Solution().mergeTwoLists


def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def test_leetcode_examples():
    assert to_list(merge(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(merge(build([]), build([]))) == []
    assert to_list(merge(build([]), build([0]))) == [0]


def test_one_side_empty():
    assert to_list(merge(build([1, 2, 3]), None)) == [1, 2, 3]
    assert to_list(merge(None, build([5]))) == [5]


def test_one_list_entirely_before_the_other():
    assert to_list(merge(build([1, 2]), build([3, 4, 5]))) == [1, 2, 3, 4, 5]
    assert to_list(merge(build([7, 8, 9]), build([1, 2]))) == [1, 2, 7, 8, 9]


def test_negatives_and_duplicates():
    assert to_list(merge(build([-100, -1, 0, 0]), build([-50, 0, 100]))) == [-100, -50, -1, 0, 0, 0, 100]


def test_reuses_original_nodes():
    a, b = build([1, 3]), build([2])
    nodes = {id(a), id(a.next), id(b)}
    merged = merge(a, b)
    seen = set()
    while merged:
        seen.add(id(merged))
        merged = merged.next
    assert seen == nodes


def test_random_against_sorted():
    rng = random.Random(3)
    for _ in range(1000):
        x = sorted(rng.randint(-100, 100) for _ in range(rng.randint(0, 50)))
        y = sorted(rng.randint(-100, 100) for _ in range(rng.randint(0, 50)))
        assert to_list(merge(build(x), build(y))) == sorted(x + y)
