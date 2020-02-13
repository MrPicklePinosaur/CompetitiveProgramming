import math

r = open("input.txt","r")

n, m = list(map(int,r.readline().split(" ")))

bills = list(map(int,r.readline().split(" ")))


dp = [math.inf for i in range(n+1)]
dp[0] = 0

for i in range(len(dp)):

	for b in bills:
		if b <= i:
			dp[i] = min(1+dp[i-b],dp[i])

print([dp[-1],-1][dp[-1]!=math.inf])