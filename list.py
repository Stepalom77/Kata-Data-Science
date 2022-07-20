from xmlrpc.client import boolean


list_elements = ["element_1", "element_2", "element_3"]

print(list_elements)
print(list_elements[0])
#length list
print(len(list_elements))

boolean_list = [True, False, True]
print(boolean_list)
integers_list = [1,2,3,4,5]
print(integers_list)
float_list = [1,3,2,6,3.78,5.99]
print(float_list)

print(type(float_list))

new_list = list((10,20,30,40))
print(new_list)