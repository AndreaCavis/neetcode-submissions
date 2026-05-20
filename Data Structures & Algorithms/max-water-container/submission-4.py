# NOTE: Naive solution, needs refactoring

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n = len(heights) - 1
        max_area = 0

        for l in range(n):
            r = n
            while l < r:
                height = min(heights[l], heights[r])
                length = r - l
                curr_area = height * length
                max_area = max(curr_area, max_area)
                r -= 1

        return max_area