# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2

# |0|1|2|
# |3|4|5|
# |6|7|8|
# Indexs 

##### Como testar estado objetivo de forma Ultra Eficiente
##### No Maximo 9 Jogadas:
### 1º Jogador: 5 números
### 2º Jogador: 4 Números
### A partir da 5 jogada (3 do 1 jodador) é capaz de terminar
### Se chegar na 9 rodada, pode dar empate
# Horizontal: 012, 345, 678
# Vertical  : 036, 147, 258
# Diagonal  : 048, 246

# Iterar para cada possiblidade de forma

class HashGame:

	# X, O, ' '
	state = ('X', 'O') # 9 [0, 8 em idice]
	range_index = [0,1,2,3,4,5,6,7,8]
	x = None
	goal_state = {
		0: ['']
	}

	# Constructor
	def __init__(self):
		#

	def list_of_actions(self):
		actions = []
		for index in HashGame.range_index():
			if(self.state[index] == None):
				actions.append(index)
		return actions

	# O mais imporatne, como avalair os estados de forma eficeinete
	# Hash-Game
	def __str__(self):
		str_output = '\t'
		for index in HashGame.range_index:
			str_output += '|' + self.state[index]
			if( (index + 1) % 3 == 0 ):
				str_output += '|\n\t'
		return str_output





