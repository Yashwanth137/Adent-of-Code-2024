#!/usr/bin/env python
# coding: utf-8

# In[1]:


col1 = []
col2 = []
res = 0


# In[2]:


# Part - 1
#total distance between your lists


# In[3]:


with open('input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        
        col1.append(num1)
        col2.append(num2)
        
col1.sort()
col2.sort()

for i, j in zip(col1, col2):
    res += abs(i-j)
    
print(res)


# In[4]:


# Part - 2
#similarity score


# In[5]:


from collections import Counter

num_count_list = Counter(col2)

total_score = sum(left * num_count_list[left] for left in col1)

print("Total Similarity Score:", total_score)


# In[ ]:




