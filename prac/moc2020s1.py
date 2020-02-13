#input = open("input.txt","r").readline

n = int(input())
sw = list(map(int,input().split(" ")))
se = list(map(int,input().split(" ")))

sw_tot = 0
se_tot = 0

max_k = 0
for i in range(n):
	sw_tot += sw[i]
	se_tot += se[i]

	if sw_tot == se_tot:
		max_k = i+1

print(max_k)
