
# coding: utf-8

# In[57]:

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
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.show()

