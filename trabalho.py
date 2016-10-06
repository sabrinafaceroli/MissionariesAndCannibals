# Trabalho 1 - Inteligencia Artificial
# Sabrina Faceroli Tridico - 9066452

# O vetor tem a seguinte configuracao [missionarios, canibais, lado em que o barco esta]
status = []

#Grafo com caminhos - usando Lista de Adjacencias
listaAdj = []

# A seguir o numero de lugares no barco
lugaresBarcos = input("Digite o numero de lugares do barco: ")

status.append(input("Digite o numero de missionarios/canibais: "))
status.append(status[0])

# O lado do barco eh 1 - direita e 0 - esquerda. Comeca na direita!
status.append(1)

print status

# Funcao para gerar o grafo de caminhos
def caminhosPossiveis(stat):
    row = []
    for a in range(1, stat[0]):
        caminho = ((stat[0]-a), (stat[1]-a), stat[2])
        row.append(caminho)

    listaAdj.append([stat, row]) 

caminhosPossiveis(status)

# Vou trabalhar nisso mais tarde
#status = [3, 2, 1]

#caminhosPossiveis(status)
#print listaAdj[0]
#print listaAdj[1]        

#tupla = listaAdj[0]
#tuplat = tupla[0]
#print tuplat[2]
     
