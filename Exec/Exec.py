import subprocess
import os
from Process import Process

class Exec(Process):

	def __init__(self, args):
		super().__init__(args)

	def run(self, env=os.environ):
		try:
			ret = subprocess.call(self.args, env=env)
		except:
			print(f'{self.args[0]}: Command not found')
			return 1
		return ret
