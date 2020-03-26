def vogal(x):
    '''
    Função que retorna se a entrada é uma vogal ou não.
    '''
    if str(x).lower() in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False


vogal('a')
vogal('b')
vogal('E')