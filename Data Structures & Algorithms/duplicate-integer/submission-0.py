class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset = set(nums)
        return len(nums) != len(dupset)

        