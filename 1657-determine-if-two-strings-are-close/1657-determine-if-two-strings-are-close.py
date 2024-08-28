class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        
        
        lis1 = [val for key,val in c1.items()]
        lis2 = [val for key,val in c2.items()]
        
        return c1==c2 or ((Counter(lis1)==Counter(lis2)) and set(word1)==set(word2))
        
        
        