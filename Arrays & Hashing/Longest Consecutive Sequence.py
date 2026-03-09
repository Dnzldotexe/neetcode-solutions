class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        nums = set(nums)
        sequences = {}

        for n in nums:
            if n-1 not in nums:
                sequences[n] = 1
        for k in sequences.keys():
            next = k+1
            while next in nums:
                sequences[k] += 1
                next += 1
        # print(sequences)
        # print(sorted(nums))
            
        return max(sequences.values())
