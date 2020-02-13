f = open("input.txt","r")

size = int(f.readline())

list1 = f.readline().strip().split(" ")
list2 = f.readline().strip().split(" ")
data = {list1[i] : list2[i] for i in range(size)}


for k in data:
	v = data[k]

	if (data[v] != k or k == v):
		print("bad")
		break
else:
	print("good")

	
