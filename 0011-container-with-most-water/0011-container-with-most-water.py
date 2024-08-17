class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height)-1
        maxArea = 0
        
        while l<r:
            maxArea = max(maxArea,min(height[l],height[r])*(r-l))
            
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
                
        return maxArea
                
            
            
            
            







        