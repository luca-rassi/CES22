def p_decorador(param):
    def deco(fun):
        def wrapper(*args, **kwargs):
            return "<p>{0}</p>".format(fun(*args, **kwargs))
        return wrapper
    return deco
 
@p_decorador(str)
def formafrase(*args):
    frase = ' '

    for i in args:
        frase = frase + i + ' '
    return frase
 
@p_decorador(int)
def somar(*args):
    soma = 0

    for i in args:
        soma = soma + i
    return soma
 
 
print(formafrase('Fazendo', 'o', 'lab', 'de', 'CES22', 'concatenando', 'strings!'))
print(somar(1, 2, 3, 4, 5, 6, 7, 8, 9))