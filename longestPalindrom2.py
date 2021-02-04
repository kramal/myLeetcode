class Solution:

    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return ""

        if len(s) == 1:
            return s

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        max_start_idx = None
        max_finish_idx = None
        max_len = 0
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                left = i
                right = i + 1
                for j in range(0, len(s)):
                    if left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                        left = left - 1
                        right = right + 1
                    else:
                        break

                if max_len < right + 1 - left:
                    max_len = right + 1 - left
                    max_start_idx = left
                    max_finish_idx = right + 1

            if i - 1 > -1 and s[i - 1] == s[i + 1]:
                left = i - 1
                right = i + 1
                for j in range(0, len(s)):
                    if left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                        left = left - 1
                        right = right + 1
                    else:
                        break

                if max_len < right - left + 1:
                    max_len = right - left + 1
                    max_start_idx = left
                    max_finish_idx = right + 1

        if max_start_idx is None:
            return s[0]
        else:
            return s[max_start_idx:max_finish_idx]








