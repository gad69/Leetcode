class Solution(object):
    def twoSum(self, nums, target):
        l = 0
        r = len(nums)-1
        arr = []
        nums_with_indices = [(j,i) for i,j in enumerate(nums)]
        nums_with_indices.sort()
        
        while l<r:
            temp_sum = nums_with_indices[l][0]+nums_with_indices[r][0]
            
            if temp_sum< target:
                l = l+1
                
            elif temp_sum> target:
                r = r-1
                
            else:
                arr.extend([nums_with_indices[l][1],nums_with_indices[r][1]])
                break
                
                
                
        return arr
                
                
                
                
                
                
                
                
                
        
        
        
        




        