class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort the list to operate with 2 pointers algorithm
        sorted_nums = sorted(nums)
        n = len(sorted_nums) - 1
        result_set = set()

        for j in range(1, n):
            # reset pointers for each j iteration
            i, k = 0, n

            while i < j and j < k:
                temp_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if temp_sum < 0:
                    i += 1
                elif temp_sum > 0:
                    k -= 1
                elif temp_sum == 0:
                    result_set.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    i += 1
                    k -= 1
                
        # DATA formatting
        temp_res = [x for x in result_set]
        res = []
        for triplet in temp_res:
            res.append([num for num in triplet])

        return res
