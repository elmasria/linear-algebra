from math import sqrt, acos, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No Parallel Component"
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No Orthogonal Component"
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = "Only defined in 2 or 3 dimensions"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

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
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,
            v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, scalar):
        new_coordinates = [Decimal(scalar)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def get_magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

    def get_magnitude_using_dot_product(self):
        return sqrt(self.dot_product(self))

    def normalize_vector(self):
        try:
            magnitude = self.get_magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_product(self, v):
        dot_product_coordinates = [x*y for x,y in zip(self.coordinates,
            v.coordinates)]
        return sum(dot_product_coordinates)

    def calculate_angle(self, v, degree = False):
        try:
            w_magnitude = self.get_magnitude()
            v_magnitude = v.get_magnitude()
            theta = acos(self.dot_product(v)/(w_magnitude*v_magnitude))
            if degree:
                return degrees(theta)
            else:
                return theta

        except Exception as e:
            raise Exception('Cannot normalize the zero vector')

    def check_orthogonal_vectors(self, v, tolerance=1e-10):
        return abs(self.dot_product(v)) < tolerance

    def check_parallel_vectors(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.calculate_angle(v, True) == 0 or
                self.calculate_angle(v, True) == 180)

    def is_zero(self, tolerance=1e-10):
        return self.get_magnitude() < tolerance

    def component_parallel_to(self, basis):
        try:
            u = basis.normalize_vector()
            weight = self.dot_product(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e


    def cross_product(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates

            x = y_1*z_2 - y_2*z_1
            y = -(x_1*z_2 - x_2*z_1)
            z = x_1*y_2 - x_2*y_1

            cross_vector = Vector([x, y, z])
            return cross_vector
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embeded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross_product(v_embeded_in_R3)
            elif (msg == 'too many values to unpack' or
                msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
        else:
            raise e


    def parallelogram_area(self, v):
        cross_vector = self.cross_product(v)
        return cross_vector.get_magnitude()

    def triangle_area(self, v):
        cross_vector = self.cross_product(v)
        return cross_vector.get_magnitude()* Decimal(0.5)