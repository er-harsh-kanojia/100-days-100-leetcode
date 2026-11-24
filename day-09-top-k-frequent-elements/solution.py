from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        # Count how many times each number "danced".
        count = Counter(nums)
        # Baltiyaan: bucket i holds the numbers that appeared exactly i times (max n).
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            buckets[c].append(num)
        # Walk from the biggest bucket down until we have k numbers.
        res = []
        for c in range(len(nums), 0, -1):
            for num in buckets[c]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
