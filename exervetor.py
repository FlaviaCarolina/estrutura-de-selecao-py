#exercicio2
v=[5,4,8,7,10]
par = 0
impar = 0
cont=0
tamanho_vetor=len(v)

while cont< tamanho_vetor:
    print("vetor na posição:", cont)
    print("O valor da posição é: ", v[cont])
    if((v[cont] % 2) == 0):
        par=par+1
        print("par")
    else:
        impar=impar+1
        print("impar")
    cont = cont + 1

print("par:", par)    
print("impar:", impar)  
