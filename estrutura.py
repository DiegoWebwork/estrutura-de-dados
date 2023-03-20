elementos = [['a', 'b', 'c', 'd'], ['q', 'i', 'n', 'm'], ['f', 'e', 'h', 'j'], ['p', 'o', 'l','g'],];
#definimos as variaveis que utilizaremos para trabalhar com a matriz fornecida
maLi = len(elementos)  #Linha
maCol = len(elementos[0])  #Coluna
iniLi = 0   #Linha inicial
fimLi = maLi - 1    #Define linha final pegando a o indice da matriz e subtraindo 1
iniCol = 0  #Define a coluna inicial
fimCol = maCol - 1  #Define coluna final pegando a o indice da matriz e subtraindo 1
indices = []   #array para atribuir as posições e fazer indexação com for.

# Abre laço
while iniLi <= fimLi and iniCol <= fimCol:
    # Percorre a linha superior da matriz
    for i in range(iniCol, fimCol + 1):
        indices.append(f"{iniLi}:{i}")
    iniLi += 1

    # Percorre a última coluna da matriz
    for i in range(iniLi, fimLi + 1):
        indices.append(f"{i}:{fimCol}")
    fimCol -= 1

    # Percorre a última linha da matriz
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
matrizPronta = sorted([mtx for linha in elementos for mtx in linha])
print("Matriz ordenada: ", matrizPronta)
print("Posições:", indices)


"""
Este código cria uma matriz de 4x4 com números inteiros e, em seguida, ordena seus elementos em ordem crescente e imprime a matriz ordenada e as posições em que os elementos estão na matriz.
O script começa definindo as variáveis que serão usadas para trabalhar com a matriz, como o número de linhas e colunas, as posições iniciais e
finais e uma lista vazia para armazenar as posições dos elementos. Em seguida, um laço while é iniciado, que percorre a matriz em espiral,
começando pela linha superior e percorrendo em sentido horário.
Dentro do laço while, há quatro laços for aninhados, que percorrem a linha superior, a última coluna, a última linha e a primeira coluna da matriz, respectivamente.
Para cada iteração desses laços, as posições dos elementos correspondentes são adicionadas à lista de índices.
Finalmente, a lista de índices é impressa juntamente com a matriz ordenada, que é criada usando a função sorted() aplicada à matriz original.

"""