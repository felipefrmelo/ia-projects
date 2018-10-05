# Grupo: Rafael Asis e Felipe - IA UFU 2018-2
"""
	Definição de Estado Objetivo:
	|1|2|3|		|0|1|2|		|_|8|7|
	|4|5|6|		|3|4|5|		|6|5|4|
	|7|8|_|		|6|7|8|		|3|2|1|
	Objetivo    Indices     Exemplo Inicial

# Dados Experimentais dados por Márcia
	+ Media de 22 passo para chegar
	+ No maximo 26

# Links que podem ser úteis
	https://wiki.python.org/moin/TimeComplexity
	+ Dicionario tem O(1) em media para colocar

# Lembre-se:
	+ Se ficar muito lento, alguma etapa terá que ser modificada para ser O(1) ou no máximo O(nlogn)
		principlamenta na parte das Estruturas de Dados que estiverem usando na execução
		e em algumas funções internas

"""
class Game:
	
	# empty_symbol = '_'

	# Estado Objetivo
	goal_state = ('1','2','3','4','5','6','7','8','_') 

	# Mapeamento de ações posspiveis de acordo com o empty_space
	possible_actions = {
		'0': [1,3],   '1': [0,2,4],   '2': [1,5],
		'3': [0,4,6], '4': [1,5,7,3], '5': [2,8,4],
		'6': [3,7],   '7': [6,4,8],   '8': [5,7]
	}
	# Variaveis Uteis para o calculo de H2
	mapping_vertical = {
			'0': 1, '1': 2, '2': 3,
			'3': 1, '4': 2, '5': 3,
			'6': 1, '7': 2, '8': 3
		} #
	mapping_horizontal = {
		'0': 1, '1': 1, '2': 1,
		'3': 2, '4': 2, '5': 2,
		'6': 3, '7': 3, '8': 3
	}
	# As 'mapping_goal' são dependentes do que for o estado objetivo # Add: gerar para qualquer estado
	mapping_goal_vertical = {
		'1': 1, '2': 2, '3': 3,
		'4': 1, '5': 2, '6': 3,
		'7': 1, '8': 2
	}
	#
	mapping_goal_horizontal = {
		'1': 1, '2': 1, '3': 1,
		'4': 2, '5': 2, '6': 2,
		'7': 3, '8': 3
	}

	# Constructor
	def __init__(self, state, empty_index, origin, action, level, cost):
		self.state		 = state		# Tupla de string = (_,1,2,3,4,5,6,7,8) lenght = 9
		self.empty_index = empty_index	# indice do espçao vazio. Serve Para nao busca a todo momento essa posicao
		self.origin		 = origin		# Ponteiro para o pai
		self.action 	 = action		# tupla (peça escolhida, blanck_space) 
		self.level		 = level		# Profundidade
		self.cost		 = cost			# Custo
		# self.hash_value  = self.generate_hash(state)	# hash para depois verificar nos nos explorados para nao repetir
		self.heuristica	 = self.heuristica2() + cost	# Implementado em cada caso, criar uma funçâo apra cada caso

	# Testa se chegou ao objetivo
	# * Etapa pode ser aprimorada caso o programa estiver lento
	def test_goal(self):
		# print(self.state)
		# print(Game.goal_state)
		return self.state == Game.goal_state

	# Serve para retornar um endereço hash a ser colocado num dicionario
	# Serve para: consultar se um estado já foi explorado
	# Ai, vamos lve se essa funçâo hash está no dicitonario
	# Dessa forma, tem O(1) para buscar, colocar e deletar num DICIONARYO
	##### Será útil para não repetir estados
	def generate_hash(self):
		hash_key = ''
		for number in self.state:
			hash_key += number
		return hash_key

	# Usado no inicio, para nao presisar buscar a toda hora
	# retorna o index de onde está a posiçao vazia
	def search_empty_space(self):
		for position in self.state:
			if(postion == 0):
				return position
		return None

	# Retorna lista de possiveis indices que podem ir para a posicao vazia
	# 	Ou seja, retorna as ações possíveis com base no espaço vazio
	#	OBS: Mantemos empty_index para faciliatar a encontra-lo
	def list_actions(self):
		return Game.possible_actions[str(self.empty_index)]

	# Executa a açao de acordo com o indexe passado. Vai ser feita de forma a so receber valores possiveis
	# desde que você use list_actions antes: Assim, se vc fizer o 'for' nele, so vai açoes fisicamente possiveis
	def execute_action(self, index_choised):
		# faz a troca das peças
		return Game( self.swap_pieces(index_choised), index_choised, self, 
			(self.state[index_choised], self.state[self.empty_index]), self.level + 1, self.cost + 1)

	# Retorna a tupla state com a posição escolhida pela posiçâo vazia
	#	Utilizando da forma certa,nâo tem como fazer uma ação impossível
	def swap_pieces(self, index_choised):
		state_list = list(self.state)			   # Copia do state atual, pois s´vai mudar dois elementos
		empty_value = state_list[self.empty_index] # elemento que esta no espaço vazio
		# swap
		state_list[self.empty_index] = state_list[index_choised]
		state_list[index_choised] = empty_value
		return tuple(state_list)

	# String a ser printada quando der um print no objeto Game
	def __str__(self):
		output = ''
		k = 0
		if(self.action == 'Start'):
			output += 'Action: ' + self.action
		else:
			output += 'Action: ' + str(self.action[0]) + ' => '+ str(self.action[1])
		output += ' | H: ' + str(self.heuristica)  + ' | Level: ' + str(self.level) + '\n\n'
		for i in range(3):
			output += '\t|' 
			for j in range(3):
				output += self.state[j+k] + '|'
			k += 3
			output += '\n'
		return output

	# Comparando para a Lista de Prioridade
	def __cmp__(self, other_node):
		return cmp(self.heuristica, other_node.heuristica2)

	def __lt__(self, other):
	    return self.heuristica < other.heuristica

	# Heurística pela Distância de Manhatan
	# 1. É feita a partir dos dicionários de 'mapping' que são variáveis staticas (compartilhada pelos objetos)
	# 2. Calculamos a distancia entre onde o número está e onde deveria está de forma na vertical e na horizontal
	# 3. A soma dessas distâncias (módulo) resulta no valor para o número
	# 4. Se já estiver no local, a soma dá Zero
	# Exemplo:
	#	Inicial		Objetivo
	#	|5|8|7|		|1|2|3|
	#	|6|_|4|		|4|5|6|
	#	|3|2|1|		|7|8|_|
	# 1. Vai ler a tupla (5,8,7,6,_,4,3,2,1); 
	# 2. Pelo 1° mapping para vert/horizon vai lê qual o valor dessa posição (1,2,3)
	# 3. pelo 2° mapping para goal vai lê a posiçâo que deveria está
	# 4. É feito a diferença em módulo, dano a distancia vertical ou horizonal
	# 5. A soma das distâncias horizonal e vertical dá distância do número, então, basta um s
	# 		basta um somátoria para todas as posiçôes (execto '_') que temos a heurística H2
	def heuristica2(self):
		sum_manhattan = 0
		for index in ['0','1','2','3','4','5','6','7','8']:
			if(int(index) == self.empty_index):
				continue
			result = abs( 
				abs( Game.mapping_horizontal[index] - Game.mapping_goal_horizontal[self.state[int(index)]]  ) 
				+
				abs( Game.mapping_vertical[index]   - Game.mapping_goal_vertical[self.state[int(index)]]  ) 
			)
			# print('Numero', self.state[int(index)], 'No indice', index, 'dist_mh', result) # print para conferir
			sum_manhattan += result
		# print('h final:', sum_manhattan)
		return sum_manhattan

	# Encapsula e inicializa a lista de retorno de sequencias de ações feito no final
	def sequence_of_actions(self):
		return self.recursive_return([], self.level, self.cost)

	# retorno recursivo para retornar lista de açoes/estados, level e custo
	# Eh necessário executar reverse() após a saida para está na ordem
	def recursive_return(self, array_state_actions, level, cost):
		array_state_actions.append(
			{
				'state' : self.state, 
				'action': self.action,
				'heuristica': self.heuristica
			}
		)
		return_data = {'state_sequence': array_state_actions, 'level': level, 'cost': cost}
		if(self.origin is None):
			return return_data
		self.origin.recursive_return(array_state_actions, level, cost)
		return return_data

	# printa jogo, 
	def print_game_recursive(self):
		if(self.origin is None):
			print(self)
			return
		else:
			self.origin.print_game_recursive()
			print(self)
			return