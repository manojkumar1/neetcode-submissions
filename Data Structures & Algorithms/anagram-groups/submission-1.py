class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solmap = defaultdict(list)
        for i in strs:
            sorted_key = ''.join(sorted(i))
            solmap[sorted_key].append(i)

        return list([val for val in solmap.values()])