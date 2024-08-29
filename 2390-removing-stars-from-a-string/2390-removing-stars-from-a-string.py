class Solution:
    def removeStars(self, s: str) -> str:
        lis = list()

        for st in s:
            if st =='*':
                lis.pop()
            else:
                lis.append(st)

        return ''.join(lis)
        