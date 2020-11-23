class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        strs = sorted(strs, key=len)
        
        min_len_str = strs[0]
        
        result = ""
        
        for ind, ch in enumerate(min_len_str):
            for i in range(1,len(strs)):
                if ch != strs[i][ind]:
                    return result
                else:
                    if i == len(strs)-1:
                        result += ch
        
        return result
        
                    
        
        
