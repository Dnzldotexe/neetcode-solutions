class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        res = 5000

        while left <= right:
            mid = left + ((right - left) // 2)
            diff_l_m = nums[left] - nums[mid]
            diff_m_r = nums[mid] - nums[right]
            
            if nums[mid] < res:
                res = nums[mid]
            if (diff_l_m + diff_m_r) < 0 or diff_l_m >= diff_m_r:
                right = mid - 1
            else:
                left = mid + 1

        return res
