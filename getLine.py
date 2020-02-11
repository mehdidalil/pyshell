def getLine(prompt):
	while True:
		line = input(prompt)
		if line.strip() == "":
			pass
		else:
			break
	return line