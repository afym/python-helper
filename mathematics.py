import random
import math

for item in range(1, 10):
	randomNumber = random.randint(1, 100)
	print ('Random number is : ' + str(randomNumber))

# random number between 0 and 1
print (random.random())

# random choice from a list
users = ['Jhon', 'Jim', 'Lucy', 'Katy']

print (random.choice(users))

# neper and pi
print (math.e)
print (math.pi)

# trigo
angle = math.radians(90) # from degrees to radians
angle2 = math.degrees(20) # from radians to degrees

print (math.sin(angle)) # 1

# some about factorial
print (math.factorial(5))

# square
math.sqrt(49) # 7

# exp
math.exp(5)