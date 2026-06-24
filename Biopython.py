#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import Entrez


# In[2]:

# Set your email address (required by NCBI)
Entrez.email = "hannamelek826@gmail.com"


# In[5]:

# Fetch the E. coli genome sequence in FASTA format
handle = Entrez.efetch(
    db="nucleotide",
    id="NC_000913.3",
    rettype="fasta",
    retmode="text"
)

sequence = handle.read()

print(sequence[:500])


# In[6]:

#"bacterial_gene.fasta" = file name
#"w" = write mode
with open("ecoli.fasta", "w") as file:
    file.write(sequence)
#puts the contents of the variable sequence into the file.

# In[8]:


from Bio import SeqIO

record = SeqIO.read("ecoli.fasta", "fasta")


# In[9]:


print(record.id)
print(len(record.seq))


# In[11]:

# Fetch the E. coli genome sequence in FASTA format directly into a SeqRecord object, (fetch and parse directly)
#You don't need to save the file. You can fetch the sequence and parse it directly into a SeqRecord object using SeqIO.read() with the handle from Entrez.efetch().

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

#Suppose you don't know the accession number.
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




