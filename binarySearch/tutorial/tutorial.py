def b_search(query):
	global li

	low = 0
	high = len(li)

	while (low<=high):
		mid = int((high+low)/2)
		print(mid)
		if (li[mid] < query):
			low = mid
		elif (li[mid] > query):
			high = mid
		elif (li[mid] == query):
			print("found")
			return mid+1
	return -1

f = open("input.txt","r")

n = int(f.readline())

li = list(map(int,f.readline().split(" ")))

q = int(f.readline())

queries = [int(f.readline()) for a in range(q)]

for query in queries:
	#print(b_search(query))
	b_search(query)


