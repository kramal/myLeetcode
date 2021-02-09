class Solution :
    # not effective way
    def lengthOfLongestSubstring(self, string: str) -> int :
        str_len = len ( string )
        if str_len == 0 :
            return 0
        if str_len == 1 :
            return 1

        u_hash = {}
        left = 0
        right = 0
        longest = [ 0, 1 ]
        max_len = 0

        while right < str_len :
            ch = string [ right ]
            if max_len < right - left :
                max_len = right - left
                longest = [ left, right ]

            if ch in u_hash :
                del_idx = u_hash [ ch ]
                left = max ( del_idx + 1, left )

            u_hash [ ch ] = right
            right += 1

        if max_len < right - left :
            max_len = right - left
            longest = [ left, right ]

        return abs ( longest [ 0 ] - longest [ 1 ] )



