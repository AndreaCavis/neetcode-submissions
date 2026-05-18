class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # numbers is sorted in increasing order (non decreasing).
        index1, index2= 0, len(numbers) - 1

        while index1 < index2:
            # ascending order, therefore num_right = small, num_left = big
            num_right, num_left = numbers[index1], numbers[index2]
            temp_sum = num_right + num_left

            if temp_sum == target:
                # indices must be 1-indexed.
                return [index1 + 1, index2 + 1]
            # sum too big, reduce num_left
            elif temp_sum > target:
                index2 -= 1
            # sum too small, increase num_right
            else:
                index1 += 1