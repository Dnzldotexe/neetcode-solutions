class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n*k)
        count = {}
        results = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        while len(results) < k:
            for m in count:
                if count[m] == max(count.values()):
                    results.append(m)
                    count[m] = 0

        return results[:k]