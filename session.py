name = input("What is your name?")
age = input("How old are you?")
age = int(age)
birth_year = 2023 - age

print(f"OMG {name}, you are {age} years old so you were born in {birth_year}!")
print("OMG",name,", you are",age, " years old so you were born in", birth_year)

a = 6
print(a+2.0)
a/=2
print(a)
b = 3
print(a**b)
b -= a
print(b+2)
c = a > b
print(c)
print(c and a)
print(a+b+c)