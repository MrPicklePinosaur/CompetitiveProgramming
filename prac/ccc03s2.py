import re

r = open("inp.txt","r")

verses = int(r.readline())

for i in range(verses):
	syl = []
	for n in range(4):
		s = r.readline().split(" ")[-1][::-1]
		end = re.findall(r"^[^aeiou]*[aeiou]",s,re.IGNORECASE)
		if end == []:
			end = [s]
		syl.append(end[-1].strip().lower())
	print(syl)

	if syl[0] == syl[1] and syl[0] == syl[2] and syl[0] == syl[3]:
		print('perfect')
	elif syl[0] == syl[1] and syl[2] == syl[3]:
		print('even')
	elif syl[0] == syl[2] and syl[1] == syl[3]:
		print('cross')
	elif syl[0] == syl[3] and syl[1] == syl[2]:
		print('shell')
	else:
		print('free')