class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1

        while left <= right:
            mid = left + ((right - left) // 2)
            min_num, max_num = min(matrix[mid]), max(matrix[mid])

            if target in range(min_num-1, max_num+1):
                return self.binarySearch(matrix[mid], target)
            elif min_num < target: # <
                left = mid + 1
            elif min_num > target: # >
                right = mid - 1
        
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        return False
