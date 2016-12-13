from vector import Vector


# Tester

# Addition
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
#print v.plus(w)

# Subtraction
v = Vector([7.119, 8.125])
w = Vector([-8.223, 0.878])
#print v.minus(w)

# Scaling
v = Vector([1.671, -1.012, -0.318])
c = 7.41
#print v.times_scalar(c)

# Magnitude
v = Vector([-0.221, 7.437])
#print v.get_magnitude()

v = Vector([8.813, -1.331, -6.247])
#print v.get_magnitude()
#print v.get_magnitude_using_dot_product()

# Normalization
v = Vector([5.581, -2.136])
#print v.normalize_vector()


v = Vector([1.996, 3.108, -4.554])
#print v.normalize_vector()


# dot Product
v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
#print v.dot_product(w)

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
#print v.dot_product(w)

# Angle
v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])
#print v.calculate_angle(w)

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
#print v.calculate_angle(w, True)

# Parallel or Orthogonal
v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])
print v.check_orthogonal_vectors(w)
print v.check_parallel_vectors(w)

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print v.check_orthogonal_vectors(w)
print v.check_parallel_vectors(w)


v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print v.check_orthogonal_vectors(w)
print v.check_parallel_vectors(w)


v = Vector([2.118, 4.827])
w = Vector([0, 0])
print v.check_orthogonal_vectors(w)
print v.check_parallel_vectors(w)