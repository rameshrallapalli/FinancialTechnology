
# coding: utf-8

# In[1]:


import numpy as np

import matplotlib.pyplot as plot


# In[6]:


x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plot.grid(True, which='both')
plot.axhline(y = 0, color='k')

plot.title('Sine and Cosine')
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.plot(x,y,x,z)
plot.show()

