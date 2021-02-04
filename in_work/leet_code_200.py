class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s_len = len(s)

        if s_len == 0:
            return 0

        if s_len == 1:
            return 1

        lengths = {}
        for i in range(0, s_len - 1):
            hash_map = {}
            hash_map[s[i]] = 1
            lengths[i] = 1

            if i == 0:
                j = i + 1
            else:
                j = start_from

            while j < s_len:
                if s[j] in hash_map.keys():
                    lengths[i] = j - i
                    break
                else:
                    lengths[i] = lengths[i] + 1
                    hash_map[s[j]] = 1
                j = j + 1

            start_from = j
        print(lengths)
        return max(lengths.values())


