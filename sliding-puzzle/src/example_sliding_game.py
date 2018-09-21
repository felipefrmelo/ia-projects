from resources import functions as f
from resources.Game import Game

# start_state = f.get_start_state() # GUI para pegar os dados do usuário
start_state = ('1', '2', '3', '4', '5', '6', '7', '8', '_') # Hard Code temporally : Já é o objetivo
f.print_game(start_state)

print(f.get_empty_space(start_state)) # Retorna o espaço vazio: sera usado na criaçao do primiiro no

# Inicializaçâo de um nó
start_node = Game(start_state, f.get_empty_space(start_state), None, 'Start', 0, 0)
print(start_node)
print(start_node.test_target())

# listando açoes possiveis : Sera o  ['left','right','clenar'] desse exercicio
list_possible = start_node.list_actions() # Retorna lista de indexcei que dá para trocar
print(list_possible) # Retorna lista

next_node = start_node.execute_action(5)
print(next_node)
print(next_node, next_node.test_target())
print(next_node.empty_index, next_node.hash_value, )


next_next_node = next_node.execute_action(2)
print(next_next_node)
print(next_next_node.empty_index, next_next_node.hash_value)
#next_node = start_node()