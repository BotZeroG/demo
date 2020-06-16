import numpy as np

x = np.random.randint(1, high =10, size =20, dtype='int');
print("Size 20 Array generated:", x)

x = np.reshape(x, (4,5));
print("Array reshaped to 4 by 5")
print(x)

print("Replace each max value with Zero in each row:")
print(np.where(x == np.max(x, axis=1).reshape(-1,1), 0, x))