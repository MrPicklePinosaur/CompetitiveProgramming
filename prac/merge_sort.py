ls = [5,3,8,1,9,4]

def mergesort(ls):
	if len(ls) > 1:
		r = []
		a = mergesort(ls[:len(ls)//2])
		b = mergesort(ls[len(ls)//2:])

		while True:

			if a[0] > b[0]:
				r.append(a.pop(0))
			elif b[0] > a[0]:
				r.append(b.pop(0))

			if len(a) < 1 and len(b) < 1:
				break;
	else:
		return ls

	return r

print(mergesort(ls))