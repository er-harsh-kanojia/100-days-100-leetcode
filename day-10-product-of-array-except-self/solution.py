class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        # Left wali aunties ka gossip: product of everything to the left.
        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        # Right wali aunties ka gossip: multiply in everything to the right.
        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans
