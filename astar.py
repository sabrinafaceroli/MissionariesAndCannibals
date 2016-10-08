CAP_BARCO = 2
LISTA_NOS = []


# def f():
#    return 10

# def heuristica():
#    return 1

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

    def gera_filhos(self, b, lado, no):
        for x in range(b + 1):
            lado = (no.estado[2] + 2) % 2
            can = no.estado[0] + x * (-1) ** lado
            mis = no.estado[1] + (b - x) * (-1) ** lado
            t_estado = [can, mis, lado + (-1) ** lado]

            if mis >= can and mis > 0 and can > 0 and not existe_estado(t_estado):
                no.filhos.append(t_estado)
                LISTA_NOS.append(t_estado)
                print("{} , {}".format(can, mis))

        for n in no.filhos:
            self.gera_filhos(CAP_BARCO, lado, n)


inicio = No()
inicio.estado = [3, 3, 1]
inicio.filhos = []
G = Grafo()

G.raiz = inicio
G.gera_filhos(2, 1, G.raiz)
print(inicio.filhos)
