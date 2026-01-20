import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a ** 2)

print(np.mean(a))
print(np.sum(a))
print(np.max(a))
print(np.min(a))

print(a.reshape(2, 2))

print(a[2])
print(a[1:3])

print(a > 2)
print(a[a > 2])

print(np.sort(b))

print(np.random.randint(1, 10, (2, 2)))
