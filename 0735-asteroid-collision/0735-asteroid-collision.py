class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()

        for ast in asteroids:
            while stack and stack[-1]>0 and ast<0:
                if abs(ast)>stack[-1]:
                    stack.pop()
                elif abs(ast)==stack[-1]:
                    stack.pop()
                    ast = 0
                elif abs(ast)<stack[-1]:
                    ast = 0
            if ast:
                stack.append(ast)

        return stack



        