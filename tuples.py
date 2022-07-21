#No se puede modificar
myTuple = ("Belen", "Paola", "Viviana", "Andres")


print(myTuple)
print(type(myTuple))

#update: Lo conviertes en lista y de ahi lo vuelvo a transformar en tuple.

aux_list = list(myTuple)
aux_list.append("Juana")
aux_list[1] = "Mariana"
myTuple = tuple(aux_list)
print(myTuple)