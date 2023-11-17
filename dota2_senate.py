from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue = deque()
        dQueue = deque()
        for i, c in enumerate(senate):
            if c == 'R':
                rQueue.append(i)
            else:
                dQueue.append(i)
        
        index = len(senate)
        while rQueue and dQueue:
            rSenator = rQueue.popleft()
            dSenator = dQueue.popleft()
            if rSenator < dSenator:
                rQueue.append(index)
            else:
                dQueue.append(index)
            index += 1
        
        return 'Radiant' if rQueue else 'Dire'