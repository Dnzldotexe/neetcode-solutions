class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 4 < 6
                left = mid + 1
                # mid = len(nums[left:])//2
            elif nums[mid] > target:
                # 4 > 2
                right = mid - 1
                # mid = len(nums[:right])//2
        
        return -1
