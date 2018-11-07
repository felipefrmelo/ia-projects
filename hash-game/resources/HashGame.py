# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2
import copy

class HashGame:

    
    # É definido por CONVEÇÃO que:
    count=0
    # O = MIN = -3
   
    # Constructor
    def __init__(self, state, origin, level, empty_indexs, utilidade, move):
        self.state        = state 	 		# Dicionario {(1,1):'X'.... inicializa vazio e é preenchido conforme as acoes são executadas
        self.origin	      = origin 			# Link para o pai
        self.level        = level           # Nível do jgo: a partir do 5 pode-se ter o fim de jogo (3 jogada de Max)%%!
        self.empty_indexs = empty_indexs    # Lista de tuplas com as acoes disponiveis para executar
        self.utilidade	  = utilidade         # Valor de 3 ,  0 ou -3
        self.move		  = move			# simbolo 'X' ou 'O'       

    def acoes(self):
        return self.empty_indexs
    
    def resultado(self,acao):
        if acao not in self.empty_indexs:
            return self
        self.count+=1
        state = self.state.copy()
        state[acao]= self.move
        empty_indexs = self.empty_indexs.copy()
        empty_indexs.remove(acao)
        return HashGame(state, self, self.level+1, empty_indexs, self.calcula_utilidade(state,acao,self.move),
                        'O' if self.move == 'X' else 'X')
       
    def calcula_utilidade(self, state, acao, player):
        """Se 'X' vence com esta acao, return 3; if 'O' vence return -3; else return 0."""
        if (self.aux_utilidade(state, acao, player, (0, 1)) or #verifica na horizontal
                self.aux_utilidade(state, acao, player, (1, 0)) or #verifica na vertical
                self.aux_utilidade(state, acao, player, (1, -1)) or #verifica na diagonal
            self.aux_utilidade(state, acao, player, (1, 1))): #//
            return 3 if player == 'X' else -3
        else:
            return 0
        
    def aux_utilidade(self, state, acao, player, delta_x_y):
        
        (delta_x, delta_y) = delta_x_y #tupla para varrer nas direcoes: horizontal,vertical e diagonais
        x, y = acao
        n = 0  
        while state.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = acao
        while state.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Porque eh contado duas vezes
        return n >= 3
    
    def test_end(self):
        
        return self.utilidade != 0 or len(self.empty_indexs) == 0
        
        
    
    def __str__(self):
        str_out= '\n'
        for i in range(1,4):
            str_out+= '\t'
            for j in range(1,4):
                str_out+= '|'+self.state.get((i,j),' ')
            str_out+= '|'+'\n'
        return str_out
    
    def print_all_hashgame(self):
        if(self.origin is None):
            print(self)
        else:
            self.origin.print_all_hashgame()
            a=list(self.state.items()).pop()
            print(a[1]+' ==>',a[0])
            print(self)

        return
    
    def play_game(self, *players):
        
        while True:
            for player in players:
                acao = player(self)
                self = self.resultado(acao)
                if self.test_end():
                    self.print_final(players)
                    
                    return self
                
    def print_final(self,players):
        
        H_player=False
        
        for i in players:
            if i.__name__ == 'h_player':
                H_player=True
        
        if H_player:
            print(self)
            if self.utilidade==3:
                print('Player 1 Ganhou!')
            elif self.utilidade==-3:
                print('Player 2 Ganhou!')
            else:
                print('Empatou!!')
        else:
            self.print_all_hashgame()
            if self.utilidade==3:
                print('Player 1 Ganhou!')
            elif self.utilidade==-3:
                print('Player 2 Ganhou!')
            else:
                print('Empatou!!')
            

