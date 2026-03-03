class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        for n in range(len(nums)):
            # if nums[n] > target:
            #     continue
            diff = target - nums[n]
            if diff in nums[:n] + nums[n+1:]:
                candidates[n] = nums[n]
        return list(candidates.keys())