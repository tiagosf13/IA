from math import sqrt, atan2

#Exercicio 4.1
impar = lambda number : number % 2 != 0

#Exercicio 4.2
positivo = lambda number : number >= 0

#Exercicio 4.3
comparar_modulo = lambda x, y : abs(x) < abs(y)

#Exercicio 4.4
cart2pol = lambda x, y : (sqrt(x**2 + y**2), atan2(y, x))

#Exercicio 4.5
ex5 = lambda f, g, h : lambda x, y, z : h(f(x, y), g(y, z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    if not lista:
        return True

    result = quantificador_universal(lista[1:], f)
    return result and f(lista[0])

#Exercicio 4.8
def subconjunto(lista1, lista2):
    if not lista1:
        return True

    if lista1[0] in lista2:
        return subconjunto(lista1[1:], lista2)
    else:
        return False

#Exercicio 4.9
def menor_ordem(lista, f):
    if not lista:
        return None
    
    minor = menor_ordem(lista[1:], f)

    if minor == None:
        return lista[0]
    else:
        return lista[0] if f(lista[0], minor) else minor
    

#Exercicio 4.10
def menor_e_resto_ordem(lista, f):
    if not lista:
        return (None, [])
    
    minor = menor_ordem(lista, f)
    lista.remove(minor)
    return (minor, lista)


#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass