class Solution:
    def getProbability(self, balls: list[int]) -> float:
        n = len(balls)
        total = sum(balls)
        half = total // 2
        ways = comb(total, half)
        good = 0
        def dfs(i, taken, d1, d2, ways):
            nonlocal good
            if i == n:
                if taken == half and d1 == d2:
                    good += ways
                return
            for ball in range(balls[i] + 1):
                nt = taken + ball
                if nt > half:
                    break
                w = ways * comb(balls[i], ball)
                dfs(i+1, nt, d1 + (ball > 0), d2 + (balls[i]-ball > 0), w)
        dfs(0, 0, 0, 0, 1)
        return good/ways
