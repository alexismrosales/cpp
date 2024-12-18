from typing import List


class Solution:
    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        # Case of one element
        if len(wordList) == 1:
            if s in wordList:
                return True
            else:
                return False

        wordDict = {}
        # Save elements on dict to future searches
        for w in wordList:
            wordDict[w] = None

        # Initialize pointers
        i = 0
        j = 1
        partitionedSubstring = ""
        while j <= len(s):
            partitionedSubstring = s[i:j]
            print(s[i:j])
            if partitionedSubstring in wordDict:
                i = j
                j = i
            else:
                j+= 1

        if partitionedSubstring in wordDict:
            return True
        return False
