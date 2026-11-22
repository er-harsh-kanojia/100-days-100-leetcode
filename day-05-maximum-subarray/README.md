# Day 5/100 — Maximum Subarray

**LeetCode #53** · Medium · Kadane's algorithm
Problem: https://leetcode.com/problems/maximum-subarray/

## Idea (Hinglish)
Running sum negative ho jaaye toh usse chhod do (0 se restart). Har step pe best sum update karo. Sab negative ho tab bhi sahi chalta hai kyunki max_sum nums[0] se shuru hota hai.

## Complexity
- Time: **O(n)**
- Space: **O(1)**

## Run the tests
```bash
python -m pytest day-05-maximum-subarray
```
