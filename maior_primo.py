def ehprimo(x):
        seq_numeros = [i for i in range(x, 1, -1)]
        res = [x % i for i in seq_numeros]
        qtd_zeros = res.count(0)

        if qtd_zeros <= 1: # é primo
            return 'é primo'
        else:
            return 'não é primo'



def maior_primo(y):
    
    seq_num = [i for i in range(y, 1, -1)]
    o_que_e = [ehprimo(j) for j in seq_num]

    if o_que_e[0] == 'é primo':
        res1 = seq_num[0]
        return res1
    else:
        if 'é primo' in o_que_e:
            res = list(map(lambda i: i == 'é primo', o_que_e)).index(True)
            primeiro_primo = seq_num[res]
        return primeiro_primo


    
print(maior_primo(521))