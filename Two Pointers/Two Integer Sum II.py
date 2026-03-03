class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            for k in range(n, len(numbers)):
                if numbers[n] + numbers[k] == target:
                    return [n+1, k+1]