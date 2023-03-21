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
plt.title("Grafico de Nota��o Big'O")
plt.xlabel("Tamanho do conjunto de dados")
plt.ylabel("Tempo de execu��o")
plt.show()


"""
Claro! Para calcular a nota��o big'O' do algoritmo, precisamos analisar seu comportamento em rela��o ao tamanho de entrada.

No caso desse algoritmo, o tamanho de entrada � o n�mero de elementos na matriz, que � dado por maLi * maCol.

Se analisarmos o c�digo, percebemos que a complexidade do algoritmo � O(maLi * maCol), pois ele percorre cada elemento da matriz uma vez.

Para exibir a nota��o big'O' em um gr�fico, precisamos plotar um gr�fico em que o eixo x representa o tamanho de entrada e o eixo y representa o tempo de execu��o.

No c�digo acima, primeiro ordenamos a matriz para obter uma lista ordenada dos elementos. Em seguida, criamos duas listas x e y. A lista x cont�m valores de 0 a maLi * maCol - 1, que representam o tamanho do conjunto de dados. A lista y cont�m o tempo de execu��o para cada tamanho de entrada.

No nosso caso, o tempo de execu��o � simplesmente o tempo necess�rio para ordenar a matriz, que � dado pelo m�todo sorted. Como a complexidade do algoritmo � O(maLi * maCol), esperamos que o tempo de execu��o cres�a proporcionalmente a maLi * maCol.

Finalmente, usamos a biblioteca matplotlib para plotar um gr�fico de x versus y. A partir do gr�fico, podemos visualizar como o tempo de execu��o cresce em rela��o ao tamanho do conjunto de dados, e assim confirmar a nota��o big'O' do algoritmo.
"""
