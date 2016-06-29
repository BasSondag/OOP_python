class Animal(object):
	def __init__(self, name):
		self.name = name
		self.healt = 100	

	def Walk(self):
		print 'walking'
		self.healt -= 1
		return self

	def Run(self):
		print 'running'
		self.healt -= 5
		return self

	def display_Healt(self):
		
		print 'my Hame is: '+ str(self.name)
		print 'my Healt is: '+str(self.healt)
		if self.healt <= 0:
			self.healt += 100
		return self
#End of Animal


class Dog(Animal):
	def __init__(self, name):
		super(Dog, self). __init__(name)
		self.healt = 150

	def Pet(self):
		print 'pet me'
		self.healt += 5
		return self	
#End of Dog


class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self). __init__(name)
		self.healt = 170

	def Fly(self):
		print 'flying'
		self.healt -= 10
		return self

	def display_Healt(self):
		print 'This is the Dragon'
		super(Dragon, self).display_Healt()
		return self
#End of dragon


animal = Animal('animal' )
animal.Walk().Walk().Walk().Run().Run().display_Healt();

dog = Dog('dog')
dog.Walk().Walk().Walk().Run().Run().Pet().display_Healt();		

dragon = Dragon('dragon')
dragon.Walk().Walk().Walk().Run().Run().Fly().Fly().display_Healt();		