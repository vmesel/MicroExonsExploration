
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv("/home/vinicius/Dropbox/Vinicius/Iniciação Científica/2018 - MicroExons/Dados/microexon_transcripts.csv")


# In[4]:


df


# In[6]:


df = df[df["gene_type"] == "protein_coding"]


# In[12]:


df.drop(columns=["ind"])

