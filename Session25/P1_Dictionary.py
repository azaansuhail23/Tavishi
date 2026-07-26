dict={
    'Tavishi':85,
    'Azaan':60,
    'Anuj':67,
    'Pathak':91,
    'Suhail':34
}

print(dict)

# key- value pair
# Way 1 : To fetch corresponding values
print(dict['Tavishi'])
print(dict['Azaan'])
print(dict['Anuj'])
print(dict['Pathak'])
print(dict['Suhail'])

print("-------------")

# Way 1 : To fetch corresponding values
print(dict.get('Tavishi'))

AllKeys=dict.keys() # give all the keys of a dictionary 
print(AllKeys)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()

print(x)

# Dictionary Methods : https://www.w3schools.com/python/python_ref_dictionary.asp
