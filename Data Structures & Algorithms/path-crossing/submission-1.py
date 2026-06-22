class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point = (0,0)
        seen = {point}
        for char in path:
            if char == 'N':
                point = (point[0] + 1, point[1])
            if char == 'S':
                point = (point[0] - 1, point[1])
            if char == 'E':
                point = (point[0], point[1] + 1)
            if char == 'W':
                point = (point[0], point[1] - 1)
            if point in seen:
                return True
            else:
                seen.add(point)
        
        return False
            

