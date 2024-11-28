from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.tCharacters = defaultdict(int)

    def minWindow(self, s, t):
        # Saving characters in dict
        for c in t:
            self.tCharacters[c] += 1
        p1, p2 = 0, 0
        rest = len(t)
        minimum = float("inf")
        best = ""
        while p2 < len(s):
            if self.tCharacters[s[p2]] > 0:
                rest -= 1

            self.tCharacters[s[p2]] -= 1
            p2 += 1  # p2 advance

            while rest == 0:
                # If the substr is better
                if p2 - p1 < minimum:
                    minimum = p2 - p1
                    best = s[p1:p2]
                # Moving p1
                if self.tCharacters[s[p1]] == 0:
                    rest += 1
                self.tCharacters[p1] += 1
                p1 += 1
        return best
