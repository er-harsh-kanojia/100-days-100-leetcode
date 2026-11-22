class Solution:
    def containsDuplicate(self, nums):
        # The bouncer's guest list: everything we've already let in.
        seen = set()
        for x in nums:
            if x in seen:
                return True  # "Bhai tu toh andar gaya tha!"
            seen.add(x)
        return False
