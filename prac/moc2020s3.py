import math
#input = open("input.txt","r").readline

river = [[i,0] for i in range(1001)]

for i in range(int(input())):
	river[int(input())][1] += 1

river = sorted(river,key=lambda x:x[1],reverse=True)
#print(river)
stuff = {}
for i in range(len(river)):
	freq = river[i][1]
	if freq not in stuff:
		stuff[freq] = [river[i][0]]
	else:
		
		stuff[freq].append(river[i][0])

for i in stuff:
	stuff[i]=stuff[i][::-1]

#print(stuff)
if len(stuff[max(stuff)]) > 1:
	print(abs(stuff[max(stuff)][0]-stuff[max(stuff)][-1]))
else:
	one = stuff[max(stuff)][0]

	stuff.pop(max(stuff))
	best = -1*math.inf
	for n in stuff[max(stuff)]:
		if abs(one-n) > best:
			best = abs(one-n)
	print(best)




