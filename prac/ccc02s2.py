from math import *
def fact(num):
	cur = num
	facts = []
	div = 1
	while(cur != 1):
		div+=1
		if (cur%div==0):
			cur/=div
			facts.append(div)
			div = 1

	return facts


num = int(input())
denom = int(input())


#check for improper
mix = num//denom
num -= mix*denom 

frac = ""

if num != 0:
	num_facts = fact(num)
	denom_facts = fact(denom)

	overlap = []
	for n in num_facts:
		if n in denom_facts:
			denom_facts.remove(n)
			overlap.append(n)

	div = 1
	for n in overlap:
		div *= n

	num/=div
	denom/=div

	frac = str(int(num))+"/"+str(int(denom))

out = ""
if mix != 0:
	out+=(str(mix)+" ")

out+=frac

if out == "":
	out = "0"
print(out)
