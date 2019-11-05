f = open("input.txt","r")

n = int(f.readline())

count = {}

data = list(map(int,f.readline().split(" ")))

k = int(f.readline())

for n in data:
	if n in count:
		count[n] += 1
	else:
		count[n] = 1

k_times = [n for n in count if count[n] == k]
print(min(k_times))

