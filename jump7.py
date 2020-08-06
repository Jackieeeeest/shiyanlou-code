i = 0
while i < 100:
	i += 1
	if i % 7 == 0 or '7' in str(i):
		continue
	print(i)
