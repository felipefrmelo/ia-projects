# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2

class Player:

	is_max = True

	def __init__(self, symbol):
		self.symbol = symbol
		if(Player.is_max):
			self.player = 'MAX'
		else:
			self.player = 'MIN'