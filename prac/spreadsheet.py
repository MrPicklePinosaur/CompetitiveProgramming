from pprint import *

r = open("input.txt","r")

sheet = [['*' for i in range(9)] for n in range(10)]

inp = []
for y in range(10):
	inp.append(r.readline().strip().split())

def locate(pos):
	return int(pos[1])-1, ord(pos[0])-65

def evaluate(prev,eq):
	global inp

	if eq.isnumeric():
		return int(eq)
	if eq == "*":
		return "*"

	cells = eq.split("+")
	tot = 0
	for c in cells:
		x,y = locate(c)
		if (x,y) in prev:
			return "*"
		prev.append((x,y))
		val = evaluate(prev,inp[y][x])
		inp[y][x] = str(val)
		if val == "*":
			return "*"
		tot += val
	return tot

#print(evaluate([],"A8"))
#pprint(inp)


for y in range(10):

	for x in range(9):
		inp[y][x] = str(evaluate([],inp[y][x]))
print("\n".join([" ".join(i) for i in inp]))
