class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            clean_word = "".join(sorted(word))
            if clean_word in anagrams:
                anagrams[clean_word].append(word)
            else:
                anagrams[clean_word] = [word]

        # print(anagrams)
        result = [x for x in anagrams.values()]

        return result


# def isAnagram(word1, word2):
#     return sorted(word1) == sorted(word2)


# def isEmpty(array):
#     return None if not array else array


# def count_char(word):
#     char_frequency = {}
#     for char in word:
#         char_count = char_frequency.get(char, 0) + 1
#         char_frequency[char] = char_count
#     # valid syntax for returning the key with the highest value
#     return char_frequency # type: ignore
