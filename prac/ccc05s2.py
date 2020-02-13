r = open("inp.txt","r")
	
size = list(map(int,r.readline().split(" ")))
#size = list(map(int,input().split(" ")))

inp = []
while True:
	i = list(map(int,r.readline().split(" ")))
	#i = list(map(int,input().split(" ")))
	inp.append(i)
	if (i[0] == 0 and i[1] == 0):
		break
x = 0
y = 0
px = 0
py = 0
for i in range(len(inp)-1):

	x += inp[i][0]
	y += inp[i][1]

	if (x < 0):
		x = 0
	elif (x > size[0]):
		x = size[0]
	if (y < 0):
		y = 0
	elif (y > size[0]):
		y = size[0]

	if (px != x and py != y):
		print(x,y)

	px = x
	py = y

	

'''
while True:
	#i = list(map(int,r.readline().split(" ")))
	i = list(map(int,input().split(" ")))
	print(i)
	if (i[0] == 0 and i[1] == 0):
		break
'''