import math
class Solution:
    def reverse(self, x: int) -> int:
        a_max = int(math.pow(2,31))
        a_min = -int(math.pow(2,31))
        
        if abs(x) > a_max:
            return 0
        
        s_org_num = str(x)
        s_num = s_org_num[1:] if s_org_num[0] == '-' else s_org_num
        i_length = len(s_num)
        
        k = i_length - 1
        i_rm_pos = 0
        while k >= 0:
            if s_num[k] != '0':
                break
            else:
                i_rm_pos = i_rm_pos + 1
                k = k - 1
        
        s_num = s_num[:i_length - i_rm_pos]
        
        i_length = len(s_num)
        
        result = []
        
        for i in range(0, i_length):
            result.append(s_num[i_length - i - 1])
        
        i_unsigned = ''.join(result)
        if len(i_unsigned) == 0:
            return 0
        if int(i_unsigned) > a_max:
            return 0
        
        result = i_unsigned if s_org_num[0] != '-' else '-' + i_unsigned
      
        return 0 if len(result) == 0 else result
        
        
        
