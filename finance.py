'''
	Financial functions
'''
def addTax(price, tax):
	newPrice = price / 100 * (100 + tax)
	return newPrice

def discount(price, discount):
	return (1 - discount) * price

def pricing(price, amount):
	return (price * 5) / (amount ** 2)