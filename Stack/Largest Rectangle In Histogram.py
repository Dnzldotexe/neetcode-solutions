class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = []
        counter = 0
        n = 0
        nums = set(heights)
        # res.append(max(heights))

        for num in nums:
            while n < len(heights):
                if heights[n] < num:
                    if counter:
                        res.append(counter*num)
                    counter = 0
                if heights[n] >= num:
                    counter += 1
                n += 1
            if counter:
                res.append(counter*num)
            counter = 0
            n = 0

        return max(res)
