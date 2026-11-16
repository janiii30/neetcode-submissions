class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pr_q = []
        res = []

        def euc_distance(x,y):
            return (x)**2 + (y)**2

        for x,y in points:
            heapq.heappush(pr_q,(euc_distance(x,y),[x,y]))

        for _ in range(k):
            _, point = heapq.heappop(pr_q)
            res.append(point)

        return res