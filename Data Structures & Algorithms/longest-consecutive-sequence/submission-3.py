class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_sequences = dict()

        for num in sorted(nums):
            if (num - 1) in num_sequences:
                if num in num_sequences[num-1]:
                    continue
                else:
                    num_sequences[num-1].append(num)
                    num_sequences[num] = num_sequences[num-1]
            else:
                num_sequences[num] = [num]

        # the result of max() in this case is a tuple, e.g.: (1, [1,2,3])
        # so 2 variables must be assigned to access max_sequence
        index, max_sequence = max(num_sequences.items(), key=lambda item: len(item[1]))

        return len(max_sequence)

        