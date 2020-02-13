from collections import deque

input = open("input.txt","r").readline

for t in range(int(input())):
	top = deque([])
	branch = deque([])
	lake = 0
	for n in range(int(input())):
		top.append(int(input()))

	valid = True
	while len(top) > 0:
		if top[-1] == lake+1: #top to lake
			top.pop()
			lake+=1
		elif len(branch) == 0 or top[-1] < branch[-1]: #top to branch
			branch.appendleft(top.pop())
		elif len(branch) > 0 and branch[0] == lake+1: #branch to lake
			branch.popleft()
			lake+=1
		else:
			valid = False
			break
		
	print(["N","Y"][valid])



