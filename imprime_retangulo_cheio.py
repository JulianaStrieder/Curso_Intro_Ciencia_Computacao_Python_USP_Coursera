largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

i = 0

while i < altura:
    print('#', end='')
    n = 0
    while n < (largura - 1):
        print('#', end='')
        n += 1
    i += 1
    print()