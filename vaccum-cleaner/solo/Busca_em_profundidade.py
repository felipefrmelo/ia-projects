from resource import functions as f
from resource.Node import Node

acoes = ['left','right','clean']
count_nodes = 0

### Escolhendo o estado inicial
start_state = f.chose_start_state()								
no = Node( f.convert_tripla(start_state), 'Start', None, 0, 0)
### Printando na tela o estado inicial para confirmar
print('\nstart_node',no,'\n')
    
limite = 10

def BPL_RECURSIVA(no,limite):
    global count_nodes
    if no.target_test():
        return f.print_formatted_sequence(no.sequence_of_action())
    elif limite == 0:
        return 'corte'
    else:
        corte_ocorreu=False

        for acao in acoes :

            filho = no.action_node(acao)
            count_nodes += 1
            resultado= BPL_RECURSIVA(filho,limite-1)

            if resultado == 'corte':
                corte_ocorreu = True

            elif resultado != 'falha':
                return resultado
        if corte_ocorreu:
            return 'corte'
        else:
            return 'falha'

BPL_RECURSIVA(no,limite)
print('count nos gerados:', count_nodes)