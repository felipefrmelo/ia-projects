# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2

class Player:

	def __init__(self, name):
		if(name.lower() == 'max'):
			self.player = 'MAX'
			self.symbol = 'X'
		elif(name.lower() == 'min'):
			self.player = 'MIN'
			self.symbol = 'O'
		else:
			exit(1)


	def decision_minmax(hashgame):

		# max da lista [] valor-min(Resultado(estado,a))
		return # array de açoes finais

	def MAX(hashgame):
		if(hasggame.teste)
			return utiliy
		v = -999
		for each action
			list.append(v, MIN)
			v = max (v, list)
		return v

	def MIN(hashgame):
		if(hasggame.teste)
			return utiliy
		v = -999
		for each action
			list.append(v, MIN)
			v = min (v, list)
		return v



"""
Esturtura desse Problema

S0 = Estado inicial, o tabuleiro Vazio (' ')
JOGAROES() : 2 jogares, Max e Min
AÇOES(s): Possiveis açoes, vem de list_action do estado
RESULTADO(s,a): é o eaxecte_action, retorna umnovo estado
TESTE DE TERMINO(s)) : verifica se terminou ou nao
UTILIDADE(s,j: Quem ganhou, +1 para Max ou -1 para mIN ou empate????




"""