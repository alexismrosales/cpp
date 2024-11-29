class Solution(object):
    def __init__(self):
        self.letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        allCombinations = []

        def backTracking(indexDigit, actualCombination):
            if len(actualCombination) == len(digits):  # In case a word is completed
                allCombinations.append(actualCombination)
                return
            if indexDigit >= len(digits):  # If the index is bigger
                return
            digitValues = self.letters[
                int(digits[indexDigit])
            ]  # get string of chars depending of digit

            # for every character in digitValues we create a new combination with next character
            for v in digitValues:
                actualCombination += v
                backTracking(indexDigit + 1, actualCombination)
                actualCombination = actualCombination[:-1]

        backTracking(0, "")
        return allCombinations
