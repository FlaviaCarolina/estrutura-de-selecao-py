#Escreva um algoritmo que leia um conjunto de 20 números inteiros e mostre qual foi o maior e o menor valor fornecido.
tamanho = 3
n=float(input("Digite um valor: "))
maior=n
menor=n
cont=0

while cont<tamanho: 
    n=float(input("Digite um valor: "))
    if(n<menor):
        menor=n
    if(n>maior):
        maior=n
    cont=cont+1

print(maior,menor)           