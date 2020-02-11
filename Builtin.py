import sys
from Process import Process
from setenv import setenv
from unsetenv import unsetenv
from echo import echo
from exit import exit
from env import env
from tictactoe import tictactoe

class Builtin(Process):
	list = {"setenv": setenv, "unsetenv": unsetenv, "echo": echo, "exit": exit, "env": env, "tictactoe": tictactoe}

	def __init__(self, args):
		super().__init__(args)

	def run(self):
		ret = 0
		try:
			ret = self.list[self.args[0]](self.args[1:])
		except SystemExit as e:
			sys.exit(e)
		except:
			return None
		return ret
