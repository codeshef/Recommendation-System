# Recommendation-System
We will be building very basic recommendation system using python.To build a recommendation system,
we will use the Dataset from Movie-Lens.So,let us now move ahead and build the recommendation model.

# Dataset
The dataset that we are going to use for building the recommendation system is the
famous movie-lens dataset which contains the multiple csv file in a single folder
"ml-100k" which can download the link:http://files.grouplens.org/datasets/movielens/ml-100k.zip.

We will be using the following files from the data:

"u.item": “u.item”: It contains information about the items i.e. movies and all other information related to it.
“u.data”: It contains the information about the users and the movie ratings.
“u.user”: It contains information about the users such as age, gender etc.
Your recommendation system in 10 steps

The first step is to load the required libraries, so let us load the required libraries using the import() function.

 
# Loading the required libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
2.Set the working directory to the location where you downloaded the data

# Set your work directory to where the data is located
os.chdir("C://Users/Your-username/Desktop/ml-100k/")
3. You can get the details about the data files in a description file in the data folder, so let us assign the variable names or column names to each data.

#column headers for the dataset
data_cols = ['user id','movie id','rating','timestamp']
item_cols = ['movie id','movie title','release date',
'video release date','IMDb URL','unknown','Action',
'Adventure','Animation','Childrens','Comedy','Crime',
'Documentary','Drama','Fantasy','Film-Noir','Horror',
'Musical','Mystery','Romance ','Sci-Fi','Thriller',
'War' ,'Western']
user_cols = ['user id','age','gender','occupation',
'zip code']
4. Now, load the data files using pandas read_csv() function.

#importing the data files onto dataframes
users = pd.read_csv('u.user', sep='|',
names=user_cols, encoding='latin-1')
item = pd.read_csv('u.item', sep='|',
names=item_cols, encoding='latin-1')
data = pd.read_csv('u.data', sep='\t',
names=data_cols, encoding='latin-1')
5.  In the next step, we will see the first few rows of each of the datasets that we have loaded.

users.head()


item.head()


data.head()
6. Now, in the next step, we will print the information on all the datasets using info() function.

print(users.info())


print(item.info())


print(data.info())
7. Create a merged data-frame of all the datasets based on a similar column.

# Create a merged dataframe
df = pd.merge(pd.merge(item, data), users)
8. Now, in the next step we will group by the movies based on their titles

# Group by Movies by their title
ratings_total = df.groupby('movie title').size()
print(ratings_total.head())


# Take the mean ratings of each movie using the mean function
ratings_mean = (df.groupby('movie title'))['movie title','rating'].mean()
print(ratings_mean.head())
 Now if you check ratings-total then you will find it is as a Series and not a Data Frame. So, we need to convert it into data-frame.

# Modify the dataframes so that we can merge the two
# Now we sort the values by the total rating
ratings_total = pd.DataFrame({'movie title':ratings_total.index,
'total ratings': ratings_total.values})
ratings_mean['movie title'] = ratings_mean.index
10. Finally, we need to sort the values by the total ratings and then these movies can be recommended to each of the user.

# Now we sort the values by the total rating
final = pd.merge(ratings_mean, ratings_total).sort_values(by = 'total ratings',
ascending= False)
print(final.describe())


print(final.head())

