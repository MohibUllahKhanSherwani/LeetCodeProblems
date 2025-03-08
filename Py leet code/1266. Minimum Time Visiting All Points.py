# On a 2D plane, there are n points with integer coordinates 
# points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

# You can move according to these rules:

# In 1 second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words,
#  move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.


# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds


# Approach: Take a seconds var = 0, points [[1, 1], [3, 4], [-1, 0]] 
# iterate through the list in range (1, len(points))
# then calculate the distance using chebyshevs max distance using
# max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
# it basically returns the next steps/seconds needed to go to the next point
# finally return the seconds
from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for i in range(1, len(points)):
            seconds += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
        return seconds
s = Solution()
points=[[1 , 1] , [3 , 4] , [-1 , 0]]
print(s.minTimeToVisitAllPoints(points))
for i in range(1, len(points)):
    print(points[i - 1][0], points[i - 1][1])
    print(points[i][0], points[i][1])
