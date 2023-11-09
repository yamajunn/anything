import math
import numpy as np

x, y, z = 10, 10, 10

me_x, me_y, me_z = 0, 0, 0

distance_array = np.array([abs(x-me_x), abs(y-me_y), abs(z-me_z)])
distance_array = distance_array ** 2
distance_root = distance_array.sum()

distance = math.sqrt(distance_root)
print(distance)

display_list = [" " for i in range(8000)]
for i in range(40):
    display_list[i*200]="\n"

display_list[80+200*10] = "#"
display_list[120+200*10] = "#"
display_list[80+200*30] = "#"
display_list[120+200*30] = "#"


display_str = "".join(display_list)
print(display_str)