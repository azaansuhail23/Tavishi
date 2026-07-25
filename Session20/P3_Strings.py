# String formatting
_name = "Azaan"
age = 24
profession = "Software Engineer"
working = "Remotely"

# Way 1
print(
    _name,
    "is a tutor at Codeyoung whose age is",
    age,
    "he is working",
    working,
    "as a",
    profession,
)

print("------")

# Way2 : String formatting using f string
print(
    f"{_name} is a tutor at Codeyoung whose age is {age} he is working {working} as a {profession}"
)
