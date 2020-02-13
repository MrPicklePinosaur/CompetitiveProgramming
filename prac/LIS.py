r = open("input.txt","r")

arr = list(map(int,r.readline().split(" ")))

dp = [1 for i in range(len(arr))]

for i in range(len(dp)):

	for n in range(i):
		if arr[n] < arr[i]:
			if dp[n] >= dp[i]:
				dp[i] = dp[n] + 1


print(dp)
print(max(dp))



