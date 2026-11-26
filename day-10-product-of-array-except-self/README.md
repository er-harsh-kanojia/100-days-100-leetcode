# Day 10/100 — Product of Array Except Self

**LeetCode #238** · Medium · Prefix / suffix products
Problem: https://leetcode.com/problems/product-of-array-except-self/

## Idea (Hinglish)
Mohalle ki har aunty ko sabka gossip pata hota hai, bas khud ka nahi. Har position pe chahiye **baaki sabka product**, aur division use karna **mana** hai (waise bhi array mein 0 aaya toh divide karte hi sab barbaad).

Gossip do taraf se aata hai:
1. **Left se right** chalo: `ans[i]` mein rakho uske left walon ka product.
2. **Right se left** chalo: ek variable `right` mein right walon ka product leke chalo, aur `ans[i]` ko usse multiply kar do.

`[1, 2, 3, 4]` → left `[1, 1, 2, 6]` × right `[24, 12, 4, 1]` = **`[24, 12, 8, 6]`**

## Complexity
- Time: **O(n)**, do passes
- Extra space: **O(1)** (output array ko count nahi karte)

## Run the tests
```bash
python -m pytest day-10-product-of-array-except-self
```
