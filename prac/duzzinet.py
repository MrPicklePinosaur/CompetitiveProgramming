from pprint import *
from queue import PriorityQueue
#input = open("input.txt","r").readline
N = int(input())

mat = []
for i in range(N):
	mat.append(list(map(int,input().strip().split())))

visited = []
path = []
q = PriorityQueue()
q.put((0,(0,0)))
#(weight,(start,end))
while len(visited) != N:
	p = q.get()
	curnode = p[1][1]
	if curnode in visited:
		continue
	path.append(p)
	visited.append(curnode)
	for n in range(len(mat[curnode])):
		weight = mat[curnode][n]
		q.put((weight,(curnode,n)))

tot = 0
for i in path:
	tot += i[0]
print(tot)