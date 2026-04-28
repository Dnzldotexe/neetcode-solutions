class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        # pile_stack = [i for i in range(1, res+1)]
        # print(pile_stack, h)

        # left, right = 0, len(pile_stack)-1
        left, right = 1, res

        while left <= right:
            mid = left + ((right - left) // 2)

            # mid_sum = sum([math.ceil(pile / pile_stack[mid]) for pile in piles])
            mid_sum = sum([math.ceil(pile / mid) for pile in piles])

            # print(mid, pile_stack[mid], mid_sum)
            
            if mid_sum <= h:
                right = mid - 1
                # res = pile_stack[mid]
                res = mid
            else:
                left = mid + 1

        return res
