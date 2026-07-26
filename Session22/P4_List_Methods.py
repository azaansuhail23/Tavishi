list=["Azaan",24,"Tavishi",16,True,False,"Volleyball"]

print(list)  #Before 

list.append("Suhail")
print(list)  #After insertion

# Multiple values not possible
# list.append("Jantar Mantar","Pathak",40.32)

list.extend(["Jantar Mantar","Pathak",40.32,"Azaan"])
print(list)

print(list.count('Azaan'))
print(len(list))

# Refer this : https://www.w3schools.com/python/python_lists_methods.asp
