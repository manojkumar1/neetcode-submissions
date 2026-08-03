class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = counts.most_common(k)
        return [val[0] for val in freq]