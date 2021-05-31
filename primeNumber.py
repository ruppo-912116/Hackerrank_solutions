#!/usr/bin/env python
# coding: utf-8

# ## Prime numbers calculation

# In[9]:


lower = int(input("enter the lower range "))
upper = int(input("enter the higher range "))
arr =[]
diff = []
for num in range(lower,upper+1):
    if(num>1):
        for i in range(2,num):
            if (num%i ==0):
                break
        else:
            arr.append(num)
for i in arr:
    print(num)
    num = i - num
    diff.append(num)
    num = i
    
print(diff)
    
            
            


# In[6]:


arr


# In[7]:


diff


# In[ ]:




