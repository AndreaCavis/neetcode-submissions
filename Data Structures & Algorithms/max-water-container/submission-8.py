class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n = len(heights) - 1
        max_area = 0
        l, r = 0, n

        while l < r:
            height = min(heights[l], heights[r])
            length = r - l
            curr_area = height * length
            max_area = max(curr_area, max_area)
            # I KNEW THIS WAS THE APPROACH BUT I SECOND GUESSED MYSELF
            # AND TALKED ME OUT OF IT. I NEED TO FIGURE THIS OUT
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
