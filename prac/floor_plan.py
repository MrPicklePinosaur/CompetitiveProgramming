from pprint import *

r = open("input.txt","r")

boards = int(r.readline())
row = int(r.readline())
col = int(r.readline())

plan = []
for i in range(row,0,-1):
	plan.append([c for c in r.readline().strip()])


def flood(x,y):
	global plan
	global row
	global col

	cx, cy = x, y

	di = [(1,0),(0,-1),(-1,0),(0,1)]
	q = [(x,y)]
	size = 0
	while len(q) > 0:

		cx, cy = q[0][0], q[0][1]

		for d in di:
			nx, ny = cx+d[0], cy+d[1]
			if nx < 0 or nx >= col:
				continue
			if ny < 0 or ny >= row:
				continue
			if plan[ny][nx] == '.' and ((nx,ny) not in q):
				q.append((nx,ny))

		plan[cy][cx] = 'I'
		del q[0]
		size += 1
	return size

rooms = []
for y in range(row):
	for x in range(col):
		if plan[y][x] == '.':
			rooms.append(flood(x,y))

rooms.sort()
rooms.reverse()

c = 0
for r in rooms:
	if boards >= r:
		boards -= r
		r = 0
	else:
		break
	c+=1


print(c,["rooms,","room,"][c==1], boards, "square metre(s) left over")


	
