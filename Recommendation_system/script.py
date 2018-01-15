# first step is to load the required libraries

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set the working directory to the location where you downloaded the data

os.chdir("/media/anchal/48546e8c-50cb-4e45-9c5b-aa423450531b/PythonPractice/Recommendation_system/ml-100k/")

# assign variable and column name to each data

# column headers for the dataset

data_cols = ['user id','movie id','rating','timestamp']
item_cols = ['movie id','movie title','release date',
'video release date','IMDb URL','unknown','Action',
'Adventure','Animation','Childrens','Comedy','Crime',
'Documentary','Drama','Fantasy','Film-Noir','Horror',
'Musical','Mystery','Romance ','Sci-Fi','Thriller',
'War' ,'Western']
user_cols = ['user id','age','gender','occupation',
'zip code']

# load the data files using pandas read_csv() function

users  = pd.read_csv('u.user',sep='|',names=user_cols,encoding='latin-1')
item = pd.read_csv('u.item',sep='|',names=item_cols,encoding='latin-1')
data = pd.read_csv('u.data',sep='\t',names=data_cols,encoding='latin-1')

users.head()
item.head()
data.head()

#print(users.info())
#print(item.info())
#print(data.info())

# create  a merged dataframe

df = pd.merge(pd.merge(item,data),users)

# group the movies based on their titles

ratings_total = df.groupby('movie title').size()
print(ratings_total.head())

# take the mean ratings of each movie using the mean function

ratings_mean = (df.groupby('movie title'))['movie title','rating'].mean()
print(ratings_mean.head())

# need to convert it into data-frame
# now we sort the values by the total rating

ratings_total =  pd.DataFrame({'movie title':ratings_total.index,
'total ratings': ratings_total.values})
ratings_mean['movie title'] = ratings_mean.index

# now we sort the values by the total rating
final = pd.merge(ratings_mean, ratings_total).sort_values(by = 'total ratings',
ascending= False)
print(final.describe())

print(final.head())
