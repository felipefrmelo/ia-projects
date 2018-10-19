from resources.HashGame import HashGame

start_state = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
start_count_goal = [0, 0, 0, 0, 0, 0, 0, 0]

# Pode COMENTAR TO O BLOCO ENTRE OS CONJUNTOS DE ####### para escolher só um para executar
# Como a parte de EMPTARE

#####################################

print('\n\nINICIO DE PARTIDA')

start_state = (	'X', 'O', 'X', 
				'X', 'O', 'O',
				'O', 'X', 'X')
start_empty_indexs = "012345678"

start_node = HashGame(start_state, None, 0,
 start_empty_indexs, start_count_goal, False, 'Start')

print(start_node)
print(start_node.statistics())

next_node = start_node.action(4, 'X')
print(next_node)
print(next_node.statistics())

next2_node = next_node.action(5, 'O')
print(next2_node)
print(next2_node.statistics())

#####################################

# print('\n\nEMPATE')
# start_state_2 = ('X', 'O', 'X', 
# 				 'X', 'O', 'O', 
# 				 'O', ' ', 'X')
# start_empty_indexs_2 = '7'

# # Perceba que o nivel já começa em 8, se nao começar ssim (pu seja, se nao for um csaso real) nao vai detectar endgame
# start_node_2 = HashGame(start_state_2, None, 8,
# 	start_empty_indexs_2, start_count_goal, False, 'Start')

# # Calcular count_goal no meio da partida (sera uytil para quando jogar contra a maquina)
# start_node_2.count_goal = start_node_2.auto_update_count_goal()
# print(start_node_2, '\n', start_node_2.statistics())

# next_node_2 = start_node_2.action(7,'X')
# print(next_node_2, '\n', next_node_2.statistics())

# # Empate: O JOGO TERMINOU  MAS UTILIDADE É 0
# print('Chegou ao Fim?:', next_node_2.test_end())
# print('Quem ganhou?:', next_node_2.utilidade())

#####################################

print('\n\nVITORIA')
start_state_3 = ('X', 'O', 'X', 
				 'X', 'X', 'O', 
				 'O', 'O', ' ')
start_empty_indexs_3 = '8'

start_node_3 = HashGame(start_state_3, None, 0,
	start_empty_indexs_3, start_count_goal, False, 'Start')

start_node_3.count_goal = start_node_3.auto_update_count_goal()
print(start_node_3, '\n', start_node_3.statistics())

next_node_3 = start_node_3.action(8, 'X')
print(next_node_3, '\n', next_node_3.statistics())

# Verficando vitoria (1 => Max Ganhou, -1)
print('Chegou ao Fim?', next_node_3.test_end())
print('Quem ganhou?:', next_node_3.utilidade())

# printando no final: print de forma recursiva
next_node_3.print_all_hashgame()
