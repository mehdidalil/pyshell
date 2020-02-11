from Exec import Exec
from Builtin import Builtin

def parseLine(line):
	line = line.split()
	proc = Builtin(line)
	ret = proc.run()
	if ret == None:
		proc = Exec(line)
		ret = proc.run()