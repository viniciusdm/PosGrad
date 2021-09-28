
#Author: Vinicius Bueno de Moraes - 2021 - Brazil - SP
#Vector Subspace Analysis
#Code Entries - Portuguese-br

# -*- coding: utf-8 -*-

import sympy 
import numpy as np

print("\nDimensōes de Subespaços Vetoriais - Soma e Intersecção - Vinicius Bueno de Moraes | EPUSP - 2021")
espacos = int(input("\nEm quantos Subespaços Vetoriais quer verificar Dependência Linear: "))
colunas = int(input("\nQuantos Elementos existem por Vetor (RX): "))

l = 0;
soma = 0;
dimFinal = 0;
intersecacao = 0;

matrizes = np.zeros((100, colunas));
dimensoesBases = np.zeros(espacos);

for h in range (1, espacos+1):
    linhas = int(input("\nQuantos Vetores existem no Subespaço {}: ".format(h)))
    vetor = np.zeros(colunas);
    matriz = np.zeros((linhas, colunas));
    
    for i in range (1, linhas+1):
        
        for j in range (1, colunas+1):
            a = int(input("Subespaço {} - Digite o {}º elemento do {}º vetor: ".format(h, j, i)))
            matriz[i-1][j-1] = a
            vetor[j-1] = a

        print(("\nO {}º Vetor do Subespaço {} digitado foi: ". format(i, h)), vetor, "\n")
    print("A Matriz do {}º Subespaço é: \n\n".format(h), matriz, "\n")
    
    _, inds = sympy.Matrix(matriz).T.rref()   
    dim = len(inds)
    base = np.zeros((len(inds), colunas));

    for i in range(1, len(inds)+1):
        base[i-1] = matriz[inds[i-1]]

    print("A dimensão do {}º Subespaço é {},".format(h, dim), "e uma Base para ele é:\n\n", base, "\n")
    
    for i in range (1, len(inds)+1):
        matrizes[l] = base[i-1];
        l = l + 1

    dimensoesBases[h-1] = dim;

print("\nAssim, tem-se que: \n")

for i in range(1, len(dimensoesBases)+1):
    print("A dimensão do {}º Subespaço é: {}".format(i, dimensoesBases[i-1]))

_, inds = sympy.Matrix(matrizes).T.rref()   
dim = len(inds)
base = np.zeros((len(inds), colunas));

for i in range(1, len(inds)+1):
    base[i-1] = matrizes[inds[i-1]]

for i in range(1, len(dimensoesBases)+1):
     dimFinal = dimFinal + dimensoesBases[i-1]

interseccao = dimFinal - dim
 
print("A dimensão da Intersecçāo entre eles é: {}". format(interseccao))
print("A dimensão da Soma é: {}". format(dim))
print("\nSendo uma Base para a Soma dos Subespaços: \n")
print(base)
print()
print("\nE a União dos Subespaços, contendo a Intersecção - O que não faz sentido, apenas para visualização: \n")
matrizes = matrizes[~np.all(matrizes == 0, axis=1)]
print(matrizes)
print()
