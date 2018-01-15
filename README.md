# Recommendation-System
We will be building very basic recommendation system using python.To build a recommendation system,
we will use the Dataset from Movie-Lens.So,let us now move ahead and build the recommendation model.

# Dataset
The dataset that we are going to use for building the recommendation system is the
famous movie-lens dataset which contains the multiple csv file in a single folder
"ml-100k" which can download the link:http://files.grouplens.org/datasets/movielens/ml-100k.zip.

We will be using the following files from the data:

<p>"u.item": It contains information about the items i.e. movies and all other information related to it.</p>
<p>“u.data”: It contains the information about the users and the movie ratings.</p>
<p>“u.user”: It contains information about the users such as age, gender etc.</p>
Your recommendation system in 10 steps

<p>The first step is to load the required libraries, so let us load the required libraries using the import() function.</p>

 
# Loading the required libraries
<p>import os</p>
<p>import pandas as pd</p>
<p>import numpy as np</p>
<p>import matplotlib.pyplot as plt</p>
2.Set the working directory to the location where you downloaded the data

# Set your work directory to where the data is located
os.chdir("C://Users/Your-username/Desktop/ml-100k/")
<p>3. You can get the details about the data files in a description file in the data folder, so let us assign the variable names or column names to each data.</p>

#column headers for the dataset
<p>data_cols = ['user id','movie id','rating','timestamp']</p>
<p>item_cols = ['movie id','movie title','release date',
'video release date','IMDb URL','unknown','Action',
'Adventure','Animation','Childrens','Comedy','Crime',
'Documentary','Drama','Fantasy','Film-Noir','Horror',
'Musical','Mystery','Romance ','Sci-Fi','Thriller',
'War' ,'Western']</p>
<p>user_cols = ['user id','age','gender','occupation',
'zip code']</p>
4. Now, load the data files using pandas read_csv() function.

#importing the data files onto dataframes
<p>users = pd.read_csv('u.user', sep='|',
names=user_cols, encoding='latin-1')</p>
<p>item = pd.read_csv('u.item', sep='|',
names=item_cols, encoding='latin-1')</p>
<p>data = pd.read_csv('u.data', sep='\t',
names=data_cols, encoding='latin-1')</p>
5.  In the next step, we will see the first few rows of each of the datasets that we have loaded.

<p>users.head()</p>


<p>item.head()</p>


<p>data.head()</p>
6. Now, in the next step, we will print the information on all the datasets using info() function.

<p>print(users.info())</p>


<p>print(item.info())</p>


<p>print(data.info())</p>
7. Create a merged data-frame of all the datasets based on a similar column.

# Create a merged dataframe
<p>df = pd.merge(pd.merge(item, data), users)</p>
8. Now, in the next step we will group by the movies based on their titles

# Group by Movies by their title
<p>ratings_total = df.groupby('movie title').size()</p>
<p>print(ratings_total.head())</p>


# Take the mean ratings of each movie using the mean function
<p>ratings_mean = (df.groupby('movie title'))['movie title','rating'].mean()</p>
print(ratings_mean.head())
 <p>Now if you check ratings-total then you will find it is as a Series and not a Data Frame. So, we need to convert it into data-frame.</p>

# Modify the dataframes so that we can merge the two
# Now we sort the values by the total rating
<p>ratings_total = pd.DataFrame({'movie title':ratings_total.index,
'total ratings': ratings_total.values})</p>
<p>ratings_mean['movie title'] = ratings_mean.index</p>
<p>10. Finally, we need to sort the values by the total ratings and then these movies can be recommended to each of the user.</p>

# Now we sort the values by the total rating
<p>final = pd.merge(ratings_mean, ratings_total).sort_values(by = 'total ratings',
ascending= False)</p>
<p>print(final.describe())</p>


<p>print(final.head())</p>

