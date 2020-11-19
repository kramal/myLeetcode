class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        l_items = { "[" : "]", "{" : "}", "(" : ")" }
        i_index = 0
        while True:
            if i_index < 0 or len(s) == 0 or i_index > len(s)-1: 
                break
                
            s_curr_char = s[i_index]
            s_neg_char = l_items.get(s_curr_char)
            
            if s_curr_char == '[' or s_curr_char == '{' or s_curr_char == '(':
                i_neg_index = s.find(s_neg_char, i_index)
                
                if i_neg_index >= 0 and i_neg_index - i_index == 1:
                    s = s[:i_neg_index] + s[i_neg_index+1:]
                    s = s[:i_index] + s[i_index+1:]
                    i_index = i_index - 1 if i_index > 0 else 0
                    continue
                elif i_neg_index < 0:
                    return False
            i_index = i_index + 1
        
        return True if len(s) == 0 else False
            
                
                
        
        
        
        
        
        
        
        
