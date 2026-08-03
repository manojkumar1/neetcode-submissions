class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in solmap:
                return [solmap[complement], i]

            solmap[nums[i]] = i

        return []     