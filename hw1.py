
# coding: utf-8

# In[1]:


import numpy as np

import matplotlib.pyplot as plot


# In[6]:


x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

#Adding Tangent for Assignment - Venkata
t = np.tan(x)
#Creating a Top level container for all plot elements - Venkata
fig = plot.figure()

plot.grid(True, which='both')
plot.axhline(y = 0, color='k')

plot.title('Sine and Cosine')
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.plot(x,y,x,z)
plot.show()

#Saving the graph localli - venkata
# we can set the path here based on where we wanted to save- by default it save in same location where the python script exist- venkata
fig.savefig('sine_cosine_tangent.png')

