#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.Seq import Seq


# In[2]:


dna = Seq("ATGCGT")

print(dna)


# In[3]:


print(len(dna))


# In[4]:


print(dna[0])


# In[5]:


print(dna[1:4])


# In[6]:


print(dna.count("G"))


# In[7]:


print(dna.complement())


# In[8]:


print(dna.reverse_complement())


# In[9]:


rna = dna.transcribe()

print(rna)


# In[10]:


rna = Seq("AUGCGU")

print(rna.back_transcribe())


# In[11]:


print(rna.translate())


# In[12]:


# reading fasta file using SeqIO


# In[21]:


with open("sample.fasta", "w") as f:
    f.write(">gene1\n")
    f.write("ATGCGTAGCTAG\n")
    f.write(">gene2\n")
    f.write("GGCCATATATGC\n")


# In[23]:


from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):
    print(record.id)
    print(record.seq)


# In[24]:


from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):
    print(record.id, len(record.seq))


# In[29]:


from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):

    seq = record.seq

    gc = ((seq.count("G") + seq.count("C")) / len(seq)) * 100
    
    print(record.id, gc)


# In[ ]:




