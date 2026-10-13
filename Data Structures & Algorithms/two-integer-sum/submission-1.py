class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in comp_map:
                return [comp_map[comp], i]

            comp_map[nums[i]] = i
