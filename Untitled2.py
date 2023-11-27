#!/usr/bin/env python
# coding: utf-8

# ### Assignment

# In[10]:


def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# In[8]:


calculate_grade(90)


# In[11]:


calculate_grade(80)


# In[12]:


calculate_grade(70)


# In[13]:


calculate_grade(60)


# In[14]:


calculate_grade(50)


# ### ASSG

# In[1]:


def is_even(integer):
    if integer % 2 == 0:
        print('even')
    else:
        print('odd')


# In[2]:


is_even(4)


# In[4]:


is_even(7)


# In[5]:


def calculate_area(l, b):
    return l * b


# In[6]:


calculate_area(5, 6)


# In[26]:


def is_triangle(x,y,z):
    if (x+y)>z:
        return 'True'
    elif (y+z)>x:
        return 'True'
    elif (x+z)>y:
        return 'True'
    else:
        return 'False'
  


# In[29]:


is_triangle(2,5,8)


# In[25]:


is_triangle(1,1,6)


# In[10]:


is_triangle(10,6,4)


# In[19]:


def max_of_three(x,y,z):
    if x>z and x>y:
        return 'X'
    elif y>x and y>z:
        return 'Y'
    else:
        return 'Z'



# In[21]:


max_of_three(4,8,12)


# ### Assignment 2

# In[51]:


def is_palindrome(string):
    length = len(string)
    first = 0
    last = length - 1
    status = 1
    while(first<last):
        if(string[first]==string[last]):
            first = first +1
            last = last -1
        else:
            status = 0
            break
        return 'True'
    return 'false'
    


# In[52]:


is_palindrome('tokyo')


# In[53]:


is_palindrome('madam')


# In[ ]:





# In[ ]:




