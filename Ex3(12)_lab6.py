
# coding: utf-8

# In[22]:

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imag


a = []
with open('img.txt', 'r') as img:
    for line in img:
        v = list(map(float, line.strip().split(" ")))
        a.append(v)
a = np.array(a)
data = a
vector = data.flatten()
new_data = vector.reshape(data.shape)
sequence = [0]*200
for i in range(200):
    sequence[i] = new_data[i] 

pool = [0]*100
for i in range(100):
    pool[i] = random.choice(sequence)
    
plt.imshow(pool, cmap = plt.get_cmap('gray'))
plt.show()

