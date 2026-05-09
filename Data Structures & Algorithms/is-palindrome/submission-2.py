class Solution:
    def isPalindrome(self, s: str) -> bool:
        working_str = "".join(s.split())
        clean_str = "".join([ch.lower() for ch in working_str if ch.isalpha() or ch.isdigit()])
        n = len(clean_str)
        l, r = 0, n-1

        while l < r:
            if clean_str[l] != clean_str[r]:
                return False
            l += 1
            r -= 1

        return True
        