import os
import sys

class Board():
	positions = [7, 8, 9, 4, 5, 6, 1, 2 ,3]

	def __init__(self):
		self.pieces = [" " for i in range(0, 9)]

	def display(self):
		if os.getenv("TERM"):
			os.system("clear")
		for i in range(len(self.pieces)):
			if i % 3 == 0:
				sys.stdout.write("\n-----------------\n")
			sys.stdout.write("| {} | ".format(self.pieces[i]))
		sys.stdout.write("\n-----------------\n")

	def addPiece(self, piece, pos):
		if pos > 9 or pos < 1:
			return False
		index = self.positions.index(pos)
		if self.pieces[index] != " ":
			return False
		self.pieces[index] = piece
		return True

	def checkWin(self, symbol):
		for i in range(0, 8, 3):
			if self.pieces[i] == self.pieces[i + 1] == self.pieces[i + 2] == symbol:
				return True
		for i in range(0, 3):
			if self.pieces[i] == self.pieces[i + 3] == self.pieces[i + 6] == symbol:
				return True
		if self.pieces[0] == self.pieces[4] == self.pieces[8] == symbol:
			return True
		if self.pieces[2] == self.pieces[4] == self.pieces[6] == symbol:
			return True
		return False