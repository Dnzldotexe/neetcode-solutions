class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = left + ((right - left) // 2)

        if nums[left] <= nums[mid] <= nums[right]:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + ((right - left) // 2)

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1 # go right
                else:
                    right = mid - 1 # go left

            return -1

        else:
            left, right = 0, len(nums) - 1
            mid = self.findMin(nums)

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
