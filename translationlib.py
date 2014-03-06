
class Translate :
	DEFAULT_LANGUAE_FROM = 'en'
	__languageFrom = None
	__languageNew = None

	def __init__ (self, languageFrom, languageNew) :
		__languageFrom = languageFrom
		__languageNew = languageNew

	def translate(self, translate) :
		if translate == 'cat' :
			return 'perro'
		elif translate == 'bird' :
			return 'pajaro'
		elif translate == 'shark' :
			return 'tiburón'
		else :
			return ''
		