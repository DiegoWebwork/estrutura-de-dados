import matplotlib.pyplot as plt

#criamos a matriz de 4x4 (4 listas de 4 elementos cada.)

matrizElementos = [['a', 'b', 'c', 'd'],['q', 'i', 'n', 'm'],['f', 'e', 'h', 'j'], ['p', 'o', 'l', 'g']] 

#definimos as variaveis que utilizaremos para trabalhar com a matrizElementos fornecida

linhaMatriz = len(matrizElementos)  #Linha
colunaMatriz = len(matrizElementos[0])  #Coluna
linhaInicial = 0   #Linha inicial
linhaFinal = linhaMatriz - 1  
colunaInicial = 0  #Define a coluna inicial 
colunaFinal = colunaMatriz - 1  
indices = []   #array para atribuir as posições e percorrer as mesmas com laço for.


"""
essas variáveis (linhaInicial e colunaFinal) tomam o valor -1 para ajustar a diferença entre a contagem de linhas/colunas (que começa em 1) e os índices da matriz (que começam em 0).
"""

while linhaInicial <= linhaFinal and colunaInicial <= colunaFinal: #Esse loop while percorre a matriz enquanto a linha inicial não ultrapassar a linha final e a coluna inicial não ultrapassar a coluna final.
    
    for i in range(colunaInicial, colunaFinal + 1): #Essa condicional percorre a linha superior da matriz, adicionando as posições passadas na lista indices.
        indices.append(f"{linhaInicial}:{i}")
    linhaInicial += 1

   
    for i in range(linhaInicial, linhaFinal + 1): #Essa condicional percorre a última coluna da matriz, adicionando as posições passadas na lista indices.
        indices.append(f"{i}:{colunaFinal}")
    colunaFinal -= 1

    
    if linhaInicial <= linhaFinal:  #Essa condicional define que será percorrida a última linha da matriz, caso exista. Ela é executada somente se a linhaInicial for menor ou igual à linhaFinal.
        for i in range(colunaFinal, colunaInicial - 1, -1): #Essa condicional percorre a última linha da matriz em ordem inversa, adicionando as posições passadas na lista indices.
            indices.append(f"{linhaFinal}:{i}")
        linhaFinal -= 1     #é usada para atualizar a variável linhaFinal, para que o próximo loop while comece na linha anterior.

    
    if colunaInicial <= colunaFinal: #Essa condicional define que será percorrida a primeira coluna da matriz, caso exista. Ela é executada somente se a colunaInicial for menor ou igual à colunaFinal.
        for i in range(linhaFinal, linhaInicial - 1, -1):   #Essa condicional percorre a primeira coluna da matriz em ordem inversa, adicionando as posições passadas na lista indices.
            indices.append(f"{i}:{colunaInicial}")
        colunaInicial += 1  #Essa linha adiciona 1 à variável colunaInicial para que o loop saia da seção já visitada.


unidimenLista = sorted([mtx for linha in matrizElementos for mtx in linha]) #list comprehension, essa construção cria uma lista unidimensional que contém todos os elementos da matriz original matrizElementos.
print("Matriz ordenada: ", unidimenLista)
print("Posições:", indices)


x = list(range(len(unidimenLista)))
y = [ord(c) for c in unidimenLista]

plt.plot(x, y)
plt.title("Grafico de Notação Big'O")
plt.xlabel("Tamanho do conjunto de dados")
plt.ylabel("Tempo de execução")
plt.show()


