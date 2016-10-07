
# coding: utf-8

# In[ ]:

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imag

def get_percentile(values, bucket_number):
    a = [0]*bucket_number
    for i in range(bucket_number):
        a[i] = np.percentile(values, (100/bucket_number)*i)
    a[0] = 0.0
    return((a))

def get_percentile_number(value, percentiles):
    a = get_percentile(values, n)
    k = -1
    if value < a[0]:
        return(0)
    else:
        for i in range(n):
            if a[i] <= value:
                k += 1
        return(k)

def value_equalization(value, percentiles, add_random):
    idx = get_percentile_number(value, percentiles)
    step = 1/len(percentiles)
    random_noise = random.uniform(idx*step, (idx+1)*step)/100
    if add_random == True:
        new_value = idx*step + random_noise
        return new_value
    else:
        new_value = idx*step
        return new_value

def values_equalization(values, percentiles, add_random):
    for i in range(len(values)):
        values[i] = value_equalization(values[i], percentiles, True)
    return values

a = []
with open('img.txt', 'r') as img:
    for line in img:
        v = list(map(float, line.strip().split(" ")))
        a.append(v)
a = np.array(a)
data = a
values = data.flatten()
n = int(input())
percentiles = get_percentile(values, n)


plt.subplot(221)
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.colorbar()

plt.subplot(222)
plt.hist(values)

plt.subplot(223)
vector = data.flatten()
vector = values_equalization(vector, percentiles, False)
new_data = vector.reshape(data.shape)
plt.imshow(new_data,  cmap = plt.get_cmap('gray'))
plt.colorbar()

plt.subplot(224)
plt.hist(vector)

plt.show()

