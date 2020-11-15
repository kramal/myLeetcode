class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        
        old_dict = {}
        for k in range(0,j+1):
            old_dict[k] = nums[k]
     
        new_dict = {k: v for k, v in sorted(old_dict.items(), key=lambda item: item[1])}
        
        pairs = []
        
        new_nums = list(new_dict.values())
        
        while i < j:
            current_sum = new_nums[i] + new_nums[j]
            
            if current_sum == target:
                pairs.append([list(new_dict.keys())[i], list(new_dict.keys())[j]])
            
            if current_sum < target:
                i = i + 1
                continue
            
            if current_sum > target:
                j = j - 1
                continue
            
            i = i + 1
            j = j - 1
            
        result = pairs[0] if len(pairs) > 0 else []
        
        return result
                
        
