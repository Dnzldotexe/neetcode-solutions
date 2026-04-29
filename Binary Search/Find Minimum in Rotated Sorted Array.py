class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        res = 1000

        while left <= right:
            mid = left + ((right - left) // 2)
            diff_l_m = nums[left] - nums[mid]
            diff_m_r = nums[mid] - nums[right]
            
            print(nums[mid], diff_l_m, diff_m_r)
            if nums[mid] < res:
                res = nums[mid]
            if diff_l_m >= diff_m_r:
                right = mid - 1
            else:
                left = mid + 1

        return res


# # nums = [x for x in range(0, 10)]
# # nums = [x for x in range(0, 50, 5)]
# nums = [4,5,6,7]

# for i in range(0, len(nums)+1):
#     s = nums[i:len(nums)] + nums[:i]
#     mid = (len(s)-1)//2
#     # sum_l_m = sum(s[0:mid])
#     # sum_m_r = sum(s[mid:-1])
#     diff_l_m = s[0] - s[mid]
#     diff_m_r = s[mid] - s[-1]
    
#     print(f"left: {s[0]}, mid: {s[mid]}, right: {s[-1]}, l_m: {diff_l_m}, m_r: {diff_m_r}")
