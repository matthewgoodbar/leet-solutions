from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = deque()
        for asteroid in asteroids:
            if asteroid > 0: #going right
                stack.append(asteroid)
            else: #going left
                aSize = abs(asteroid)
                done = False
                while not done:
                    done = True
                    if not stack or stack[-1] < 0: #stack empty or going left too, just append
                        stack.append(asteroid)
                    elif stack[-1] < aSize: #top of stack smaller
                        stack.pop()
                        done = False
                    elif stack[-1] == aSize: #top of stack same size
                        stack.pop()
                    #if top of stack is bigger, we're done with this asteroid
                    
        return list(stack)