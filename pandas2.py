#!/usr/bin/env python
# coding: utf-8

# In[1]:


# day 10 pandas merge, sort, apply


# In[2]:


import pandas as pd


# In[3]:


expr = pd.DataFrame({"Gene":["TP53","BRCA1","MYC"], "Expression":[50,120,80]})
print(expr)


# In[6]:


gc = pd.DataFrame({"Gene":["TP53","BRCA1","MYC"], "GC_content":[55,48,69]})
print(gc)


# In[7]:


merged = pd.merge(expr, gc, on="Gene")
print(merged)


# In[9]:


sorted_df = merged.sort_values("GC_content")
print(sorted_df)


# In[11]:


sorted_df = merged.sort_values("GC_content", ascending = False)
print(sorted_df)


# In[12]:


def label_gene(x):
    if x > 100:
        return "High"
    else:
        return "Low"


# In[13]:


merged["Status"] = merged["Expression"].apply(label_gene)
print(merged)


# In[14]:


data = {
    "Gene": ["TP53", "BRCA1", None, "MYC"],
    "Expression": [50, None, 90, 80]
}

df = pd.DataFrame(data)

print(df)


# In[15]:


print(df.isnull())


# In[16]:


clean_df = df.dropna()
print(clean_df)


# In[20]:


filtered = sorted_df[sorted_df["Expression"] > 100]
print(filtered)  




# In[ ]:




