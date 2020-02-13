#input = open("inp.txt","r").readline

N = input().strip()
H = input().strip()

def splitN():
	ans = []
	for n in N:
		ans.append(n)
	return ans

q = []
perms = []
for i in range(len(H)):

	let = H[i]

	added = 0
	if let in N:
		s = splitN()
		s.remove(let)
		q.append([let,s])
		added = -1

	finished = []
	for n in range(len(q)+added):

		if let not in q[n][1]:
			finished.append(q[n])
			continue

		q[n][1].remove(let)
		q[n][0]+=let

		if len(q[n][0]) == len(N): #found perm
			perms.append(q[n][0])
			finished.append(q[n])

	for f in finished:
		q.remove(f)

print(len(set(perms)))