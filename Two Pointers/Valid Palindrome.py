class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        res = ""

        for x in s:
            if \
                ord(x) in range(48, 58) or\
                ord(x) in range(65, 91) or\
                ord(x) in range(97, 123):
                res += x
        
        return res == res[::-1]