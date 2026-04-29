class Solution:
    def __init__(self, points):
        self.points = points

    def findClosestPair(self):
        import math
        min_dist = float('inf')
        n = len(self.points)
    
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = self.points[i]
                x2, y2 = self.points[j]
                d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                min_dist = min(min_dist, d)
    
        return min_dist
