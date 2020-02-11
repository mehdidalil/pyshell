class Player():
	instance = []
	def create(self, name, symbol):
		if len(name) < 32 and len(name) >= 2 and name.isalnum():
			self.name = name
		else:
			raise Exception("Name not valid !")
		if len(symbol) <= 1 and len(symbol) > 0 and name.isalnum():
			for player in self.instance:
				if player.symbol == symbol:
					raise Exception("Symbol already existing !") 
			self.symbol = symbol
		else:
			raise Exception("Symbol not valid")
		Player.instance.append(self)

	def prompt(self, prompt):
		while True:
			try:
				name = input("{}, please enter your name (between 2 and 32 characters): ".format(prompt))
				symbol = input("Choose your symbol (1 character only): ")
				self.create(name, symbol)
			except Exception as e:
				print(e)
			else:
				break
		