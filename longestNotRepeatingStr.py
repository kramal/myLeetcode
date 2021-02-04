class Solution:
    # not effective way
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        lengths = {}
        for i in range(0, len(s) - 1):
            hash_map = {}
            hash_map[s[i]] = 1
            lengths[i] = 1

            for j in range(i + 1, len(s)):
                if s[j] in hash_map.keys():
                    lengths[i] = j - i
                    break
                else:
                    lengths[i] = lengths[i] + 1
                    hash_map[s[j]] = 1

        return max(lengths.values())