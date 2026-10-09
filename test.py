# human = False
# print(human)
# print(type(human))

# print("Are you a human: " + str(human))

# first_name = "ivan"
# last_name = "dalena"
# print(first_name + " " + last_name)


#multiple assignment

# name = "ivan"
# age = 21
# attractive = True

# name, age, attractive = "ivan", 21, True
# print(name)

# Spongebob = Patrick = Sandy = 30
# print(Spongebob)


# name = "ivan"
#print(len(name)) #returns the length of the string
#print(name.find("v")) #returns the position of the letter requested
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("a","e"))
# print(name*3)

# x = 1 #int
# y = 2.0 #float
# z = "3" #str, we cannot perform math on strings!

# int(y) #to convert y into type int. it is not a permanent change!
# # if I want a permanent change I have to recast y

# print(x, int(y), z*3)
# print(x*4, y, z)

# x, y , z = float(x), float(y), float(z)
# print(x,y,z)






import random
import math

random.seed(42)

x = random.uniform(-1, 1)

q = (3/4) * (1 + x*x) #proposal distribution q(x)
p = (3/8) * (1 + x*x)

print(q)

u = random.uniform(0, )
