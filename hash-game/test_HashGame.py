from resources.HashGame import HashGame
from resources.Player import *
import time


moves=[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

node=HashGame({},None,0,moves,0,'X')

for func in [minimax_player,alfabeta_player]:
    print()
    print(func.__name__)
    start = time.time()
    node.play_game(func)
    end = time.time()
    tempo_total=end-start
    print('Total de nos gerados {0}\nTempo {1:.4} s'.format(count_nodes[func.__name__.split('_')[0]],tempo_total))




def jogo():
    
    jogadores=[h_player,minimax_player,alfabeta_player,random_player]
    j=[]
    str_jg='\n0 : h_player\n1 : minmax_player\n2 : alfabeta_player\n3 : random_player\n' 
    for i in range(1,3):
        j.append(int(input('Escolha o jogador '+str(i)+str_jg)))

    print('Jogador 1 : ' +jogadores[j[0]].__name__,
          '\nJogador 2 : '+jogadores[j[1]].__name__,
          '\n\tStart')
    node.play_game(jogadores[j[0]],jogadores[j[1]])


    

