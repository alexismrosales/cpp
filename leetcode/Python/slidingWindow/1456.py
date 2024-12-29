class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        maxNumber = 0
        currentVowels = 0
        for c in range(k):
            if c in vowels:
               currentVowels+=1
        maxNumber = currentVowels
        for c in range(k, len(s)):
            if s[c] in vowels:
                currentVowels += 1
            if s[c-k] in vowels:
                currentVowels -=1
            maxNumber = max(maxNumber, currentVowels)
        return maxNumber
