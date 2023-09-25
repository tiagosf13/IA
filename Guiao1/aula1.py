#Exercicio 1.1
def comprimento(lista):
	if not lista:
		return 0
	else:
		return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	
	if not lista:
		return 0
	else:
		return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if not lista:
		return False
	else:
		return lista[0] == elem or existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
	if not l1:
		return l2
	elif not l2:
		return l1
	else:
		return [l1[0]] + concat(l1[1:], l2)
	pass

#Exercicio 1.5
def inverte(lista):
	if not lista:
		return []
	else:
		return inverte(lista[1:]) + [lista[0]]
	pass

#Exercicio 1.6
def capicua(lista):
	if not lista:
		return True
	else:
		comprimento_lista = comprimento(lista)
		furthest_index = comprimento_lista - 2
		return lista[0] == lista[-1] and capicua(lista[1:furthest_index])

#Exercicio 1.7
def concat_listas(lista):
	if not lista:
		return []
	else:
		return concat(lista[0], concat_listas(lista[1:]))

#Exercicio 1.8
def substitui(lista, original, novo):
	if not lista or not original or not novo:
		return lista
	else:
		if lista[0] == original:
			return concat([novo], substitui(lista[1:], original, novo))
		else:
			return concat([lista[0]], substitui(lista[1:], original, novo))

#Exercicio 1.9
def fusao_ordenada(lista1, lista2):
	if not lista1 or not lista2:
		return concat(lista1, lista2)
	else:
		if lista1[0] < lista2[0]:
			return concat([lista1[0]], fusao_ordenada(lista1[1:], lista2))
		else:
			return concat([lista2[0]], fusao_ordenada(lista1, lista2[1:]))

#Exercicio 1.10
def lista_subconjuntos(lista):
	if not lista:
		return [[]]
	else:
		element = lista[0]
		subsets = lista_subconjuntos(lista[1:])
		return concat(subsets, [[element] + subset for subset in subsets])


#Exercicio 2.1
def separar(lista):
	if not lista:
		return ([], [])
	else:
		first_element, second_element = lista[0][0], lista[0][1]
		first_list, second_list = separar(lista[1:])
		return (concat_listas([[first_element], first_list]), concat_listas([[second_element], second_list]))

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if not lista:
		return ([], 0)
	else:
		removed_list, count = remove_e_conta(lista[1:], elem)
		if lista[0] == elem:
			return (removed_list, count + 1)
		else:
			return (concat([lista[0]], removed_list), count)
	pass

#Exercicio 3.1
def cabeca(lista):
	if not lista:
		return None
	else:
		return lista[0]

#Exercicio 3.2
def cauda(lista):
	if not lista:
		return None
	else:
		return lista[1:]

#Exercicio 3.3
def juntar(l1, l2):
	if comprimento(l1) != comprimento(l2):
		return None
	element1 = cabeca(l1)
	element2 = cabeca(l2)
	if element1 == None or element2 == None:
		return None
	else:
		return concat([(element1, element2)], juntar(cauda(l1), cauda(l2)))


#Exercicio 3.4
def menor(lista):

	if not lista:
		return None
	else:
		minor = menor(lista[1:])
		if minor == None:
			return lista[0]
		else:
			if lista[0] < minor:
				return lista[0]
			else:
				return minor

#Exercicio 3.6
def max_min(lista):
	if not lista:
		return None
	else:
		max_min_tuple = max_min(lista[1:])

		if max_min_tuple == None:
			return (lista[0], lista[0])
		else:
			maximum = max_min_tuple[1]
			minimum = max_min_tuple[0]
			if lista[0] > maximum:
				maximum = lista[0]
			elif lista[0] < minimum:
				minimum = lista[0]
			return (minimum, maximum)