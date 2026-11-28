class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)  # saare dibbe platform pe
        best = 0
        for x in s:
            if x - 1 not in s:  # engine: no coach before it
                y = x
                while y + 1 in s:  # couple coaches forward
                    y += 1
                best = max(best, y - x + 1)
        return best
