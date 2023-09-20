import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self) -> list[float]:
        randr = math.sqrt(random.random()) * self.radius
        randtheta = random.random() * 2 * math.pi
        return [randr * math.cos(randtheta) + self.x, randr * math.sin(randtheta) + self.y]

    def testPoint(self, coords):
        randx, randy = coords
        dist = math.sqrt((self.x - randx)**2 + (self.y - randy)**2)
        if dist <= self.radius:
            return None
        else:
            return [coords, dist, self.radius]

sol = Solution(0.01, -73839.1, -3289891.3)

for _ in range(30000):
    coord = sol.randPoint()
    anomaly = sol.testPoint(coord)
    if anomaly:
        print("anomaly found")
        print(f'coords: {anomaly[0]}')
        print(f'dist from center: {anomaly[1]}')
        print(f'radius of circle: {anomaly[2]}')
        break
