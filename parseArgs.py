def checkOptions(options, optionList):
	optionsTmp = []
	options = set(options)
	for i in options:
		if i in optionList:
			optionsTmp.append(i)
		else:
			raise Exception("Option does not exist: {}".format(i))
	return optionsTmp
	
def parseArgs(args, optionList):
	options = []
	index = 0
	for i in args:
		if i.startswith("-"):
			try:
				options.extend(checkOptions(i[1:], optionList))
				index += 1
			except Exception as e:
				pass
		else:
			break
	args = args[index:]
	return (options, args)