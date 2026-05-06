class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        min_num = self.findMin(nums)

        if nums[left] == nums[min_num]:
            mid = left + ((right - left) // 2)
        else:
            mid = min_num

        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] <= target <= nums[right]:
                left = mid + 1 # go right
                print("right")
            else:
                right = mid - 1 # go left
                print("left")
            mid = left + ((right - left) // 2)

        return -1

    
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return l
