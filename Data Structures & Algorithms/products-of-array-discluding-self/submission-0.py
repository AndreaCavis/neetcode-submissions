class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        # lists of len(nums) filled with 1 placeholders
        prefix, suffix = [1] * n, [1] * n
        prod_left, prod_right = 1, 1

        while l < n or r >= 0:
            # assigning values to indices before multiplication excludes current i
            prefix[l] = prod_left
            suffix[r] = prod_right
            # perform multiplication for next round of indices
            prod_left *= nums[l]
            prod_right *= nums[r]
            l += 1
            r -= 1

        res = []
        # fill res with the multiplications using prefix and suffix
        for i in range(n):
            res += [prefix[i] * suffix[i]]

        return res
        