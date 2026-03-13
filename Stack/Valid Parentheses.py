class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
                ')': '(', 
                '}': '{', 
                ']': '['
                }
        open = []
        close = []

        for char in s:
            if char in pairs.values():
                open.append(char)
            elif len(open) \
               and char in pairs.keys() \
               and open[-1] == pairs[char]:
                open.pop()
            else:
                close.append(char)
        
        if len(open) or len(close):
            return False
        return True
