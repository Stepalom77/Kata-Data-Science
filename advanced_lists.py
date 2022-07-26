myList = [1,2,3,4,5,6,7,8]

myList.append(9) # add to end of the list
myList.append(10)
myList.insert(0,0) # add to specific index of list
myList.remove(7) # remove specific element
myList.pop() # remove last index
del myList[3] # remove specific element

# myList.clear()

print("FOR IN LOOP")
for x in myList:
    print(x)

print("FOR IN RANGE LOOP")
for e in range(len(myList)):
    print(myList[e])
#While loop
print("While loop")
itr = 0
while itr < len(myList):
    print(myList[itr])
    itr = itr + 1

print(myList)

print("LOOPING A LIST BY LIST COMPREHENSION")
[print(x) for x in myList]