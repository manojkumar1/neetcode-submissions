class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        sollist = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            sollist[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            sollist[i] *= suffix
            suffix *= nums[i]
        
        return sollist
                