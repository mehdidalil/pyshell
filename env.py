import os
import sys
from Exec import Exec
from parseOptions import parseOptions

optionList = "i"

def parseEnvExec(args):
	newEnv = {}
	garbage = []
	for i in args:
		if '=' in i:
			garbage.append(i)
			t = i.split('=')
			newEnv[t[0] if t[0] else ""] = t[1] if t[1] else ""
		else:
			break
	for i in garbage:
		args.remove(i)
	return newEnv

def env(args):
	options = parseOptions(args, optionList)
	envTmp = parseEnvExec(args)
	newEnv = {} if "i" in options else os.environ.copy()
	newEnv.update(envTmp)
	if not args:
		for key in newEnv:
			sys.stdout.write(f'{key}={newEnv[key]}\n')
	else:
		proc = Exec(args)
		proc.run(newEnv)
	return 0