import math

#r = open("input.txt","r")
num = int(input())

n, k, g, c = [], [], [], []
for i in range(num):
	inp = input().split(" ")
	n.append(inp[0])
	k.append(int(inp[1]))
	g.append(int(inp[2]))
	c.append(int(inp[3]))

bestcost = -1*math.inf
bestpair = []
for b in range(num):
	for a in range(b+1,num):
		cost = 2*(k[a]+k[b])+(g[a]+g[b])-(c[a]+c[b])
		if cost > bestcost:
			bestcost = cost
			bestpair = [n[a],n[b]]

bestpair.sort()
print(["\n".join(bestpair),-1][len(bestpair)==0])