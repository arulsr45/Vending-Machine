from parse_rest.connection import register
register("t4WKDKIQROtp4tUHtQRyUOBGAnyTKjMv8fwlzMvB","IMTtB88bSsiWhOei0aCGJI3QIRChqUXZYBAXf0aa", master_key=None)

from parse_rest.datatypes import Object as ParseObject

obj = ParseObject.Query.get(title='coke')
print obj.title
print obj.quantity
obj.quantity -= 1
print obj.quantity
<<<<<<< HEAD
obj.save()
=======
obj.save()
>>>>>>> bacc1dcfaf83f170aec38f315ec7edabb424456a
