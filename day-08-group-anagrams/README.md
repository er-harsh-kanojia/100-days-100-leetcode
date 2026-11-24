# Day 8/100 — Group Anagrams

**LeetCode #49** · Medium · Hash map · counting
Problem: https://leetcode.com/problems/group-anagrams/

## Idea (Hinglish)
Shaadi ka seating plan: har word ek guest hai, aur anagrams ek hi family. Family ka "surname" = 26 dabbe (har letter ka count) ka tuple. HashMap mein surname → table; har word ko uske surname wali table pe bitha do. Sort karne ki zaroorat hi nahi.

(Sorted letters ko key banana bhi chalta hai — `"".join(sorted(w))` — par woh O(n · k log k) hai.)

## Complexity
- Time: **O(n · k)** — n words, k = longest word ki length
- Space: **O(n · k)**

## Run the tests
```bash
python -m pytest day-08-group-anagrams
```
