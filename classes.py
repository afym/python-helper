class pet:
	number_of_legs = 0

	def sleep(self):
		return "ZzZzZz"

	def count_legs(self):
		return self.number_of_legs

class dog(pet):
	def bark(self):
		return "woof"

class person:
	__id = None
	__name = None
	__surname = None

	def set_id(self, identifier):
		self.__id = identifier

	def get_id(self):
		return self.__id

# Implementation with this class
false_dog = pet()
false_dog.number_of_legs = 4
print ("false_dog has %s legs." % (false_dog.number_of_legs))

sleep_false_dog = false_dog.sleep()

print ("false_dog is sleeping : %s " % (false_dog.sleep()))

# Implementation with dog class which extends from
true_dog = dog()

print ("true_dog is saying : %s " % (true_dog.bark()))
print ("true_dog is sleeping : %s " % (true_dog.sleep()))

# Implementation of private methods
person_number_1 = person()
person_number_1.set_id(100);

print ("Person id : %s " % (person_number_1.get_id())) # acces de private method