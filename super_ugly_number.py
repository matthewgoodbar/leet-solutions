import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        generated = [p for p in primes]
        heapq.heapify(generated)
        seen = set()
        res = 1
        for i in range(n-1):
            smallest = heapq.heappop(generated)
            res = smallest
            for p in primes:
                if p * smallest not in seen:
                    heapq.heappush(generated, p * smallest)
                    seen.add(p * smallest)
        return res

primes = [2,7,13,19]
n = 12
sol = Solution()
print(sol.nthSuperUglyNumber(n, primes))