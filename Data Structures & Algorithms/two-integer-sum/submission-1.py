class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        result = []

        for i in range(len(nums)):
            num = nums[i]
            difference = target - num

            if difference in seen_numbers:
                return[seen_numbers[difference], i]

            if num not in seen_numbers:
                seen_numbers[num] = i

        return []
        