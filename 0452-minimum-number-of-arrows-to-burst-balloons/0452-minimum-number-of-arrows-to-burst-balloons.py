class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)
        
        arrows = 0
        i = 0
        
        while i < n:
            arrows += 1
            end = points[i][1]
            
            j = i + 1
            while j < n and points[j][0] <= end:
                end = min(end, points[j][1])  
                j += 1
            
            i = j
        
        return arrows
