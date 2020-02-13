from pprint import *
from collections import deque
input = open("inp.txt","r").readline

def factors(num):

	f = [1]
	while num != 1:

		for i in range(2,num+1):
			if num%i == 0:
				f.append(i)
				num=int(num/i)
				break
	return f

M = int(input())
N = int(input())

grid = []
for i in range(M):
	grid.append(list(map(int,input().strip().split(" "))))
pprint(grid)

visited = []
q = deque([(1,1)])
while len(q) > 0:

	x,y = q.popleft()
	val = grid[y-1][x-1]
	fac = factors(val)

	for f in fac:
		



