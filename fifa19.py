9# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Udayan\Desktop\Data Science Codingnest\datasets\fifa19_data.csv')

df.head()

df1 = df[df['Value'].notnull()]

df1.shape
df.shape

pd.__version__

# NOT WORKING -- df1.loc[:,['Value']] = [pd.to_numeric(x[1:-1])*1000 for x in df1.Value if x[-1] == 'M']

# NOT WORKING -- df1['Value'] = [pd.to_numeric(x[1:-1])*1000 for x in df1.Value if x[-1] == 'M']

df.Value = [x[1:-1] for x in df.Value]

## df['Value'] = df['Value'].astype(float) ----- not working

df['Value'] = pd.to_numeric(df['Value'])

df['Value'].head()

df.Wage = [x[1:-1] for x in df.Wage]

df['Wage'] = pd.to_numeric(df['Wage'])

df['Wage'].head()

#df = sns.load_dataset(r"C:\Users\Udayan\Desktop\Data Science Codingnest\datasets\fifa19_data.csv")

#sns.barplot(x = 'Nationality',y = 'Age', data = df)

df.dtypes

df_top5 = df[df['Nationality'].isin(["Argentina", "Brazil", "Spain", "Portugal", "England"])]

df_top15 = df[df['Nationality'].isin(["Argentina", "Brazil", "Spain", "Portugal", "England",
             "Germany", "France","Belgium","Croatia","Uruguay","Slovenia","Poland","Italy",
             "Egypt", "Denmark"])]

# NOT WORKING -- df_top15['Value'] = df_top15['Value'].apply(lambda x: pd.to_numeric(x[1:-1])*1000 if x[-1] == 'M')

# NOT WORKING -- df_top15['Value'] = df_top15['Value'].apply(lambda x: (x[1:-1].astype(float))*1000 if x[-1] == 'M')

# NOT WORKING -- df_top15['Value'] = [x[1:-1].astype(float))*1000 for x in df_top15.Value if x[-1] == 'M']

# NOT WORKING -- df_top15['Value'] = [pd.to_numeric(x[1:-1])*1000 for x in df_top15.Value if x[-1] == 'M']

# NOT WORKING -- df_top15.Value.str.replace('€|M|K','').astype(float).apply(lambda x:x*1000  if  ))

df_top5.shape

#plt.figure(figsize=(8, 6))
#sns.barplot(x = 'Nationality',y = 'Age', data = df_top15)
#plt.xticks(rotation=90,fontsize='large')

#sns.barplot(x = 'Age',y = 'Nationality', data = df_top15)

plt.figure(figsize=(8,6))
sns.lineplot(x='Nationality',y='Value',data=df_top15)
sns.lineplot(x='Nationality',y='Wage',data=df_top15)
plt.xticks(rotation=90,fontsize='large')

#plt.figure(figsize=(8,6))
#sns.boxplot('Nationality', 'Age', data = df_top15)
#plt.xticks(rotation=90,fontsize='large')

#===================== VIOLIN PLOT BETWN AGE AND NATIONALITY =====================#
plt.figure(figsize=(8,6))
sns.violinplot('Nationality', 'Age', data = df_top15)
plt.xticks(rotation=90,fontsize='large')

#================ IR of Players basis of foot ====================================#
sns.countplot('International Reputation', data = df_top15, hue = 'Preferred Foot')

#================ Count of Players Nation wise basis of foot ====================================#
sns.countplot('Nationality', data = df_top15, hue = 'Preferred Foot')
plt.xticks(rotation=90,fontsize='large')

#================ Nationality with body type ====================================#
plt.figure(figsize=(8,6))
sns.countplot('Nationality', data = df_top5, hue = 'Body Type')

#================ Position and Preferred foot ====================================#
plt.figure(figsize=(15,5))
sns.countplot('Position', data = df_top15, hue = 'Preferred Foot')



df['Height'].dtypes

sns.barplot(x = 'Weight', y = 'Overall', data = df_top5)