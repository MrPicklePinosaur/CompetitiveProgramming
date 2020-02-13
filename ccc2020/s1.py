import math
#input = open("inp.txt","r").readline

N = int(input())
inp = []
for i in range(N):
	inp.append(list(map(int,input().strip().split(" "))))
inp = sorted(inp,key=lambda x:x[0])

best = -1*math.inf
for i in range(len(inp)-1):
	speed = abs((inp[i+1][1]-inp[i][1])/(inp[i+1][0]-inp[i][0]))

	if speed > best:
		best = speed
print(best)