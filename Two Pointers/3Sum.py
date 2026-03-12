class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # left, right = 0, len(nums)-1
        # right = len(nums)-1
        target = 0
        res = []
        # candidates = {}
        
        # increment from left to right
        for left in range(len(nums)):
            # decrement right to left
            for right in range(len(nums)-1, left, -1):
                diff = target - nums[left] - nums[right]
                if diff in nums[:left] + nums[left+1:right]:
                    res.append([nums[left], nums[right], diff])
        
        return [list(n) for n in {tuple(sorted(sums)) for sums in res}]
