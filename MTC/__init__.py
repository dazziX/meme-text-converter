import random
from random import random as rnd
from googletrans import Translator
import json

trans = Translator()

class Convert:
	"""
	Example:
	from MTC import Convert
	text = Convert('Hello World')
	print(text.mock()) # convert to spongebob mock
	"""
	
	def __init__(self, text):
		self.text = text
		
	def mock(self):
		"""hELlO wORlD"""
		return ''.join([l.lower() if random.randint(0,1) == 0 else l.capitalize() for l in list(self.text)])
		
	def b(self):
		"""(N word) => ni🅱️🅱️a"""
		return ''.join(['🅱️' if l == 'g' else l for l in list(self.text)])
	
	def crab(self):
		"""🦀 HELLO WORLD 🦀"""
		caps = [l.capitalize() for l in list(self.text)]
		caps.insert(0, '🦀 ')
		caps.append(' 🦀')
		return ''.join(caps)
	
	def owo(self):
		"""Hewwo Wowwd"""
		to_owo = {'b':'w','j':'w','l':'w','n':'ny','r':'w','B':'W','J':'W','L':'W','N':'NY','R':'W'}
		return ''.join([to_owo.get(l, l) for l in list(self.text)])
		
	def sbeve(self):
		"""(Hell)o World"""
		sbren = ''

		for w in self.text.split(' '):
			b = False
			s = ''
			for c in w:
				b2 = rnd() <= .5
				if b != b2:
					s += '(' if b2 else ')'
					b = b2
				s += c
			sbren += s + (')' if s.count('(') < s.count(')') else '') + ' '
		return sbren
		
	def emoji(self):
		""" """
		output = []
		with open('MTC/emojis.json') as f:
			jsondata = json.loads(f.read())
		
		for word in self.text.split():
			emojis = [emoji["char"] for dict,emoji in jsondata.items() if word.lower().strip('.') in emoji["keywords"]]
			if emojis != []:
				output.append(word + random.choice(emojis))
			else:
				output.append(word)
				
		return ' '.join(output)
				
	def binary(self):
		"""1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100"""
		return ' '.join(format(ord(x), 'b') for x in self.text)
		
	def shuffle1(self):
		"""eHW olrlodl (letters and spaces)"""
		to_conv = list(self.text)
		random.shuffle(to_conv)
		return ''.join(to_conv)
		
	def shuffle2(self):
		"""eHWol rlodl (letters only)"""
		getlet = list(''.join(self.text.split()))
		convt = []
		for word in self.text.split():
			aa = []
			for l in range(len(word)):
				i = random.choice(range(len(getlet)))
				aa.append(getlet[i])
				getlet.pop(i)
			convt.append(''.join(aa))
			
		return ' '.join(convt)
		
	def shuffle3(self):
		"""World Hello (words only)"""
		words = self.text.split()
		random.shuffle(words)
		return ' '.join(words)
		
	def fllf(self):
		"""HelloolleH (flips the text across its center)"""
		half_i = len(self.text) // 2
		half = list(self.text)[:half_i]
		output = ''.join(half)
		half.reverse()
		output += ''.join(half)
		return output
		
	def piip(self):
		"""olleHHello (flips the text parallel to its center)"""
		half_i = len(self.text) // 2
		half = list(self.text)[half_i:]
		half.reverse()
		output = ''.join(half)
		half.reverse()
		output += ''.join(half)
		return output
		
	def lipsum(self):
		"""Salve Orbis Terrarum (translates to latin) (Requires internet connection)"""
		translation = trans.translate(self.text, dest='la')
		return translation.text
		
	def igbo(self):
		"""Ndewo Uwa (Requires internet connection)"""
		transla = trans.translate(self.text, dest='igbo')
		#udata = str(transla.text, 'utf-8')
		#return unidecode(udata)
		cdict = {'ụ':'u','ọ':'o','ị':'i','ṅ':'n','Ụ':'U','Ọ':'O','Ị':'I','Ṅ':'N'}
		conv = [cdict.get(l, l) for l in list(transla.text)]
		return ''.join(conv)
		
		
	
	
	#Random
	def random(self, include_from=False):
		"""A random conversion (Add include_from=True if you want to include .from conversions)"""
		choose = [self.mock(), self.b(), self.crab(), self.owo(), self.sbeve(), self.emoji(), self.binary(), self.shuffle1(), self.shuffle2(), self.shuffle3(), self.fllf(), self.piip(), self.lipsum(), self.igbo()]
		return random.choice(choose)
	

	
	
	
"""
hw = Convert('Hello World')
fox = Convert('The quick brown fox jumps over the lazy dog')
		
print(fox.sbeve())
"""		
		
		
		
		