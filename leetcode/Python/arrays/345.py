from typing import List



class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        reverseVowels = []
        newS = ""
        i = len(s)-1
        while i >= 0:
            if s[i] in vowels:
                reverseVowels.append(s[i])
            i-=1

        vowelsIndex = 0
        for i in range(0, len(s)):
            if s[i] in vowels:
                newS += reverseVowels[vowelsIndex]
                vowelsIndex+=1
            else:
                newS += s[i]
        return newS
