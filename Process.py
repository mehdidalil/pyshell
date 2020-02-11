class Process():
	def __init__(self, args):
		self.args = args
	
	def run(self):
		raise(NotImplementedError)