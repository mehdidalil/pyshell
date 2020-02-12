import sys
import os
from .Player import Player
from .Board import Board

def game(board, players):
	win = False
	while not win:
		for player in players:
			board.display()
			valid = False
			while not valid:
				move = int(input("\nYour move, {}: ".format(player.name)))
				valid = board.addPiece(player.symbol, move)
			win = board.checkWin(player.symbol)
			lastPlayer = player
			if win:
				break ;
	else:
		board.display()
		print("\n{} won !!\n".format(lastPlayer.name))

def tictactoe(args):
	board = Board()
	players = [Player(), Player()]
	players[0].prompt("Player One")
	players[1].prompt("Player Two")
	game(board, players)
	return 0

if __name__ == "__main__":
	tictactoe()