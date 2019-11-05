f = open("input.txt","r")

n = int(f.readline())

uni = list(map(int,f.readline().split(" ")))

unique = {}
for i in uni:
	if i in unique:
		unique[i] += 1
	else:
		unique[i] = 1
print(unique)