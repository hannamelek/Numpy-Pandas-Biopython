#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import Entrez


# In[2]:


Entrez.email = "hannamelek826@gmail.com"


# In[5]:


handle = Entrez.efetch(
    db="nucleotide",
    id="NC_000913.3",
    rettype="fasta",
    retmode="text"
)

sequence = handle.read()

print(sequence[:500])


# In[6]:


with open("ecoli.fasta", "w") as file:
    file.write(sequence)


# In[8]:


from Bio import SeqIO

record = SeqIO.read("ecoli.fasta", "fasta")


# In[9]:


print(record.id)
print(len(record.seq))


# In[11]:


from Bio import Entrez, SeqIO

Entrez.email = "hannamelek826@gmail.com"

handle = Entrez.efetch(
    db="nucleotide",
    id="NC_000913",
    rettype="fasta",
    retmode="text"
)

record = SeqIO.read(handle, "fasta")

print(record.id)
print(len(record.seq))


# In[13]:


from Bio import Entrez

Entrez.email = "hannamelek826@gmail.com"

handle = Entrez.esearch(
    db="nucleotide",
    term="Escherichia coli recA"
)

record = Entrez.read(handle)

print(record["IdList"])


# In[15]:


from Bio import Entrez

Entrez.email = "hannamelek826@gmail.com"

handle = Entrez.efetch(
    db="nucleotide",
     id="3347424143",
    rettype="fasta",
    retmode="text"
)

print(handle.read()[:500])
    


# In[ ]:




