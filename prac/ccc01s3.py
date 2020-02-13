
r = open("inp.txt","r")

tree = {}	
usin = []
while True:

	inp = r.readline().strip()

	if inp == "**":
		break

	usin.append(inp)

	for c in range(2):
		a = inp[c]
		b = inp[c-1]
		if a not in tree:
			tree[a] = [b]
		else:
			tree[a].append(b)



def traverse(tree, road):

	tree[road[0]].remove(road[1])
	tree[road[1]].remove(road[0])

	#print(tree)
	#bfs explore
	visited = []
	queue = ["A"]
	curnode = ""
	while len(queue) != 0:
		curnode = queue[0]
		visited.append(curnode)
		del queue[0]

		if curnode == "B":
			return 1

		toexplore = [i for i in tree[curnode] if i not in visited]
		#print(f"visited: {visited}")
		#print(f"toexplore: {toexplore}")
		#print(f"queue: {queue}")
		for i in toexplore:
			queue.append(i)
			
	return 0


for road in usin:
	#print(f"{road} =-=-=-=-=-=-=-=")
	if not traverse(tree,road):
		print(road)
		pass