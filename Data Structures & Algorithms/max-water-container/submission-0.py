class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = []
        for i in range(len(heights)):
            for j in range(len(heights)):
                area.append(abs((j-i) * min(heights[j],heights[i])))

        max_area = max(area)

        return max_area
