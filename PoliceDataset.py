#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# # Import .csv file

# In[119]:


data = pd.read_csv(r"C:\Users\PRAGYA GUPTA\OneDrive\Documents\MyProjects\DataAnalysisPython\PoliceData.csv")


# In[120]:


data


# # Data Cleaning

#  Que 1 : Remove columns that contains null values(missing values)

# In[121]:


data.isnull() 
# -> This will output True or False.
# -> True means places(columns) which have null value,False means places which do not have null values


# In[122]:


data.isnull().sum()
# -> Shows sum of null values column-wise
# -> 0 means that column has no null values, n(n=total no. of rows in a table) means all rows have null values(REMOVE THIS)


# This shows country_name has 65535 null values = total no. of rows
# => these column has only null values and hence of no use,and can be removed.

# In[123]:


data.drop(columns = 'country_name',inplace = True) 
# => this removes columns,to remove rows use index in place of columns
# => inplace = True permanently removes columns, without this parameter,if u fetch data it will still show all columns    


# In[124]:


data 
# since in above query we used inplace = true, country name is deleted here,else without inplace=true it will still be visible


# # Filtering Data

# Que 2 : Who were stopped more often for speed violations? Men or Women.

# In[111]:


data.head()


# In[23]:


data[data.violation == 'Speeding'].driver_gender.value_counts()
# => from que, its clear we need to use violation and gender columns.
# => .value_counts() this counts unique values in a columns


# Que 3 : Who were searched more often ? Men or Women. 

# In[112]:


data.head()


# In[33]:


data.groupby("driver_gender").search_conducted.sum()


# # Mapping Data and datatype casting

# Que 4 : Calcuate mean for stop_duration.

# In[113]:


data.head()


# In[36]:


#data["columnname"] = data['Columnname'].map({oldvalue : newvalue, oldvalue :newvalue})
# => Used for substituting each value in a Series with another value,here stop_duration value is substituted with mean value.


# In[95]:


# first i need to find all unique values in stop_duration
data.stop_duration.value_counts()


# In[125]:


# Converting above values to mean values and substituting them.
data['stop_duration'] = data['stop_duration'].map({'0-15 Min' : 7.5 ,'16-30 Min' : 23 ,'30+ Min' : 45}) 


# In[126]:


data


# In[127]:


data['stop_duration'].mean()


# # Using Group by and Describe

# Que 5 : Compare age distribution with violations

# In[130]:


data.head()


# In[132]:


data.groupby('violation').driver_age.describe()  # describe() => used to show statistical data


# # Pragya Gupta
