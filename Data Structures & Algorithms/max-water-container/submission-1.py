class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f = 0
        s = len(heights) - 1
        max_area = 0

        while f < s:
            area = min(heights[f], heights[s]) * (s-f)
            max_area = max(max_area, area)
            if heights[f] <= heights[s]:
                f+=1
            else:
                s-=1    

        return max_area
