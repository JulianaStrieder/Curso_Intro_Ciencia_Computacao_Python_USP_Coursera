def computador_escolhe_jogada(n, m):
    '''
    Essa função recebe os valores para o número de peças inicial e 
    o número máximo de peças a serem tiradas em cada jogada, e retorna 
    quantas peças foram retiradas.
    '''
    multiplos_de_m_mais_um = [i for i in range(n+1) if i % (m+1) == 0]
    a = [n - x for x in multiplos_de_m_mais_um]
    
    for x in a:
        if x < m and x > 0:
            pecas_retiradas = x
        else:
            pecas_retiradas = m

    return pecas_retiradas


def usuario_escolhe_jogada(n, m):
    '''
    Essa função recebe os valores para o número de peças inicial e 
    o número máximo de peças a serem tiradas em cada jogada, e retorna 
    quantas peças foram retiradas.
    '''    
    pecas_retiradas = int(input('Quantas peças você vai tirar? '))
    
    while pecas_retiradas > m or pecas_retiradas <= 0:
        print('Jogada inválida! Escolha um valor menor ou igual a {} ou menor que a quantidade de peças que sobraram'.format(m))
        pecas_retiradas = int(input('Quantas peças você vai tirar? '))
        
    return pecas_retiradas    


def partida():
    '''
    Solicita ao usuário que informe os valores para o número de peças inicial e 
    o número máximo de peças a serem tiradas em cada jogada e inicia o jogo,
    alternando entre jogadas do computador e do usuário.
    '''
    total_pecas = int(input('Quantas peças? '))
    limite_pecas = int(input('Limite de peças por jogada? '))

    # while limite_pecas > total_pecas:
    #     limite_pecas = int(input('Limite de peças por jogada? '))


    placar_usuario = 0
    placar_computador = 0

    print()

   
    if total_pecas % (limite_pecas + 1) == 0:
        print('Você começa! \n')
        n = total_pecas
        m = limite_pecas
        
        while n > 0:
            pecas_retiradas = usuario_escolhe_jogada(n, m)
            n = n - pecas_retiradas
            
            if n > 1:
                print('Agora restam {} peças no tabuleiro.'.format(n))
            elif n == 1:
                print('Agora resta {} peça no tabuleiro.'.format(n))
            else:
                print('Fim do jogo! Você ganhou!')
                placar_usuario += 1

            pecas_retiradas = computador_escolhe_jogada(n, m)
            n = n - pecas_retiradas

            if n > 1:
                print('Agora restam {} peças no tabuleiro.'.format(n))
            elif n == 1:
                print('Agora resta {} peça no tabuleiro.'.format(n))
            else:
                print('Fim do jogo! O computador ganhou!')
                placar_computador += 1

    else:
        print('Computador começa! \n')
        n = total_pecas
        m = limite_pecas

        while n > 0:
            pecas_retiradas = computador_escolhe_jogada(n, m)
            n = n - pecas_retiradas
            if n > 1:
                print('Agora restam {} peças no tabuleiro.'.format(n))
            elif n == 1:
                print('Agora resta {} peça no tabuleiro.'.format(n))
            elif n <= m:
                print('Fim do jogo! O computador ganhou!')
                placar_computador += 1
                break
            else:
                print('Fim do jogo! O computador ganhou!')
                placar_computador += 1
                break
            pecas_retiradas = usuario_escolhe_jogada(n, m)
            n = n - pecas_retiradas
            if n > 1:
                print('Agora restam {} peças no tabuleiro.'.format(n))
            elif n == 1:
                print('Agora resta {} peça no tabuleiro.'.format(n))
            else:
                print('Fim do jogo! Você ganhou!')
                placar_usuario += 1
    return placar_computador, placar_usuario

def campeonato():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    camp = int(input('2 - para jogar um campeonato '))

    if camp == 1:
        partida()
        
    else:
        resultado = []
        print()
        print('Você escolheu um campeonato!')
        print()
        i = 0
        while i < 3:
            print()
            print('**** Rodada {} ****'.format(i+1))
            print()
            resultado.append(partida())
            i += 1
    
        placar_computador = int(resultado[0][0]) + int(resultado[1][0]) + int(resultado[2][0])
        placar_usuario = int(resultado[0][1]) + int(resultado[1][1]) + int(resultado[2][1])
        print('')
        print('**** Final do campeonato! ****')
        print()
        print('Placar: Você {} X {} Computador'.format(placar_usuario, placar_computador))

campeonato()

