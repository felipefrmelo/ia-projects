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
	target_state = ('1','2','3','4','5','6','7','8','_') # Estado Objetivo
	possible_actions = {
		'0': [1,3],
		'1': [0,2,4],
		'2': [1,5],
		'3': [0,4,6],
		'4': [1,5,7,3],
		'5': [2,8,4],
		'6': [3,7],
		'7': [6,4,8],
		'8': [5,7]
	}

	# Constructor
	def __init__(self, state, empty_index, origin, action, level, cost):
		self.state		 = state		# Tupla de string = (_,1,2,3,4,5,6,7,8) lenght = 9
		self.empty_index = empty_index	# indice do espçao vazio. Serve Para nao busca a todo momento essa posicao
		self.origin		 = origin		# Ponteiro para o pai
		self.action 	 = action		# tupla (peça escolhida, blanck_space) 
		self.level		 = level		# Profundidade
		self.cost		 = cost			# Custo
		self.hash_value  = self.generate_hash(state)	# hash para depois verificar nos nos explorados para nao repetir
		#self.heuristica	 				# Implementado em cada caso, criar uma funçâo apra cada caso

	# Testa se chegou ao objetivo
	# * Etapa pode ser aprimorada caso o progrma estiver lento
	def test_target(self):
		return self.state == Game.target_state

	# Serve para retornar um endereço hash a ser colocado num dicionario
	# Serve para: Quando formos consultar se um estado já foi exploradp
	# Ai, vamos lve se essa funçâo hash está no dicitonario
	# Dessa forma, tem O(1) para buscar, colocar e deletar num DICIONARYO
	##### Será útil para não repetir estados
	def generate_hash(self, tuple_state):
		hash_key = ''
		for number in tuple_state:
			hash_key += number
		return hash_key

	# usado no inicio, para nao presisar buscar a toda hora
	# retorna o index de onde está a posiçao vazia
	def search_empty_space(self):
		for position in self.state:
			if(postion == 0):
				return position
		return None

	# Retorna lista de possiveis indices que podem ir para a posicao vazia
	# Ou seja, retorna as ações possíveis com base no espaço vazio
	# Pode ser: 1. Baeada em valores fixos ou 2. Calcular a toda hora, para otimizar, é bom criar essa
	# estrutura fixa de inicio para nao fazer toda hora esse mapeamento
	def list_actions(self):
		return Game.possible_actions[str(self.empty_index)]

	# Executa a açao de acordo com o indexe passado. Vai ser feita de forma a so receber valores possiveis
	# desde que você use list_actions antes: Assim, se vc fizer o 'for' nele, so vai açoes fisicamente possiveis
	def execute_action(self, index_choised):
		# faz a troca
		return Game( self.swap_pieces(index_choised), index_choised, self, 
			(self.state[index_choised], self.state[self.empty_index]), self.level + 1, self.cost + 1)

	# Retorna a tupla state com os elementos trocados
	def swap_pieces(self, index_choised):
		state_list = list(self.state)
		# Deixa asism, no final, troca só por '_' pois sempre vai ser isso
		empty_value = state_list[self.empty_index] # elemento que esta no espaço vazio
		# swap
		state_list[self.empty_index] = state_list[index_choised]
		state_list[index_choised] = empty_value
		return tuple(state_list)

	# String a ser printada quando der um print no objeto
	def __str__(self):
		output = ''
		k = 0
		for i in range(3):
			output += '\t|' 
			for j in range(3):
				output += self.state[j+k] + '|'
			k += 3
			output += '\n'
		output += 'Action: ' + str(self.action) + '| Heuristica: ' #+ str(heuristica) 
		output += '| Level: ' + str(self.level)
		return output