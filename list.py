#empty list
list_1=[]

#mixed datatypes
list_2=["python",1,1.2,True]
print(list_2)
#accessing element
print(list_2[1])
print(list_2[:])
print(list_2[1:])
print(list_2[:3])

#deleting a list
del list_2[3]
print(list_2)
list_3=["python",1,1.2,True]
list_3.pop(0)
print(list_3)
list_3.pop()
print(list_3)
list1=["python","java","c++","android","ios"]
#assignment operator
list1[2]=".net"
print(list1)
print(".net" in list1)
#concatenation operator
print(list_3+list1)



