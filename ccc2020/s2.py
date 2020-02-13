from pprint import *
from collections import deque
#input = open("inp.txt","r").readline

def factors(num):

	f = [1]
	while num != 1:

		for i in range(2,num+1):
			if num%i == 0:
				f.append(i)
				num=int(num/i)
				break
	return f

def makepairs(factors):

	tot = len(factors)*"1"
	ans = set([])
	num = ""
	c = 0

	while num != tot:

		num = format(c,"b")
		num = (len(tot)-len(num))*"0"+num

		c+=1

		a = 1
		b = 1
		for n in range(len(tot)):

			if num[n] == "1":
				a*=factors[n]
			else:
				b*=factors[n]

		ans.add((a,b))
	return list(ans)

M = int(input())
N = int(input())

grid = []
for i in range(M):
	grid.append(list(map(int,input().strip().split(" "))))

#print(makepairs([1,7,7]))
#pprint(grid)

x,y = 1,1
q = deque([(x,y)])
visited = []

end = False
while len(q) > 0:

	x,y = q[0]

	q.popleft()


	val = grid[y-1][x-1]
	visited.append(val)
	#print(visited)

	if x == N and y == M:
		end = True

	f = factors(val)
	pairs = makepairs(f)

	for p in pairs:
		if p[0] < 1 or p[0] > N or p[1] < 1 or p[1] > M or p in q or grid[p[1]-1][p[0]-1] in visited:
			continue

		q.append(p)




print(['no','yes'][end])
