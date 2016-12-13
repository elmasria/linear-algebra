from vector import Vector


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