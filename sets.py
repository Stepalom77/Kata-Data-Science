#Son listas desordenados y que no repite elementos.
mySet = {"Tesla", "Ferrari", "BMW", "Aston Martin"}
mySet2 = {"Chevrolet", "Nissan", "Tesla"}
for el in mySet:
    print(el)

mySet.add("ADDD")
mySet.add("BMW")
mySet.update(mySet2)
print(mySet)
print(type(mySet))