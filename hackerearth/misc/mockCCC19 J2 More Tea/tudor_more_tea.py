f = open("input.txt","r")

chunks = 0
isChunk = False
for i in range(7):
	inp = f.readline().strip()

	if (not isChunk and inp == 'J'):
		isChunk = True
		chunks+=1
	elif (isChunk and inp == 'T'):
		isChunk = False

print(chunks)
	