#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# day 9 pandas and reading csv files, filtering and groupby


# In[1]:

#creating a pandas DataFrame from a dictionary
import pandas as pd


# In[3]:


genes = {"Genes":["TP53", "BRCA1", "MYC"], "Expression":[50, 120, 80]}

df = pd.DataFrame(genes)

print(df)


# In[13]:

#Read a CSV File
import pandas as pd

df = pd.read_csv(r"C:\Users\Dr.MAAM\Downloads\genes.csv")

print(df)



# In[14]:


print(df.head())
print(df.columns)


# In[16]:


print(df["type"])


# In[18]:

#Filter Rows Based on a Condition
high_exp = df[df["expression"] > 100]

print(high_exp)


# In[21]:


data = {"gene":["TP53","BRCA1","MYC","EGFR"], 
        "Type": ["Tumor","Tumor","Oncogene","Oncogene"], 
        "Expression": [50,120,80,200]}
df = pd.DataFrame(data)

print(df)


# In[22]:

#Group By and Aggregate
results = df.groupby("Type")["Expression"].mean()
print(results)


# In[26]:


import pandas as pd

df = pd.read_csv(r"C:\Users\Dr.MAAM\Downloads\genes2.csv")

print("All genes:")
print(df)

high_exp = df[df["expression"]>100]

print("\nHighly expressed genes:")
print(high_exp)


# In[ ]:




