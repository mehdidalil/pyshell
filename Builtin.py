import sys
from Process import Process
from setenv import setenv
from unsetenv import unsetenv
from echo import echo
from exit import exit
from env import env
from cd import cd
from tictactoe import tictactoe

class Builtin(Process):
	list = {
		"setenv": setenv,
		"unsetenv": unsetenv,
		"echo": echo,
		"exit": exit,
		"env": env,
		"tictactoe": tictactoe,
		"cd": cd
		}

	def __init__(self, args):
		super().__init__(args)

	def run(self):
		ret = 0
		if self.args[0] not in self.list:
			return None
		try:
			ret = self.list[self.args[0]](self.args[1:])
		except SystemExit as e:
			sys.exit(e)
		except Exception as e:
			print(f'{self.args[0]}: {e}')
			ret = 1
		return ret
