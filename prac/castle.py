from pprint import *
from collections import deque
input = open("input.txt","r").readline

def parse(num):
	ans = ""
	if num%2 == 1:
		num-=1
		ans+="W"
	nums = [8,4,2]
	d = ["S","E","N"]
	for i in range(len(nums)):
		if num-nums[i] >= 0:
			num-=nums[i]
			ans+=d[i]
	return ans


M, N = list(map(int,input().strip().split(" ")))
inp = []
for i in range(N):
	inp.append(list(map(int,input().strip().split(" "))))

inp = [[parse(i) for i in n] for n in inp]

def flood(start):
	global inp

	q = deque([start])

	rooms = 0
	while len(q) > 0:
		x,y = q.popleft()
		wall = inp[y][x]

		if len(wall) == 0:
			continue

		rooms += 1

		direct = {"N":(0,-1),"E":(1,0),"S":(0,1),"W":(-1,0)}
		for w in wall:
			if w in direct:
				direct.pop(w)

		for d in direct:
			offset = direct[d]
			nx, ny = x+offset[0],y+offset[1]
			if (nx < 0 or nx > M) or (ny < 0 or ny > N) or (len(inp[ny][nx]) == 0):
				continue
			q.append((nx,ny))

		inp[y][x] = ""

	return rooms

roomsize = []
for y in range(N):
	for x in range(M):
		size = flood((x,y))
		if size > 0:
			roomsize.append(size)





for y in range(N):
	for x in range(M):
		rm = []
		for i in inp[y][x]:
			if (y == 0 and i == "N") or (y == M and i == "S") or (x == 0 and i == "W") or (x == N and i == "E"):
				continue
			rm.append(i)

print(f"{len(roomsize)}\n{max(roomsize)}")

