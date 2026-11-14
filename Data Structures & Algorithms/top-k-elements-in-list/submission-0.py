from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter()

        for n in nums:
            if n in freqs:
                freqs[n] += 1
            else: freqs[n] = 0

        return [k for k,_ in freqs.most_common(k)]