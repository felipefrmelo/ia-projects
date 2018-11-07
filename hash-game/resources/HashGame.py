# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2
import copy

class HashGame:

    count_node = 0
   
    # Constructor
    def __init__(self, state, origin, level, empty_indexs, utilidade, move):
        self.state        = state           # Dicionario {(1,1):'X'.... inicializa vazio e é preenchido conforme as acoes são executadas
        self.origin	      = origin          # Link para o pai
        self.level        = level           # Nível do jogo
        self.empty_indexs = empty_indexs    # Lista de tuplas com as acoes disponiveis para executar
        self.utilidade	  = utilidade       # Valor de 3 ,  0 ou -3
        self.move		  = move            # simbolo 'X' ou 'O'       

    def acoes(self):
        return self.empty_indexs
    
    # Aplicaççao de ação: é passado somente a tupla de onde vai ser colocado o simbolo
    def resultado(self, acao):
        if acao not in self.empty_indexs:
            return self
        HashGame.count_node += 1
        state = self.state.copy()
        state[acao]= self.move
        empty_indexs = self.empty_indexs.copy()
        empty_indexs.remove(acao)
        return HashGame(state, self, self.level+1, empty_indexs, self.calcula_utilidade(state,acao,self.move),
                        'O' if self.move == 'X' else 'X')
       
    def calcula_utilidade(self, state, acao, symbol_player):
        # Se 'X' vence com esta acao, return 3; if 'O' vence return -3; else return 0.
        if (self.aux_utilidade(state, acao, symbol_player, (0, 1) ) or # check na horizontal 
            self.aux_utilidade(state, acao, symbol_player, (1, 0) ) or # check na vertical   
            self.aux_utilidade(state, acao, symbol_player, (1, -1)) or # check na diagonal 1
            self.aux_utilidade(state, acao, symbol_player, (1, 1) )):  # check na diagonal 2
            return 3 if symbol_player == 'X' else -3
        else:
            return 0
        
    # Percorre 'state' apartir de onde foi colocado acao se formou uma linha de acordo com delta_x_y em h, v, d1, d2
    # Check se formou a linha contando
    def aux_utilidade(self, state, acao, symbol_player, delta_x_y):
        (delta_x, delta_y) = delta_x_y 
        x, y = acao
        n = 0  
        while state.get((x, y)) == symbol_player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = acao
        while state.get((x, y)) == symbol_player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Porque eh contado duas vezes
        return n >= 3
    
    # Testa se chegou ao fim verificando a utilidade e se acabou as jogadas (possivel empate)
    def test_end(self):
        return self.utilidade != 0 or len(self.empty_indexs) == 0

    # O que é impresso ao dar 'print' num objeto
    def __str__(self):
        str_out= '\n'
        for i in range(1,4):
            str_out+= '\t'
            for j in range(1,4):
                str_out+= '|'+self.state.get((i,j),' ')
            str_out+= '|'+'\n'
        return str_out
    
    # print recursivo do jogo. Vai até o pai de origem e dpeois imprime na ordem inicio -> fim
    def print_all_hashgame(self):
        if(self.origin is None):
            print(self)
        else:
            self.origin.print_all_hashgame()
            a=list(self.state.items()).pop()
            print(a[1]+' ==>',a[0])
            print(self)
        return
    
    # COmo funciona a partida
    def play_game(self, *players):
        while True:
            for player in players:
                acao = player(self)
                self = self.resultado(acao)
                if self.test_end():
                    self.print_final(players)
                    return self
                
    # Impressão no final: Se for
    def print_final(self,players):
        H_player = False
        for i in players:
            if i.__name__ == 'h_player':
                H_player = True
        
        if H_player:
            print(self)
            self.print_final_status()
        else:
            self.print_all_hashgame()
            self.print_final_status()

    # Imprime se Ganou, Perdeu ou Empatou
    def print_final_status(self):
        if self.utilidade==3:
            print('Player 1 Ganhou!')
        elif self.utilidade==-3:
            print('Player 2 Ganhou!')
        else:
            print('Empatou!!')
            

