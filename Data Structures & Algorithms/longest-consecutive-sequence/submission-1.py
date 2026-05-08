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

        index, max_sequence = max(num_sequences.items(), key=lambda item: len(item[1]))

        return len(max_sequence)

        