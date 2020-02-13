#input = open("input.txt","r").readline

n = int(input())

tot = 0
for y in range(1,6):
	for x in range(0,y+1):
		#print(x,y)
		if x+y == n:
			tot+=1
print(tot)