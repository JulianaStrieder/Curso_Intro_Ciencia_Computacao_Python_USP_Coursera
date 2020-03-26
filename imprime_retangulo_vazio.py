largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

i = 0

while i < altura: 
    n = 0
    while n < largura:
        if i > 0 and i != (altura - 1) and n > 0 and n < (largura - 1):
            print(' ', end='')
        else:
            print('#', end='')
        n += 1
    i += 1
    print()