import math
import numpy as np

x, y, z = 10, 10, 10

me_x, me_y, me_z = 0, 0, 0

distance_array = np.array([abs(x-me_x), abs(y-me_y), abs(z-me_z)])
distance_array = distance_array ** 2
distance_root = distance_array.sum()

distance = math.sqrt(distance_root)
print(distance)