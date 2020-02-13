from collections import deque

input = open("input.txt","r").readline

q = int(input())
n = int(input())
d = deque(sorted(list(map(int,input().split(" ")))))
p = deque(sorted(list(map(int,input().split(" ")))))

tot = 0
for i in range(n):

	if q == 1:
		tot += max(d.pop(),p.pop())
	else:
		if d[-1] >= p[-1]:
			tot += max(d.pop(),p.popleft())
		else:
			tot += max(p.pop(),d.popleft())
print(tot)


