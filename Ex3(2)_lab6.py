
# coding: utf-8

# In[38]:

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

import numpy as np
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
n = int(input())
percentiles = get_percentile(values, n)
print(percentiles)
get_percentile_number(float(input()), percentiles)

