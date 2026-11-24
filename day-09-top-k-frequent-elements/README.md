# Day 9/100 — Top K Frequent Elements

**LeetCode #347** · Medium · Bucket sort
Problem: https://leetcode.com/problems/top-k-frequent-elements/

## Idea (Hinglish)
Shaadi mein sabse zyada kaun naacha? Pehle `Counter` se har number ka count nikalo. Koi number maximum n baar aa sakta hai, toh **n + 1 baltiyaan** banao — balti `i` mein woh numbers jo exactly `i` baar aaye. Phir sabse badi balti se neeche aate jao jab tak k numbers na mil jaayein. Koi sorting nahi.

(Count karke sort karna bhi chalta hai, par woh O(n log n) hai. Heap of size k: O(n log k).)

## Complexity
- Time: **O(n)**
- Space: **O(n)**

## Run the tests
```bash
python -m pytest day-09-top-k-frequent-elements
```
