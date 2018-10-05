from resources import functions as f
from resources.Game import Game
import queue as Q

priority_border = Q.PriorityQueue()
explorateds_states = {}

# start_state = f.get_start_state()
# start_state = ('5', '8', '7', '6', '_', '4', '3', '2', '1') # HardCode
#start_state = ('5', '8', '7', '6', '4', '_', '3', '2', '1') # HardCode
#start_state = ('1','2','3','4','5','6','7','_','8') 
#start_state = ('5', '8', '3', '6', '4', '_', '7', '2', '1') # HardCode	# Funciona
start_state = ('7', '2', '4', '5', '_', '6', '8', '3', '1')				# Funciona
count_nodes = 0

node = Game(start_state, f.get_empty_space(start_state), None, 'Start', 0, 0)
priority_border.put(node)

while True:
	# Borda Vazia
	if(priority_border.empty()):
		print('\n\tBorda Vazia: Nao encontrou sequencia\n')
		break
	node = priority_border.get()
	# Encontrou
	if(node.test_goal()):
		print('\n\tEncontrou Estado Objetivo\n')
		print(node.print_game_recursive())
		break
	# Executando as ações
	for action in node.list_actions():
		count_nodes += 1
		son = node.execute_action(action)
		try:
			bool(explorateds_states[son.generate_hash()])
		except:
			priority_border.put(son)
	explorateds_states[node.generate_hash()] = True

print('Count Nodes', count_nodes)

