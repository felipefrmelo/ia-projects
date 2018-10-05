# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2

from resources import functions as f
from resources.Game import Game
import queue as Q

priority_border = Q.PriorityQueue()	# Fila de prioridade por f(n)
explorateds_states = {}				# Dicionario de estados explorados: Funciona como Hash

# start_state = f.get_start_state()	# Insere estado inicial manualmente

## HardCode que funciona
#start_state = ('5', '8', '3', '6', '4', '_', '7', '2', '1') # HardCode	# Funciona

start_state = ('7', '2', '4', '5', '_', '6', '8', '3', '1')				# Funciona

count_nodes = 0

node = Game(start_state, f.get_empty_space(start_state), None, 'Start', 0, 0)
priority_border.put(node)

while True:
	# Flha: Borda Vazia
	if(priority_border.empty()):
		print('\n\tBorda Vazia: Nao encontrou sequencia\n')
		break
	node = priority_border.get()
	# Encontrou estado objetivo
	if(node.test_goal()):
		print('\n\tEncontrou Estado Objetivo\n')
		node.print_game_recursive()
		break
	# Executando as ações possíveis
	for action in node.list_actions():
		count_nodes += 1
		son = node.execute_action(action)
		try:
			# Verifica se existe esse estado no explorateds_states
			bool(explorateds_states[son.generate_hash()])
		except:
			# Se não existir esse estado, insere em explorados, se não, não insere
			priority_border.put(son)
	explorateds_states[node.generate_hash()] = True # Poê em explorateds_states

print('Count Nodes:', count_nodes)