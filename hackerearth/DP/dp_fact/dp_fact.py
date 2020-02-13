fact_memo = [-1 for n in range(100000)]
highest_modified = 0

def fact(i):
	global highest_modified
	fact_memo[0] = 1
	fact_memo[1] = 1

	if (i > highest_modified):
		for n in range(i+1):
			if (fact_memo[n] != -1):
				continue

			fact_memo[n] = n*fact_memo[n-1]
		highest_modified = i

	return fact_memo[i]




f = open("input.txt","r")

n = int(f.readline())

for i in range(n):
	inp = int(f.readline())
	print(fact(inp))

