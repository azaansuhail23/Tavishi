list = [1, 2, "azaan", "24", True, 99]
# index  0  1    2       3     4    5

print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(type(list[3]))
print(type(list[4]))
print(type(list[5]))

# Slicing in list
print(list[0:3])  
print(list[3:6])
print(list[1:4])

print(len(list))

# String Methods
list.append("Tavishi")
print(list)

list.insert(2, "Happy Birthday")
print(list)

list1=[3,4,-1,7,9,11,0, -4, 1,99,16]
list1.sort()  #increasing/ascending order 
print(list1)