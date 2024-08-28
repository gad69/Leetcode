class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        for i in arr:
            if i not in dic:
                dic[i] =1
            dic[i]+=1


        if len(set(dic.values())) == len(dic):
            return True

        return False


        
        