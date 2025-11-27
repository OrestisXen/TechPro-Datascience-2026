import exercise_1
import exercise_2
import time
import numpy as np


heights_list = exercise_1.getListWithRandoms(1000000,180,5)
weights_list = exercise_1.getListWithRandoms(1000000,70,10)

heights_arr = np.array(heights_list)
weights_arr = np.array(weights_list)

start = time.time()
bmi_arr = weights_arr / ((heights_arr/100)**2)

end = time.time()

print(f"{end-start} seconds elapsed")







