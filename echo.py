import sys
from parseArgs import parseArgs

def echo(args):
	options, args = parseArgs(args, "ne")
	str = ' '.join(args)
	str = str + '' if 'n' in options else str + '\n'
	sys.stdout.write(str)
	return 0