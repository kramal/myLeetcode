class Solution:
    
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k == 0:
            return 0
        
        if len(s) == 1 and k != 1:
            return 1
        
        if len(s) == 1 and k == 1:
            return 1
        
        max_len_temp = 0
        max_len = 0
        h = {}
        
        for i in range(0, len(s)):
            if s[i] in h:
                max_len_temp = max_len_temp + 1
            else:
                if len(h) == k:
                    h = {}
                    h[s[i]] = True
                    temp_len = 1
                    for ch in s[:i][::-1]:
                        if ch in h:
                            temp_len = temp_len + 1
                            continue
                        if len(h) == k:
                            break
                        h[ch] = True
                        temp_len = temp_len + 1
                    
                    max_len_temp = temp_len  
                else:
                    h[s[i]] = True
                    max_len_temp = max_len_temp + 1
                    
            max_len = max(max_len_temp, max_len)
            
        return max_len
                    
        
        
            
                
            
            
            
