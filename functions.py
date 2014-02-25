cost1 = 15
cost2 = 20
globalVariable = 35

numbersList = [1, 22, 34, 55, 22.3]

def getSomeValue() :
	return globalVariable

def sumCart(item1 = 1, item2 = 0):
	totalCost = item1 + item2
	print(totalCost)

def pow(base, exponent):
	return base ** exponent

def getTotalAmount(productPricesList):
	amount = 0

	if type(productPricesList) == list and len(productPricesList) > 0 :
		for productPrice in productPricesList :
			amount += productPrice
	return amount


print (getSomeValue())

print (getTotalAmount(numbersList))
print (dir(numbersList))
print (type(numbersList) == list)

sumCart(1, 2)
sumCart(55)
sumCart(item2 = 60)

print(pow(10, 5))