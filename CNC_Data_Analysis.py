# CNC_Data_Analysis
"""
Exploring the possible ML models that can be used with a CNC data set that I found on Kaggle. 

Using this knowledge to help me understand the possibilities of using ML at work to help understand tool wear
"""
#%%  Libraries
# Numerical
import numpy as np
import pandas as pd
# Viz
import matplotlib.pyplot as plt
import seaborn as sns
# Viz Settings
sns.set_style(style='darkgrid')
# Importing Files
import glob
#%% Import CNC Data
# List of Data Files & Locations
path = r'F:\Work - Detroit Diesel\CNC_Machining_Dataset'
filenames = glob.glob(path + '/experiment*.csv')

# Making a list of DFs (1 DF per CSV file)
li = []
i = 1
for file in filenames:
    dfs = pd.read_csv(file,index_col=None,header=0)                             # Making DF for each dataset
    dfs['exp_no'] = i                                                           # Identifying the exp number
    i += 1                                                                      # Iterating through exp numbers
    li.append(dfs)                                                              # Appending the DF to the outside list

# Concatendating all individual DFs together
## If headers are the same, then each new item is concatenated to the end
df = pd.concat(li,ignore_index=True)

#%% Importing Experiment Results Data
exp_result = pd.read_csv(r'F:\Work - Detroit Diesel\CNC_Machining_Dataset\train.csv')

# Cleaning Exp Data
exp_result['passed_visual_inspection'].fillna('no',inplace=True)

#%% Merging Exp Results & CNC Data
df_final = df.merge(exp_result,right_on='No',left_on='exp_no',how='left')
df_final.drop('No',axis=1,inplace=True)

#%% Exploratory Data Analysis
plt.figure(figsize=(12,6))
sns.countplot(data=df_final,
              x='Machining_Process'
             )

#%% Data Cleansing
df_final['Machining_Process'].replace(to_replace=('end','Starting'),value=('End','Prep'),inplace=True)

#%% Exploratory Data Analysis Cont.
plt.figure(figsize=(12,6))
sns.countplot(data=df_final,
              x='Machining_Process'
             )

plt.figure(figsize=(12,6))
sns.countplot(data=df_final,
              x='tool_condition'
             )

plt.figure(figsize=(12,6))
sns.countplot(data=df_final,x='machining_finalized')