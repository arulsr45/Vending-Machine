# Registering connection to Parse
from parse_rest.connection import register
register("t4WKDKIQROtp4tUHtQRyUOBGAnyTKjMv8fwlzMvB","IMTtB88bSsiWhOei0aCGJI3QIRChqUXZYBAXf0aa", master_key=None)

# Using the Parse Object to update the stock
from parse_rest.datatypes import Object as ParseObject

# variable to use to test decrementing
n = 0

# decrement function
#   decrement quantity and save in the cloud
def decrement(item):
	item.quantity -= 1
	item.save()

while True:
<<<<<<< HEAD
	# inventory procedure
	n = int(input("Enter a number:"))

=======
	n = int(input("Enter a number:"))
	# inventory procedure
>>>>>>> 9b2194ddb59e55a3e7c7e7f1e235b79515799980
	if n == 0:
		obj = ParseObject.Query.get(title='Coke')
		decrement(obj)
	elif n == 1:
		obj = ParseObject.Query.get(title='DietCoke')
		decrement(obj)
	elif n == 2:
		obj = ParseObject.Query.get(title='Water')
		decrement(obj)
	elif n == 3:
		obj = ParseObject.Query.get(title='Sprite')
		decrement(obj)	
	elif n == 4:
		obj = ParseObject.Query.get(title='StrawberryGatorade')
		decrement(obj)	
	elif n == 5:
		obj = ParseObject.Query.get(title='MelonGatorade')
		decrement(obj)
	elif n == 6:
		obj = ParseObject.Query.get(title='GrapeGatorade')
		decrement(obj)
	elif n == 7:
		obj = ParseObject.Query.get(title='Rockstar')
		decrement(obj)	
	elif n == 8:
		obj = ParseObject.Query.get(title='Monster')
		decrement(obj)
	elif n == 9:
		obj = ParseObject.Query.get(title='DietRockstar')
		decrement(obj)			
