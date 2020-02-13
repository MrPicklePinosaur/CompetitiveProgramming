#input = open("inp.txt","r").readline

N = input().strip()
H = input().strip()


ans = set([])
def perms(cur,left):
	global ans
	if len(left) == 0:
		ans.add(cur)
		return

	for i in range(len(left)):
		
		perms(cur+left[i],left[:i]+left[i+1:])

perms("",N)
#print(ans)
tot = 0

for a in ans:
	if a in H:
		tot+=1
print(tot)