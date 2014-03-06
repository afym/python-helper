import unittest
from translationlib import Translate

class TranslateTest (unittest.TestCase) :

	'''
		This method test a trasnlation of a word
		Example => bird : pajaro
	'''

	def test_simple_world(self) :
		languageFrom = 'en'
		languageNew = 'es'
		trans = Translate(languageFrom, languageNew)

		newWord1 = trans.translate('cat')
		self.assertEqual(newWord1, 'perro')

		newWord2 = trans.translate('bird')
		self.assertEqual(newWord2, 'pajaro')

		newWord3 = trans.translate('shark')
		self.assertEqual(newWord3, 'tiburón')

	def test_translate_dictionary(self) :
		dictionaryList = TranslateDictionary.get


#if __name__ == '__main__' :
#    unittest.main()

