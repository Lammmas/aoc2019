start = 153517
end = 630395

count = 0

for c in range(start, end + 1):
	code = [ int(e) for e in str(c) ]

	decr = False
	same = False
	prev = -1

	for n in code:
		if n == prev:
			same = True
		elif n < prev:
			decr = True
			break

		prev = n

	hasPair = False
	if same:
		numbers = {}
		for n in code:
			if str(n) in numbers:
				numbers[str(n)] += 1
			else:
				numbers[str(n)] = 1

		for n, v in numbers.items():
			if v == 2:
				hasPair = True

	if not decr and same and hasPair:
		count += 1

print(count)
