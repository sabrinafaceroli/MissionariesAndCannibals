# Capacidade do barco
CAP_BARCO = 2
# Lista de nós já gerados
LISTA_NOS = []


# Função de distância
def f():
    return 10


# Heuristica utilizada para resolver o problema
def heuristica():
    return 1


# Verifica se o estado já está na lista de estados existentes
def existe_estado(estado):
    for i in LISTA_NOS:
        if i == estado:
            return False

    return True


class No:
    def __init__(self):
        self.filhos = None
        self.distancia = None
        self.estado = None

    def calcula_distancia(self):
        self.distancia = f()


class Grafo:
    def __init__(self):
        self.raiz = None

    # Método que gera o grafo
    def gera_filhos(self, b, lado, no):
        for x in range(b + 1):
            lado = (no.estado[2] + 2) % 2
            can = no.estado[0] + x * (-1) ** lado
            mis = no.estado[1] + (b - x) * (-1) ** lado

            t_estado = [can, mis, lado + (-1) ** lado]

            # Verifica a validade do estado criado
            if mis >= can and mis > 0 and can > 0 and not existe_estado(t_estado):
                no.filhos.append(t_estado)
                LISTA_NOS.append(t_estado)
                print("{} , {}".format(can, mis))

        # Gera os filhos dos filhos
        for n in no.filhos:
            self.gera_filhos(CAP_BARCO, lado, n)


inicio = No()
inicio.estado = [3, 3, 1]
inicio.filhos = []
G = Grafo()

G.raiz = inicio
G.gera_filhos(2, 1, G.raiz)
print(inicio.filhos)
