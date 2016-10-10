# Estado: [Missionarios, Canibais, Lado do barco]

from operator import attrgetter

# Capacidade do barco
CAP_BARCO = int(input("Capacidade do barco "))
# Quantidade de canibais e missionários
N = int(input("Quantidade de canibais e missionários "))
# Lista de nós já gerados
LISTA_NOS = [[N, N, 1]]
# Custo de cada movimento é igual
CUSTO_MOVIMENTO = 1
NO_FINAL = [0, 0, 0]
# Caminho da solução
SOLUCAO = []
# Pais
P = []

# Heuristica utilizada para resolver o problema
def f_avaliacao(p_estado):
    # Soma de todos os elementos
    return sum(p_estado)


# Método que calcula a distância do estado para a solução.
# Leva em conta a heurística escolhida e os passos dados até ele.
def f_heuristica(p_no):
    distancia = 9999
    if p_no.estado:
        distancia = f_avaliacao(p_no.estado) + p_no.custo
    return distancia


# Verifica se o estado já está na lista de estados existentes
def existe_estado(p_estado):
    for i in LISTA_NOS:
        if i == p_estado:
            return True

    return False


# Verifica se o estado é válido
def estado_valido(p_estado):
    quantidade = N >= p_estado[1] >= 0 and N >= p_estado[0] >= 0

    # Se a quantidade de M e C for igual OK
    if p_estado[0] == p_estado[1]:
        maioria = True
    # Se a quantidade de M é maior nos dois lados OK
    else:
        maioria = ((p_estado[0] >= p_estado[1])
                    and (N - p_estado[0] >= N - p_estado[1])) \
                    or (p_estado[0] == N) or (p_estado[0] == 0)

    # Se o estado ainda não existe e a quantidade e a maioria nos dois lados
    # estão OK, este é um estado válido.
    if not existe_estado(p_estado) and quantidade and maioria:
        return True

    return False


class No:
    def __init__(self, estado=None, custo=0):
        self.estado = estado
        self.custo = custo
        self.filhos = []
        self.distancia = f_heuristica(self)


class Grafo:
    def __init__(self):
        self.raiz = None

    # Método que gera o grafo
    def gera_filhos(self, lado, no):
        # Gera todas as possibilidades de movimentos a partir do nó
        for x in range(CAP_BARCO + 1):
            for y in range(CAP_BARCO + 1 - x):
                lado = (no.estado[2] + 1) % 2
                canibais = no.estado[1] - x * (-1) ** lado
                missionarios = no.estado[0] - y * (-1) ** lado

                # Possivel estado
                t_estado = [missionarios, canibais, lado]

                # Verifica a validade do estado criado
                if estado_valido(t_estado) and x + y > 0:
                    no.filhos.append(No(t_estado, no.custo + 1))
                    P.append([t_estado, no.estado])
                    LISTA_NOS.append(t_estado)

        # Gera os filhos dos filhos
        for t in no.filhos:
            # Estado final nao precisa gerar filho
            if t.estado != [0, 0, 0]:
                self.gera_filhos(lado, t)


# Encontra o nó com menor função heuristica
def menor_no_aberto(p_abertos):
    min_num = min(p_abertos, key=attrgetter('distancia'))

    return min_num


# Constrói o caminho voltando pelos pais de cada nó
def constroi_caminho(p_no):
    caminho = []
    caminho.append(p_no.estado)
    atual = p_no.estado

    while atual != inicio.estado:
        for x in P:
            if atual == x[0]:
                caminho.insert(0, x[1])
                atual = x[1]
                break

    return caminho


# Algoritmo A*
def a_star(inicio):
    nos_abertos = [inicio]
    qtd_nos_visitados = 0

    while nos_abertos:
        # Pega o nó aberto com o menor valor de função heurística
        menor = menor_no_aberto(nos_abertos)
        qtd_nos_visitados = qtd_nos_visitados + 1

        # Se já tiver chegado na solução, constrói o caminho percorrido
        if menor.estado == [0, 0, 0]:
            return constroi_caminho(menor), qtd_nos_visitados

        # Remove o nó dos nós abertos e adiciona seus filhos
        nos_abertos.remove(menor)

        for x in menor.filhos:
            nos_abertos.append(x)

    # Retorna
    return -1


inicio = No()
inicio.estado = [N, N, 1]
inicio.filhos = []
G = Grafo()
G.raiz = inicio
G.gera_filhos(1, G.raiz)

s, qtd_visitados = a_star(G.raiz)
print("VITORIA")
print("Caminho:")
print(s)
print("Movimentos da solução: {}".format(len(s) - 1))
print("Quantidade de nós visitados: {}".format(qtd_visitados))
