N = 5
Numero = int(input("Digite o valor: "))
N = 5
cont = 1
menor = Numero
maior = Numero

while cont < N:
    Numero = int(input("Digite o numero: "))
    if Numero < menor:
        menor = Numero
    else:
      if Numero > maior:
        maior = Numero
    cont = cont + 1
print( "Menor:", menor , "Maior:", maior)