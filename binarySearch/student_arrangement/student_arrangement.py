f = open("input.txt","r")

inp = list(map(int,f.readline().split(" ")))
#n m k

perferred = list(map(int,f.readline().split(" ")))

rows = [inp[2] for i in range(inp[1])]

for p in perferred:
	rows[p-1]-=1

print(rows)