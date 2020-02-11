import subprocess
from Process import Process

class Exec(Process):

	def __init__(self, args):
		super().__init__(args)
	def run(self):
		try:
			ret = subprocess.call(self.args)
		except:
			print("program not found")
			return 1
		return ret
