def checkOptions(options, optionList):
	optionsTmp = []
	options = set(options)
	for i in options:
		if i in optionList:
			optionsTmp.append(i)
		else:
			raise Exception("Option does not exist: {}".format(i))
	return optionsTmp
	
def parseOptions(args, optionList):
	options = []
	garbage = []
	index = 0
	for i in args:
		if i.startswith("-"):
			try:
				options.extend(checkOptions(i[1:], optionList))
				garbage.append(i)
			except Exception as e:
				pass
		else:
			break
	for i in garbage:
		args.remove(i)
	return options