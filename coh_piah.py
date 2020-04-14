import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def tamanho_medio_palavra(texto):
    '''
    Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    '''
    soma_tamanho_palavras = 0

    for palavra in texto:
        soma_tamanho_palavras = soma_tamanho_palavras + (len(palavra) - palavra.count(' '))
        
    tamanho_medio_palavra = soma_tamanho_palavras/len(texto)

    return tamanho_medio_palavra


def relacao_typen_token(texto):
    '''
    É o número de palavras diferentes dividido pelo número total de palavras.
    '''
    return n_palavras_diferentes(texto)/len(texto)


def razao_hapax_legomana(texto):
    '''
    É o número de palavras que aparecem uma única vez dividido pelo total de palavras. 
    '''
    return n_palavras_unicas(texto)/len(texto)


def tamanho_medio_sentenca(resultado):
    '''
    É a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
    '''
    soma_caracteres = 0
    for i in range(len(resultado)):
        soma_caracteres = soma_caracteres + len(resultado[i])
        
    return soma_caracteres/len(resultado)      


def complexidade_de_sentenca(resultado):
    '''
    É o número total de frases divido pelo número de sentenças.
    '''
    numero_frases = 0
    
    for res in resultado:
        numero_frases = numero_frases + len(separa_frases(res))
    
    return numero_frases/len(resultado)
        

def tamanho_medio_frase(resultado):
    '''
    É a soma do número de caracteres em cada frase dividida pelo número de frases no texto.
    '''
    
    frases = []
    soma_frases = 0
    for res in resultado:
        frases.append(separa_frases(res))
        soma_frases = soma_frases + len(separa_frases(res))
    
    soma = 0
    for frase in frases:
        for i in range(len(frase)):
            soma = soma + len(frase[i])
        
    return soma/soma_frases


def calcula_assinatura(texto):
    '''
    Essa funcao recebe um texto e deve devolver a assinatura do texto.
    '''
       
    assinatura_calculada = []

    
    texto_puro = re.split(r'[\s.!?,;:]+', texto)
    if texto_puro[-1] == '':
        del texto_puro[-1]
        
    assinatura_calculada.append(tamanho_medio_palavra(texto_puro))
    assinatura_calculada.append(relacao_typen_token(texto_puro))
    assinatura_calculada.append(razao_hapax_legomana(texto_puro))
    

    sentencas = separa_sentencas(texto)
    
    assinatura_calculada.append(tamanho_medio_sentenca(sentencas))
    assinatura_calculada.append(complexidade_de_sentenca(sentencas))
    assinatura_calculada.append(tamanho_medio_frase(sentencas))

    return assinatura_calculada


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    somatorio = 0
    for i in range(0,6):
        diferenca = abs(as_a[i] - as_b[i])
        somatorio = somatorio + diferenca
    
    similaridade = somatorio/6
    return similaridade


def avalia_textos(textos, ass_cp):
    '''
    Essa funcao recebe uma lista de textos e uma assinatura ass_cp 
    e deve devolver o numero (1 a n) do texto com maior probabilidade 
    de ter sido infectado por COH-PIAH.
    '''
    comparacao_assinaturas = 100
    
    for texto in textos:
        resultado = compara_assinatura(ass_cp, calcula_assinatura(texto))
        if comparacao_assinaturas > resultado:
            comparacao_assinaturas = resultado
            texto_id = textos.index(texto) + 1

    return texto_id
    # print('O autor do texto {} está infectado com COH-PIAH'.format(texto_id))
 


def main():
    
    assinatura_lida = le_assinatura()
    textos = le_textos()
    avalia_textos(textos, assinatura_lida)

    


if __name__ == "__main__":
    main()