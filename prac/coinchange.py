input = open("input.txt","r").readline

N = int(input())
n = int(input())

S = []
for i in range(n):
	S.append(int(input()))

S.sort()
dp = [0 for i in range(N)]

for i in range(len(dp)):
	for c in S:
		if dp[i-c] != 0:
			dp[i]+=(dp[i-c]+1)
			break
		elif i == c:
			dp[i]+=1		

print(dp[-1])
