f = open("input.txt","r")

n = int(f.readline())

weights = [0 for i in range(31)]

for i in range(n):

	msg = f.readline().strip().split(" ")

	dates = [d for d in msg if d.isdigit()]

	w = 2 if msg[0] == "G:" else 1
	for d in dates:
		weights[int(d)] += w

max_val = max(weights)
best_days = [i for i, v  in enumerate(weights) if v == max_val]

print(best_days)
if len(best_days) == 1:
	print("Date" if (best_days[0] == 19 or best_days[0] == 20) else "No Date")
else:
	print("No Date")