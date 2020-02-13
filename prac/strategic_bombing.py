from collections import deque
input = open("input.txt","r").readline

roads = {}
usin = []
inp = ""
while True:
	inp = input().strip()

	if inp == "**":
		break

	usin.append(inp)

	for i in range(2):
		one = inp[i]
		two = inp[1-i]

		if one not in roads:
			roads[one] = [two]
		else:
			roads[one].append(two)

def traverse(roads,rm):
	#roads[rm[0]].remove(rm[1])
	#roads[rm[1]].remove(rm[0])

	visited = []
	q = deque([])
	q.append("A")

	while len(q) > 0:
		
		cur = q.popleft()

		if cur in visited:
			continue
		visited.append(cur)

		if cur == "B":
			return True

		for p in roads[cur]:
			if (cur == rm[0] and p == rm[1]) or (cur == rm[1] and p == rm[0]):
				continue
			if p not in visited:
				q.append(p)
	return False

#print(traverse(roads,"CF"))
tot = 0
for i in usin:

	if not traverse(roads,i):
		tot += 1
		print(i)

print(f"There are {tot} disconnecting roads.")







