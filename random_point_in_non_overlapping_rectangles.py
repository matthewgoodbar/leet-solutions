import numpy as np

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.totalPoints = 0
        self.rects = rects
        self.weights = []
        for rect in rects:
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]
            points = (width+1) * (height+1)
            self.weights.append(points)
            self.totalPoints += points
        self.weights = [weight / self.totalPoints for weight in self.weights]
        

    def pick(self) -> list[int]:
        rectIdx = np.random.choice([_ for _ in range(len(self.rects))], p=self.weights)
        rect = self.rects[rectIdx]
        xs = [i for i in range(rect[0], rect[2]+1)]
        ys = [j for j in range(rect[1], rect[3]+1)]
        return [np.random.choice(xs), np.random.choice(ys)]