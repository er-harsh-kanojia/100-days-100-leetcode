def two_sum(nums, target):
    # Step 1: Create a hash table (dictionary in Python)
    num_to_index = {}

    # Step 2: Loop through each number in the list
    for index, num in enumerate(nums):
        # Step 3: Compute the complement
        complement = target - num

        # Step 4: Check if complement exists in the hash table
        if complement in num_to_index:
            # Step 5: If found, return indices of both numbers
            return [num_to_index[complement], index]

        # Step 6: Otherwise, store the current number and its index
        num_to_index[num] = index

    # Step 7: If no pair is found, return empty list
    return []


class Solution:
    """LeetCode signature, so you can paste this class straight into LeetCode."""

    def twoSum(self, nums, target):
        return two_sum(nums, target)
