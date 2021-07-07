#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import csv 
import numpy as np

df = pd.read_csv (r'/Users/sukarmaparimoo/Documents/Studies/CMU/ML_AI_Course/Python_Assignment/RatingsInput.csv')
new = df["MovieName"].str.split(",", n = 1, expand = True)
df["MovieID"]= new[0]
df["MovieName"]= new[1].str.capitalize()
df_sorted=df.sort_values(by=['UserAge', 'Rating'], ascending=(True, False))
data = df_sorted[df_sorted['Rating'] >= 3]


# In[38]:


dict_1 = {}
for index,row in data.iterrows():
    age = row['UserAge']
    rating = row['Rating']
    #print(rating)
    movieName = row['MovieName']
    
    if age not in dict_1:
        dict_2 = {}
        dict_2[rating] = [movieName]
        dict_1[age] = dict_2    
        
    else:
        dict_2 = dict_1[age]
        if rating not in dict_2:
            dict_2[rating] = [movieName]
        else:
            mn = dict_2[rating]
            mn.append(movieName)
                                  
def recommend_movies(x,y):
    list_of_movies = []
    if x in dict_1:
        movies = list(dict_1[x].values())
        #return movies
        #print(movies)
        new_list = []
        for i in movies:
            for j in i:
                new_list.append(j)
        list_of_movies=new_list[0:y]
    else:
        age_arr = list(dict_1.keys())
        diff_arr = abs(np.array(age_arr) - x)
        #print(diff_arr)
        closest_age = age_arr[np.argmin(diff_arr)]
        if closest_age in dict_1:
            movies = list(dict_1[closest_age].values())
        new_list_movies = []
        for i in movies:
            for j in i:
                new_list_movies.append(j)
        list_of_movies=new_list_movies[0:y]
        
    return list_of_movies


# In[39]:


input_file = pd.read_csv (r'/Users/sukarmaparimoo/Documents/Studies/CMU/ML_AI_Course/Python_Assignment/NewUsers.csv')
#print(input_file)


# In[40]:


final_list = []
for i,row in input_file.iterrows():
    x = row ['UserAge']
    y = row ['NoOfMoviesToRecommend']
#     print(x,y)
    list_of_movies = recommend_movies(x,y)
#     print(list_of_movies)
    final_list.append(list_of_movies)
#print(final_list)


# In[41]:


dfi = pd.read_csv (r'/Users/sukarmaparimoo/Documents/Studies/CMU/ML_AI_Course/Python_Assignment/NewUsers.csv')
dfi['Movies'] = final_list
#print(dfi['Movies'])
dfi.to_csv('/Users/sukarmaparimoo/Documents/Studies/CMU/ML_AI_Course/Python_Assignment/RecommendedMovieOutput.csv')


# In[ ]:





# In[ ]:





# In[ ]:




