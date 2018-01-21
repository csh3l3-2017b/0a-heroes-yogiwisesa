
# coding: utf-8

# In[15]:


# YOGI WISESA CHANDRA  1301154282 IF 39-02
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
name = []
role = []
data = pd.read_csv('test.csv')
for i in range(len(data)):
    name.append(data["name"][i])
    if (data["movementSpeed"][i] >= 270):
        role.append("MARKSMAN")
    elif (data["mana"][i] >= 500):
        role.append("MAGE")
    elif (data["armor"][i] >= 25):
        role.append("TANK")
    elif (data["physicalAttack"][i] >= 121):
        role.append("ASSASSIN")
    elif (data["hp"][i] >= 2580):
        role.append("FIGHTER")
    else:
        role.append("SUPPORT")
        
raw_data = { 'name' : name, 'role':role}
df = pd.DataFrame(raw_data, columns = ['name', 'role'])
df.to_csv('prediction.csv', index=False)

