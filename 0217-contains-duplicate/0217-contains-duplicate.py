class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for ele in nums:
            if ele not in dic:
                dic[ele] = 1
                
            else:
                dic[ele]+=1
                
        return any(val>=2 for key, val in dic.items())







        