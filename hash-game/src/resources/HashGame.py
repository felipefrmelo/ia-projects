# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2

""""
|X| |O|
| |O| |
|X| |X|


"""

# |0|1|2| | | |
# |3|4|5| | | |
# |6|7|8| | | |
# Indexs 

# Possibilidades: 8 POSSIBILIDADES

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
	state = ('X', 'O') # 9 [0, 8 em index]
	range_index = [0,1,2,3,4,5,6,7,8]
	x = None
	goal_state = {
		0: ['']
		4:
		8:
	}


	# 8 formas de terminar: 3 casas: 2 simbolos = 42 ifs
	# Se fazer considerando o jogador: se o ultimo mov, ele venceu: entao: 24
	goal_end = {
		'h_up': [0,1,2]
		'h_mi': [3,4,5]
		'h_dw': [6,7,8]
		'v_le': [0,3,6]
		'v_ce': [1,4,7]
		'v_ri': [2,5,8]
		'd_dw': [0,4,8]
		'd_up': [6,4,2]
	}

# |0|1|2| | | |
# |3|4|5| | | |
# |6|7|8| | | |
# Indexs 

# |X| |O|
# | |O| |
# |X| |X|

# Pior cenario
# | |X| |
# |0| |0|
# |X| |X|






	# Quando vocÊr chega, na 5 casa, onde é possivel termianr: por conta das outras 2 no minimo
	# que seu opnetne colocu 2: entâo, você tem no minimo 2 possibildade até 5 a menos por conta dele
	block_state {
		0: ['h_up', 'v_le', 'd_dw'], 
		1: ['h_up', 'v_ce'],
		2: ['h_up', 'v_ri', 'd_up'],
		3: ['h_ce', 'v_le'],
		4: ['h_ce', 'v_ce', 'd_dw', 'd_up'], 
		5: ['h_ce', 'v_ri'],
		6: ['h_dw', 'v_le', 'd_up'],
		7: ['h_dw', 'v_ce'],
		8: ['h_dw', 'v_ri', 'd_dw'], 
	}


"""

	Criar um dicionario com as 8 possibilidades:
		Cada um inicializa com 0
		+ Se max coloca, ganha +1 onde pode dar certo
		+ se min coloca, diminui
		+ Verifica se: a ultima atribuiçao de simbolo, der 3: entao, terminou
"""


	count_goal = {
		'h_up': 0,
		'h_mi': 0,
		'h_dw': 0,
		'v_le': 0,
		'v_ce': 0,
		'v_ri': 0,
		'd_dw': 0,
		'd_up': 0,
	}






	# Constructor
	def __init__(self, state, empty_indexs, level, count_goal, goal_state_ending):
		self.state = state 	 							# Tupla do estado
		self.origin	= origin 							#
		self.empty_indexs = empty_indexs    			# Lista de açoes possiveis, a cada açao, sai uma
		self.level = level                              # Nível do jgo: a partir do 5 pode-se ter o fim de jogo (3 jogada de Max)
		self.count_goal = count_goal                    # Dic de estao onde se conta o quao perto está de chegar: se 3 ou -3, venceu
		self.goal_state_ending = goal_state_ending      # Estado que chegou em 3, assim, o teste objetivo sera uma unica verificacao

	# Teste Objetivo:
	# Apesar de o livro colocar ele como neutro, fica mais interrestane se colocarsmo: Se MAX ganhou| Se Min ganhoru
	# Por que aí, veer suas açôes fica mais fácil
	def test_goal(self, symbol):
		if(self.level < 5):
			return False
		elif(self.level != 9):


	def analysis_block_state(self):



		


	"""
Esturtura desse Problema

S0 = Estado inicial, o tabuleiro Vazio (' ') 						(X)
JOGAROES() : 2 jogares, Max e Min 									(X)
AÇOES(s): Possiveis açoes, vem de list_action do Estado 			(X)
RESULTADO(s,a): é o eaxecte_action, retorna umnovo estado 			(X)
TESTE DE TERMINO(s)) : verifica se terminou ou nao
UTILIDADE(s,j: Quem ganhou, +1 para Max ou -1 para mIN ou empate????


"""



	# def insert_symbol(self, selected_index, symbol):
	# 	new_state = copy(self.state)[]
	# 	new_state[selected_index] = symbol
	# 	return new_state

	def action(self, selected_index, symbol):
		# Insert Symbol
		new_state = copy(self.state)
		new_state[selected_index] = symbol
		# Novo array de ações possíveis
		new_empty_indexs = copy(self.empty_indexs)
		del empty_indexs[selected_index]
		# Novo count_goal
		new_goal_state = copy(self.count_goal)
		for key_goal_state in block_state[selected_index]:
			new_goal_state[key_goal_state] += 1
		return HashGame(new_state, new_empty_indexs, origin,  self.level + 1)

	## Retorna Indexes de espaços vazios possíveis # Tira no final pois pode ser uma alternativa
	# def list_of_actions(self):
	# 	actions = []
	# 	for index in HashGame.range_index():
	# 		if(self.state[index] == ' '):
	# 			actions.append(index)
	# 	return actions


	"""
	block_state {
		0: ['h_up', 'v_le', 'd_dw'], 
		1: ['h_up', 'v_ce'],
		2: ['h_up', 'v_ri', 'd_up'],
		3: ['h_ce', 'v_le'],
		4: ['h_ce', 'v_ce', 'd_dw', 'd_up'], 
		5: ['h_ce', 'v_ri'],
		6: ['h_dw', 'v_le', 'd_up'],
		7: ['h_dw', 'v_ce'],
		8: ['h_dw', 'v_ri', 'd_dw'], 
	}

	"""

	# Hash-Game em forma de String
	def __str__(self):
		str_output = '\t'
		for index in HashGame.range_index:
			str_output += '|' + self.state[index]
			if( (index + 1) % 3 == 0 ):
				str_output += '|\n\t'
		return str_output





