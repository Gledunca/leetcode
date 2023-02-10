class Solution:
    def third(self, item):
        return item[2]
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point.append((sqrt( point[0]**2 + point[1]**2 )))
        points.sort(key=self.third)
        return [item[:2] for item in points[:k]]