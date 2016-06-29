class Bike(object):
	def __init__(self, price, max_speed,):
		self.price = price
		self.max_speed = max_speed
		self.sum_miles = 0

	def display(self):
		print 'the prince is $' + str(self.price)
		print 'the maxium speed is ' + str(self.max_speed) + 'mph'
		print 'the milige is ' + str(self.sum_miles) + 'miles'
		return self

	def ride(self):
		print 'have nice ride'
		self.sum_miles += 10
		return self

	def reverse(self):
		print 'bike repair'
		if self.sum_miles >= 5:
			self.sum_miles -= 5
		return self


bike1 = Bike(200, 25)
bike2 = Bike(200, 25)
bike3 = Bike(200, 25)

print 'bike1'
bike1.ride().ride().ride().reverse().display();
print '\n'

print"bike2"
bike2.ride().ride().reverse().reverse().display();
print'\n'

print "bike3"
bike3.reverse().reverse().reverse().display();

