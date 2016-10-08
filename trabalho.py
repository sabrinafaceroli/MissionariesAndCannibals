# Trabalho 1 - Inteligencia Artificial
# Sabrina Faceroli Tridico - 9066452

# O vetor tem a seguinte configuracao [missionarios, canibais, lado em que o barco esta]
status = ()

#Grafo com caminhos - usando Lista de Adjacencias
listaAdj = {}

# A seguir o numero de lugares no barco
lugaresBarco = input("Digite o numero de lugares do barco: ")
aux = input("Digite o numero de missionarios/canibais: ")

# O lado do barco eh 1 - direita e 0 - esquerda. Comeca na direita e com o mesmo numero de canibais e missionarios!
status = (aux, aux, 1)

# Funcao para gerar o grafo de caminhos
def caminhosPossiveis(stat, lugares):
    row = caminhosPossiveisRecursao(stat, lugares)
    listaAdj[stat] = row

# DEUS QUE QUE TÁ ACONTECENDOOOO
def caminhosPossiveisRecursao(stat, lugares):
    row = []
    if (lugares == 1):
        caminho = (stat[0]-1, stat[1], stat[2])
        row.append(caminho)
        print row
        caminho = (stat[0], stat[1]-1, stat[2])
        row.append(caminho)
        print row
    else:
#    for a in range(lugares, 1):
        caminho = ((stat[0]-lugares), stat[1], stat[2])
        row.append(caminho)
        print row
        caminho = (stat[0], (stat[1]-lugares), stat[2])
        row.append(caminho)
        print row
        caminho = caminhosPossiveis(stat, (lugares-1))
        row.append(caminho)
        print row
    
    return row


caminhosPossiveis(status, lugaresBarco)
print listaAdj
     
