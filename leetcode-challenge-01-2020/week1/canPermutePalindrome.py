def canPermutePalindrome(self, s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True

    char_mapping = {}

    for i in range(0, len(s)):
        if s[i] not in char_mapping:
            char_mapping[s[i]] = 1
        else:
            char_mapping[s[i]] = char_mapping[s[i]] + 1

    for key in char_mapping.keys():
        char_mapping.update({key: char_mapping.get(key) % 2})

    char_mod_counts = list(char_mapping.values())

    if sum(char_mod_counts) == 0 or sum(char_mod_counts) == 1:
        return True

    return False