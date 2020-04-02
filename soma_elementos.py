def soma_elementos(lista):
    soma = 0
    
    for elemento in lista:
        soma = soma + elemento

    return soma   
 

lista1 = [1, 20, 3]
print(soma_elementos(lista1))