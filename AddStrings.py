class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        carry = 0
        res = ""
        while l1 > 0 or l2 > 0:
            a = ord(num1[l1-1]) - ord('0') if l1 > 0 else 0
            b = ord(num2[l2-1]) - ord('0') if l2 > 0 else 0
            curSum = a + b + carry
            
            carry = curSum / 10
            c = curSum % 10
            res += str(c)
            l1 -= 1
            l2 -= 1
        return '1' + res[::-1] if carry else res[::-1]

A = Solution()
print A.addStrings("1234", "8913")