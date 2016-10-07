
# coding: utf-8

# In[20]:

def get_percentile(values, bucket_number):
    a = [0]*bucket_number
    for i in range(bucket_number):
        a[i] = np.percentile(values, (100/bucket_number)*i)
    a[0] = 0.0
    return((a))

import numpy as np
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
n = int(input())
get_percentile(values, n)

