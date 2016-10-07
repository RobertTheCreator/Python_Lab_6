
# coding: utf-8

# In[37]:

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
    
import numpy as np
import random
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
n = int(input())
percentiles = get_percentile(values, n)
print(percentiles)
for i in range(len(values)):
    values[i] = value_equalization(values[i], percentiles, False)
print(values)

