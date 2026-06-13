#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.DataFrame({"Sample1":[5, 10, 15, 20, 25],
    "Sample2": [6, 9, 14, 18, 30],
    "Sample3": [7, 11, 13, 19, 28],
    "Sample4": [8, 12, 16, 22, 27]
}, index=["TP53", "BRCA1", "MYC", "EGFR", "KRAS"])


# In[3]:


print(data)


# In[4]:


plt.figure(figsize=(6,4))
sns.heatmap(data, annot=True, cmap="viridis")
plt.title("Gene Expression Heatmap")
plt.show()


# In[5]:


df_melt = data.reset_index().melt(id_vars="index")
df_melt.columns = ["Gene", "Sample", "Expression"]

sns.boxplot(x = "Sample", y = "Expression", data = df_melt)
plt.show


# In[7]:


sns.scatterplot(x = data["Sample1"], y = data["Sample2"])
plt.xlabel("Sample1 Expression")
plt.ylabel("Sample2 Expression")
plt.title("Sample1 vs Sample2 Gene Expression")
plt.show


# In[ ]:




