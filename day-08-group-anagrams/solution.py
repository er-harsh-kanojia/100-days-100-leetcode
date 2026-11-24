from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        # Shaadi ka seating plan: family surname -> table of guests.
        groups = defaultdict(list)
        for w in strs:
            # Surname = the 26 dabbe (letter counts), no sorting needed.
            count = [0] * 26
            for ch in w:
                count[ord(ch) - 97] += 1
            groups[tuple(count)].append(w)
        return list(groups.values())
