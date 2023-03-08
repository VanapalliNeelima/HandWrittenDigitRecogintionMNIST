#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install tensorflow')


# In[4]:


from tensorflow.keras.datasets import mnist
(X_train,Y_train),(X_test,Y_test) = mnist.load_data()


# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


sample=1
image=X_train[sample]

fig=plt.figure
plt.imshow(image,cmap="gray")
plt.show


# In[13]:


fig=plt.figure
plt.imshow(image,cmap="gray_r")
plt.show


# In[16]:


num=10
images=X_train[:num]
labels=Y_train[:num]
print(images)
print(labels)


# In[27]:


num=10
images=X_train[:num]
labels=Y_train[:num]

num_row=2
num_col=5

fig,axes=plt.subplots(num_row,num_col,figsize = (1.5*num_col,2*num_row))

for i in range(num):
    ax = axes[i//num_col,i%num_col]
    ax.imshow(images[i],cmap='gray')
    ax.set_title('Label:{}'.format(labels[i]))
plt.tight_layout()
plt.show()

