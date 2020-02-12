import sys
from .parseOptions import parseOptions

optionList = "ne"

def echo(args):
	options = parseOptions(args, optionList)
	str = ' '.join(args)
	str = str + '' if 'n' in options else str + '\n'
	sys.stdout.write(str)
	return 0