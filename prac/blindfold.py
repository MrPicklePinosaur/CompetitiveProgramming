from pprint import *

r = open("input.txt","r")

row = int(r.readline())
col = int(r.readline())

grid = []
for i in range(row):
	grid.append([n for n in r.readline().strip()])

direct = [(0,1),(-1,0),(0,-1),(1,0)]


inst = []
for ins in range(int(r.readline())):
	inst.append(r.readline().strip())

for i in range(4):
	facing = i
	moves = []
	for inp in inst:

		if inp == "L":
			facing -= 1
		elif inp == "R":
			facing += 1

		if facing >= 4:
			facing -= 4
		elif facing <= -1:
			facing += 4

		if inp == "F":
			moves.append(direct[facing])

	for y in range(row):
		for x in range(col):
			cx,cy = x,y
			if grid[cy][cx] == 'X':
				continue

			for m in moves:

				cx,cy = cx+m[0],cy+m[1]

				if cx >= col or cx < 0:
					break
				elif cy >= row or cy < 0:
					break 
				elif grid[cy][cx] == 'X':
					break
			else:
				grid[cy][cx] = '*'

print("\n".join(["".join(i) for i in grid]))




