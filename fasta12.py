#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.Seq import Seq


# In[2]:


dna = Seq("ATGCGT")

print(dna)


# In[3]:

#length of the sequence
print(len(dna))


# In[4]:

#accessing individual nucleotides
print(dna[0])


# In[5]:

#slicing the sequence
print(dna[1:4])


# In[6]:

#counting the number of G's in the sequence
print(dna.count("G"))


# In[7]:

#complement of the sequence
print(dna.complement())


# In[8]:

#reverse complement of the sequence
print(dna.reverse_complement())


# In[9]:

#transcribing DNA to RNA
rna = dna.transcribe()

print(rna)


# In[10]:

#back-transcribing RNA to DNA
rna = Seq("AUGCGU")

print(rna.back_transcribe())


# In[11]:

#translating RNA to protein
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

#reading fasta file using SeqIO
from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):
    print(record.id)
    print(record.seq)


# In[24]:

#calculating the length of each sequence in the fasta file
from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):
    print(record.id, len(record.seq))


# In[29]:

#calculating the GC content of each sequence in the fasta file
from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):

    seq = record.seq

    gc = ((seq.count("G") + seq.count("C")) / len(seq)) * 100
    
    print(record.id, gc)


# In[ ]:




