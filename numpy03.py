# Array Search
import numpy as np

arr = np.array([1,2,3,4,5,7,4,41,2,3,4,5,6,7,8,9,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33])

x = np.where(arr%2 == 0)
print("\nBulunan çift sayıların yeri .where(arr%2 == 0) :",x)