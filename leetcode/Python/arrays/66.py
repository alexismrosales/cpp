class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strNumber = ""
        for d in digits:
            strNumber += str(d)
        intNumber = int(strNumber) + 1
        return [int(ch) for ch in str(intNumber)]
        

        
