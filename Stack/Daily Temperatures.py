class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for n in range(len(temperatures)-1, -1, -1):
            stack.append(temperatures[n])
            for m in range(len(stack)-1, -1, -1):
                if stack[m] > temperatures[n]:
                    res[n] = len(stack)-1-m
                    break
                elif stack[m] < temperatures[n]:
                    continue
        
        return res
