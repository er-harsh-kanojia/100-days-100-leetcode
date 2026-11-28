# Day 11/100 — Longest Consecutive Sequence

**LeetCode #128** · Medium · HashSet
Problem: https://leetcode.com/problems/longest-consecutive-sequence/

## Idea (Hinglish)
Platform pe train ke dibbe bikhre pade hain: `100, 4, 200, 1, 3, 2`. Sabse lambi train jodni hai, **bina sort kiye**, aur O(n) mein.

Sort karke ginna easy hai, par woh **O(n log n)** hai. Interviewer ko O(n) chahiye.

Trick: **sirf engine ginti shuru karega** 🚂
1. Saare dibbe ek **HashSet** mein daalo.
2. Har dibbe `x` se poocho: kya `x − 1` set mein hai?
   - Haan → `x` engine nahi hai, skip.
   - Nahi → `x` engine hai. Ab aage gino: `x + 1`, `x + 2`, … jab tak dibbe milte rahein.
3. Sabse lambi train yaad rakho.

`[100, 4, 200, 1, 3, 2]` → engine `1` → `2 ✓ 3 ✓ 4 ✓ 5 ✗` → **4**

Ginti sirf engine se shuru hoti hai, isliye har dibba sirf ek baar gina jaata hai.

## Complexity
- Time: **O(n)**
- Space: **O(n)**, HashSet ke liye

## Run the tests
```bash
python -m pytest day-11-longest-consecutive-sequence
```
