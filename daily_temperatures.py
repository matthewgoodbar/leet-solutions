from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # monostack records the indices of days of monotonically decreasing temp
        monostack = deque()
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            if not monostack or temperatures[monostack[-1]] >= temperatures[i]:
                # if current temp is equal to or decreasing compared to last temp,
                # append index of temp to monostack
                monostack.append(i)
            else:
                # if current temp is greater than last temp, then the number of
                # days to wait for a warmer day is current index - last index.
                # same is true for all previous temps in the stack less than
                # the current temp, so we use a while loop.
                while monostack and temperatures[monostack[-1]] < temperatures[i]:
                    resolvedIdx = monostack.pop()
                    res[resolvedIdx] = i - resolvedIdx
                monostack.append(i)
        return res

sol = Solution()
temperatures = [89,62,70,58,47,47,46,76,100,70]
print(sol.dailyTemperatures(temperatures))