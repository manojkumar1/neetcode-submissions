class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            p = l + ((h - l) // 2)
            
            if target > nums[p] :
                l = p + 1
            elif target < nums[p]:
                h = p - 1
            elif target == nums[p]:
                return p
           
        return -1