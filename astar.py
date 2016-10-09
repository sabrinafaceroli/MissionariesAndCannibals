# Estado: [Canibais, Missionarios, Lado do barco]


# Capacidade do barco
CAP_BARCO = 2
# Lista de nós já gerados
LISTA_NOS = [[3, 3, 1]]
# Quantidade de missionarios e canibais
n = 3

# Função de distância
def f():
    return 1


# Heuristica utilizada para resolver o problema
def heuristica():
    return 1


# Verifica se o estado já está na lista de estados existentes
def existe_estado(estado):
    for i in LISTA_NOS:
        if i == estado:
            return True

    return False

# Verifica se o estado é válido
def estado_valido(estado):
    quantidade = n >= estado[0] >= 0 and n >= estado[1] >= 0
    maioria = False

    # Se a quantidade de M e C for igual OK
    if estado[1] == estado[0]:
        maioria = True
    # Se a quantidade de M é maior nos dois lados OK
    else:
        maioria = ((estado[1] >= estado[0]) and (n - estado[1] >= n - estado[0])) or (estado[1] == n) or (estado[1] == 0)

    if not existe_estado(estado) and quantidade and maioria:
        return True

    return False


class No:
    def __init__(self, estado=None):
        self.filhos = []
        self.distancia = None
        self.estado = estado

    def calcula_distancia(self):
        self.distancia = f()


class Grafo:
    def __init__(self):
        self.raiz = None

    # Método que gera o grafo
    def gera_filhos(self, b, lado, no):
        print ("Filhos de {}:".format(no.estado))
        for x in range(b + 1):
            for y in range(b + 1 - x):
                lado = (no.estado[2] + 1) % 2
                can = no.estado[0] - x * (-1) ** lado
                mis = no.estado[1] - y * (-1) ** lado

                # Possivel estado
                t_estado = [can, mis, lado]

                # Verifica a validade do estado criado
                if estado_valido(t_estado) and x + y > 0:
                    no.filhos.append(No(t_estado))
                    LISTA_NOS.append(t_estado)
                    print(t_estado)

        # Gera os filhos dos filhos
        for n in no.filhos:
            # Estado final nao precisa gerar filho
            if n.estado != [0,0,0]:
                self.gera_filhos(CAP_BARCO, lado, n)


inicio = No()
inicio.estado = [3, 3, 1]
inicio.filhos = []
G = Grafo()

G.raiz = inicio
G.gera_filhos(CAP_BARCO, 1, G.raiz)

print("VITORIA")
