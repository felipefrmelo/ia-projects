# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2
import copy

class HashGame:

	# Mapea posicao de incremento de goal
	block_state_goal =  {
		0: [0, 3, 6], 1: [0, 4]      , 2: [0, 5, 7],
		3: [1, 3]   , 4: [1, 4, 6, 7], 5: [1, 5],
		6: [2, 3, 7], 7: [2, 4]      , 8: [2, 5, 6]
	}

	# É definido por CONVEÇÃO que:
	# X = MAX = +3
	# O = MIN = -3

	# Constructor
	def __init__(self, state, origin, level, empty_indexs, count_goal, tag_end, move):
		self.state        = state 	 		# Tupla do estado ('X', 'O', ' ')
		self.origin	      = origin 			# Link para o pai
		self.level        = level           # Nível do jgo: a partir do 5 pode-se ter o fim de jogo (3 jogada de Max)
		self.empty_indexs = empty_indexs    # String com cada char '01234567' onde, a medida da cada açao, sai um deese numeros INICIAL: '01234567'
		self.count_goal   = count_goal      # lista de estao onde se conta o quao perto está de chegar: se 3 ou -3, venceu [0,0,0,0,0], [-1,-2,+3]
		self.tag_end	  = tag_end         # Quando detectar +3 ou -3, termina
		self.move		  = move			# Tupla (index => Symbol)

	# Teste Objetivo:
	# Retorna True ou False se terminou: Quando chegar no level 9 e nao tiver terminada, entao será empate
	def test_end(self):
		if(self.level == 9 and not self.tag_end):
			return True
		else:
			return self.tag_end

	# Retorna +1,0,-1 indicando quem ganhou ou se deu empate
	# Empate será quando level=9 e tag ser falso. Max/Min ganaha se tiver +3/-3 em um dos count_goal
	def utilidade(self):
		if(self.level == 9 and not self.tag_end):
			return 0
		# Testa count_goal
		for count_goal_line in self.count_goal:
			if(count_goal_line == 3):
				return 1
			elif(count_goal_line == -3):
				return -1
		return 0

	# Retorna o count_goal do stado atual
	# Usado para atuzliar o count_goal de acordo com o stado atual, 
	# pois o procesos é feito de forma incremental a cada jogada
	# talvez nao será usado
	def auto_update_count_goal(self):
		new_count_goal = [0,0,0,0,0,0,0,0,0]
		for (key, value) in enumerate(self.state):
			if(value == 'X'):
				for index in HashGame.block_state_goal[key]:
					new_count_goal[index] += 1
			elif(value == 'O'):
				for index in HashGame.block_state_goal[key]:
					new_count_goal[index] -= 1
		return new_count_goal

	# Seleciona index e Symbolos (Nao faz verificaçao de quadrado válido)
	def action(self, selected_index, symbol):
		new_tag = False
		increment = 1 if symbol == 'X' else -1
		# Insert Symbol
		new_state = list(self.state)
		new_state[selected_index] = symbol
		new_state = tuple(new_state)
		# Novo array de ações possíveis: tira um char da String
		new_empty_indexs = copy.copy(self.empty_indexs)
		new_empty_indexs = new_empty_indexs.replace(str(selected_index), '')
		# Novo count_goal
		new_count_goal = self.count_goal.copy()
		for key_count_goal in HashGame.block_state_goal[selected_index]:
			new_count_goal[key_count_goal] += increment
			if(abs(new_count_goal[key_count_goal]) == 3):
				new_tag = True # Terimnou com ganhador
		# Retorna novo no do HashGAME
		return HashGame(new_state, self, self.level + 1, new_empty_indexs, new_count_goal, new_tag, (selected_index, symbol))

	## Retorna Indexes de espaços vazios possíveis # Tira no final pois pode ser uma alternativa
	# Retornar uma String, que é possivel iterar da mesma forma que uma lista
	def list_of_actions(self):
		return self.empty_indexs

	# Hash-Game em forma de String em Jogo da Velha
	def __str__(self):
		str_output = '\n\t'
		for index in range(9):
			str_output += '|' + self.state[index]
			if( (index + 1) % 3 == 0 ):
				str_output += '|\n\t'
		aux = ' '+self.move if self.move == 'Start' else str(self.move[0]) + ' ==> ' + self.move[1]
		str_output += aux
		return str_output + '\n'

	# Retorna String de dados do obejto (No futuro pode fazer parte do __str__)
	def statistics(self):
		output  = 'Index possiveis de Colocar: ' + self.empty_indexs + ' len: ' + str(len(self.empty_indexs)) + '\n'
		output += 'Contagem ate Vitoria/Derrota: ' + ''.join(str(e) for e in self.count_goal) + '\n'
		output += 'Profundidade: ' + str(self.level) 
		output += '| Test End: ' + str(self.test_end()) + '| Utilidade: ' + str(self.utilidade()) + ' | '
		aux = self.move if self.move == 'Start' else str(self.move[0]) + ' ==> ' + self.move[1]
		output += aux
		return output + '\n'

	# Print de forma recursiva
	def print_all_hashgame(self):
		if(self.origin is None):
			print(self)
		else:
			self.origin.print_all_hashgame()
			print(self)
		return