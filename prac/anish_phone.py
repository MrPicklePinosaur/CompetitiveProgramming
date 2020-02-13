from pprint import *

r = open("input.txt","r")

t, n = list(map(int,r.readline().split(" ")))

name = [""]
prod = [0]
charge = [0]
for i in range(n):
	inp = r.readline().split(" ")
	name.append(inp[0])
	prod.append(int(inp[1]))
	charge.append(int(inp[2]))

#0-name 1-productivity 2-charge
dp = [[0 for i in range(t+1)] for j in range(n+1)]
for y in range(1,n+1):

	for x in range(1,t+1):
		if charge[y] <= x:
			dp[y][x] = max(prod[y-1],prod[y]+dp[y-1][x-charge[y]])
		else:
			dp[y][x] = dp[y-1][x]

items = []
cx, cy = t, n
while cx > 0 and cy > 0:

	if dp[cy][cx] == dp[cy-1][cx]:
		cy -= 1
	else:
		cx -= charge[cy] 
		items.append(name[cy])
		cy -= 1

items.sort()


print(dp[n][t],sum([charge[items.index(i)] for i in items]))
print(" ".join(items))

#1d
'''
apps = []
for i in range(usin[1]):
	apps.append(r.readline().split(" "))
	apps[i][1] = int(apps[i][1])
	apps[i][2] = int(apps[i][2])

dp = [0 for i in range(usin[0])]

for i in range(len(dp)):

	for w in apps:
		if w[2] <= i:
			prod = w[2]+dp[i-w[2]]
			if prod > dp[i]:
				dp[i] = prod

print(dp)
'''