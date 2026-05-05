class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = set()
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        sorted_seen = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        res = [num[0] for num in sorted_seen]
        return res[:k]

        