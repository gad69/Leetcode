class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}

        for ele in strs:
            base = ''.join(sorted(ele))
            
            if base not in dic:
                dic[base] = [ele]
            else:
                dic[base].append(ele)
                
             
    
        return dic.values()
            
                


            




        