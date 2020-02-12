def exit(args):
	ret = 0
	if len(args) > 1:
		raise Exception("Too many arguments")
	try:
		if len(args) == 1:
			ret = int(args[0])
	except:
		print("Argument is not an int")
		return 1
	raise SystemExit(ret)
	return 0