class Solution:
    
    def get_num_order(self,x):
        order = 1
        temp = x
        while temp > 10:
            temp = temp/10
            order = order + 1
        return order
    
    def get_main_num(self,x):
        if x < 10:
            return x
        
        result = int( x/int(math.pow(10,self.get_num_order(x)-1)) )
        
        if result >= 10:
            return int(result/10)
        
        return result
    
    def get_last_num(self,x):
        result = 0
        
        if x%10 == 0:
            while x%10 == 0:
                x = int(x/10)
                
        order = self.get_num_order(x)
        
        while order > 1:
            x = x - self.get_main_num(x) * math.pow(10, order - 1)
            order = self.get_num_order(x)
            
        result = int(x)
        return result
    
    def isPalindrome(self, x: int) -> bool:
        max32 = math.pow(2,31) - 1
        
        if x > max32 or x < 0:
            return False
        
        if x != 0 and x % 10 == 0:
            return False
        
        if x < 10 and x >= 0:
            return True
        
        order = self.get_num_order(x)
        temp_order = 1
        divider_one = 1
        divider_two = int(math.pow(10,order))

        while temp_order <= order:
            i_first = (x//divider_one)
            i_second = (x%divider_two)
            divider_one = divider_one * 10
            divider_two = int(divider_two / 10)
            temp_order = temp_order + 1
            
            if self.get_last_num(i_first)  != self.get_main_num(i_second):
                return False
            
        return True
        
        
        
        
        
        
        
        
        
        
