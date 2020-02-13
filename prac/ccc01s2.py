from math import *
from pprint import *
r = open("inp.txt","r")
low = int(r.readline())
high = int(r.readline())


def spiral(low,high):

	dif = high-low
	size = ceil((dif+1)**0.5)

	longest_dig = len(str(high))
	grid = [[" "*longest_dig for n in range(size)] for n in range(size)]

	d = [(0,1),(1,0),(0,-1),(-1,0)]

	x = y = (size-1)//2
	#print(f"starting:{x},{y}")

	num = low
	count = 1
	dir_count = 0
	cur_d = d[0]


	while(True):
		for i in range(2):
			for n in range(count):
				#print(cur_d)
				#print(x,y)
				#print(num)

				padding = (longest_dig-len(str(num)))*" "
				grid[y][x] = (padding+str(num))
				x += cur_d[0]
				y += cur_d[1]
				num += 1

				if (num > high):
					return grid

				#pprint(grid)
				#print("=-=-=-=-=-=")

			dir_count+=1
			cur_d = d[dir_count%4]

			
		count += 1


result = ""
for i in spiral(low,high):
	for n in i:
		result += (n+" ")
	result += "\n"
print(result)