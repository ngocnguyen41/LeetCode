class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []

        for x, y, r in queries:
            count = 0
            for x1, y1 in points:
                if (x1 - x)**2 + (y1 - y)**2 <= r**2:
                    count += 1
            result.append(count)
        return result        