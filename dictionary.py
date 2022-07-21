myDictionary = {
    "name": "Stephano",
    "last_name": "Palomino",
    "age": 29,
    "weight": 73.5,
    "city": "Lima",
    "hobbies": ["gym", "piano", "gaming"]
}

print(myDictionary)
print(myDictionary["name"])
print(type(myDictionary))
print(len(myDictionary))

#loops
for value in myDictionary.values():
    print(value)

for key in myDictionary.keys():
    print(key)