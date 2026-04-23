class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            clean_word = "".join(sorted(word))
            if clean_word in anagrams:
                anagrams[clean_word].append(word)
            else:
                anagrams[clean_word] = [word]

        result = [x for x in anagrams.values()]

        return result

