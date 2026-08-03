class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointers approach

        f=0
        s=len(numbers)-1

        while f < s:
            tsum = numbers[f] + numbers[s]
            if tsum < target:
                f+=1
            elif tsum > target:
                s-=1
            else:
                return [f+1,s+1]
            
        return []