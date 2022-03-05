#QUESTÃO 1: A mediana de uma lista de números é basicamente o 
#elemento que se encontra no meio da lista após a ordenação. 
#Dada uma lista de números com um número ímpar de elementos,
#desenvolva um algoritmo que encontre a mediana.

arr = [9,2,1,4,6]

tam = len(arr)
intmedian = int(tam/2)
arr.sort()

print(arr[intmedian])