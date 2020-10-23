#!/usr/bin/env python
# coding: utf-8

# In[1]:


#exercice 2 
#1)

import matplotlib.pyplot as plt
from numpy import linspace
f=lambda x: x**3+x**2-3*x-3
T=linspace(-2,2,41)
plt.title("solution dans [-2:2] ");
plt.xlabel("x")
plt.ylabel ("f(x)")
plt.grid(True)
plt.plot(T,f(T))


# In[50]:


#2)
def dicho(f,a,b,eps):
    m=(a+b)/2
    err=abs(b-a)
    while err>eps: 
        if f(m)==0: 
            return m
    
        elif f(a)*f(m)<0: 
            b=m
        else: 
            a=m
         
        m=(a+b)/2
        err=abs(b-a)
        x=m
              


# In[51]:


x1=dicho(f,-2,2,0.001)
print(x1)


# In[ ]:




