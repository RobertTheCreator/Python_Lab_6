
# coding: utf-8

# In[4]:

import random

n = int(input())
S = 0
for i in range(1, n+1):
    u_i = random.uniform(-3, 3)
    if -2 <= u_i <= 2:
        S = S + (6/n)*(-u_i**2 + 4)
print(S)

