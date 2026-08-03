class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sollist = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            f = i + 1
            s = len(nums) - 1
            while f < s:
                tsum = nums[i] + nums[f] + nums[s]
                if tsum > 0:
                    s -= 1
                elif tsum < 0:
                    f += 1
                else:
                    sollist.append([nums[i] , nums[f] , nums[s]])
                    f += 1
                    s -= 1
                    while nums[f] == nums[f - 1] and f < s:
                        f += 1
        print(nums, sollist)
        return sollist