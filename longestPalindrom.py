class Solution:
    def isPalindrom(self, s: str):
        i_count = len(s)

        for i in range(0, i_count // 2):
            if s[i] != s[i_count - i - 1]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        indexes = []
        max_len = 0

        if len(s) == 0:
            return ""

        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                if self.isPalindrom(s[i:j + 1]):
                    print(s[i:j + 1])
                    if max_len < j - i:
                        max_len = j - i
                        indexes = [i, j]
        if len(indexes) == 0:
            return s[0]

        return s[indexes[0]:indexes[1] + 1]





