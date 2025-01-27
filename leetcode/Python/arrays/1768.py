class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        mergedString = ""
        isWord1 = True
        while i < len(word1) and j < len(word2):
            if isWord1:
                mergedString += word1[i]
                i+=1
                isWord1 = False
            else:
                mergedString += word2[i]
                j+=1
                isWord1 = True
        while i < len(word1):
            mergedString+=word1[i]
            i+=1
        while j < len(word2):
            mergedString += word2[i]
            j+=1
        return mergedString

