from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,
            v.coordinates)]
        return new_coordinates

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,
            v.coordinates)]
        return new_coordinates

    def times_scalar(self, scalar):
        new_coordinates = [scalar*x for x in self.coordinates]
        return new_coordinates

    def get_magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalize_vector(self):
        try:
            magnitude = self.get_magnitude()
            return self.times_scalar(1./magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


# Tester
# Addition
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print v.plus(w)

# Subtraction 
v = Vector([7.119, 8.125])
w = Vector([-8.223, 0.878])
print v.minus(w)

# Scaling 
v = Vector([1.671, -1.012, -0.318])
c = 7.41
print v.times_scalar(c)

v = Vector([-0.221, 7.437])
print v.get_magnitude()

v = Vector([8.813, -1.331, -6.247])
print v.get_magnitude()

v = Vector([5.581, -2.136])
print v.normalize_vector()


v = Vector([1.996, 3.108, -4.554])
print v.normalize_vector()