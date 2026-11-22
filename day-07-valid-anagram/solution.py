class Solution:
    def isAnagram(self, s, t):
        # Bouncer check: different length can never be an anagram.
        if len(s) != len(t):
            return False
        # Mummy ka hisaab: 26 dabbe, one per lowercase letter.
        count = [0] * 26
        for a, b in zip(s, t):
            count[ord(a) - 97] += 1  # mummy ki list -> +1
            count[ord(b) - 97] -= 1  # dukaan ka bill -> -1
        return all(c == 0 for c in count)
