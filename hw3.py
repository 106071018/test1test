
# coding: utf-8

# In[1]:


def aaa(x):
    bbb=dict()
    for ccc in x:
        if ccc not in bbb:
            bbb[ccc]=1
        else:
            bbb[ccc]+=1
    return bbb


# In[16]:


sen=input('Please type anything:''\n')
for item in aaa(sen).items():
    zzz,xxx=item
    print("'"+str(zzz)+"' = '"+str(xxx)+"'")

