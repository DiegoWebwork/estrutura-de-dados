import matplotlib.pyplot as plt 
matriz = [['a', 'b', 'c', 'd'],['q', 'i', 'n', 'm'],['f', 'e', 'h', 'j'], ['p', 'o', 'l', 'g']]


#definimos as variaveis que utilizaremos para trabalhar com a matriz fornecida
maLi = len(matriz)  #Linha
maCol = len(matriz[0])  #Coluna
iniLi = 0   #Linha inicial
fimLi = maLi - 1    #Define linha final pegando a o indice da matriz e subtraindo 1
iniCol = 0  #Define a coluna inicial 
fimCol = maCol - 1  #Define coluna final pegando a o indice da matriz e subtraindo 1
indices = []   #array para atribuir as posi��es e fazer indexa��o com for.

# Abre laco
while iniLi <= fimLi and iniCol <= fimCol:
    # Percorre a linha superior da matriz
    for i in range(iniCol, fimCol + 1):
        indices.append(f"{iniLi}:{i}")
    iniLi += 1

    # Percorre a ultima coluna da matriz
    for i in range(iniLi, fimLi + 1):
        indices.append(f"{i}:{fimCol}")
    fimCol -= 1

    # Percorre a ultima linha da matriz
    if iniLi <= fimLi:
        for i in range(fimCol, iniCol - 1, -1):
            indices.append(f"{fimLi}:{i}")
        fimLi -= 1

    # Percorre a primeira coluna da matriz
    if iniCol <= fimCol:
        for i in range(fimLi, iniLi - 1, -1):
            indices.append(f"{i}:{iniCol}")
        iniCol += 1

# Ordena os elementos em ordem crescente e imprime
matrizPronta = sorted([mtx for linha in matriz for mtx in linha])
print("Matriz ordenada: ", matrizPronta)
print("Posi��es:", indices)


x = list(range(len(matrizPronta)))
y = [ord(c) for c in matrizPronta]

plt.plot(x, y)
plt.title("Grafico de Notação Big'O")
plt.xlabel("Tamanho do conjunto de dados")
plt.ylabel("Tempo de execução")
plt.show()
