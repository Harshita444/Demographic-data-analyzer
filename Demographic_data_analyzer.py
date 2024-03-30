#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas


# In[3]:


import pandas as pd


# In[6]:


import os


# In[7]:


os.makedirs('./projects',exist_ok=True)


# In[103]:


df = pd.read_csv("C:/Users/tanwa/Downloads/project2.csv")


# In[11]:


df


# ### How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

# In[12]:


race_count = df['race'].value_counts()


# In[13]:


race_count


# ## What is the average age of men?
# 

# In[19]:


avg_age_men = df[df['sex'] == 'Male']['age'].mean()


# In[20]:


avg_age_men


# ### What is the percentage of people who have a Bachelor's degree?
# 

# In[27]:


bachelor_count=(df['education']=='Bachelors').sum()


# In[29]:


bachelor_count


# In[30]:


total_count=len(df)


# In[31]:


total_count


# In[32]:


bachelor_percentage=(bachelor_count/total_count)*100


# In[33]:


bachelor_percentage


# ### What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
# 

# In[38]:


Advance_education=df[df['education'].isin(['Bachelors','Masters','Doctorate'])]


# In[56]:


advance_eduaction_count=len(Advance_education)


# In[57]:


advance_eduaction_count


# In[46]:


advance_education_higher_Salary=Advance_education[Advance_education['salary']=='>50K']


# In[47]:


advance_education_higher_Salary


# In[ ]:





# In[52]:


advance_education_higher_Salary_count=len(advance_education_higher_Salary)


# In[53]:


advance_education_higher_Salary_count


# In[58]:


advance_education_higher_Salary_percentage=(advance_education_higher_Salary_count/advance_eduaction_count)*100


# In[59]:


advance_education_higher_Salary_percentage


# ### What percentage of people without advanced education make more than 50K?
# 

# In[61]:


Non_Advance_education=df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]


# In[62]:


Non_Advance_education


# In[63]:


Non_Advance_education_count=len(Non_Advance_education)


# In[64]:


Non_Advance_education_count


# In[65]:


non_advance_education_higher_Salary=Non_Advance_education[Advance_education['salary']=='>50K']


# In[66]:


non_advance_education_higher_Salary


# In[68]:


non_advance_education_higher_Salary_percentage= (len(non_advance_education_higher_Salary)/Non_Advance_education_count)*100


# In[69]:


non_advance_education_higher_Salary_percentage


# ### What is the minimum number of hours a person works per week?
# 

# In[73]:


min_hour=df['hours-per-week'].min()


# In[74]:


min_hour


# ### What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

# In[100]:


min_hour_df=df[df['hours-per-week']==min_hour]


# In[101]:


min_hour_df


# In[87]:


min_hour_high_salary=min_hour_df[min_hour_df['salary']=='>50K']


# In[88]:


min_hour_high_salary


# In[89]:


min_hour_high_salary_Percentage=len(min_hour_high_salary)/len(min_hour_df)*100


# In[90]:


min_hour_high_salary_Percentage


# ### What country has the highest percentage of people that earn >50K and what is that percentage?

# In[105]:


more_than_50k = df[df['salary'] == '>50K']


# In[107]:


more_than_50k


# In[108]:


total_counts = df['native-country'].value_counts()
more_than_50k_counts = more_than_50k['native-country'].value_counts()


# In[109]:


total_counts


# In[110]:


more_than_50k_counts


# In[111]:


percentage_more_than_50k = (more_than_50k_counts / total_counts) * 100


# In[112]:


percentage_more_than_50k


# In[ ]:





# In[113]:


more_than_50k = df[df['salary'] == '>50K']

# Calculate the total counts and the counts for those earning more than 50K by country
total_counts = df['native-country'].value_counts()
more_than_50k_counts = more_than_50k['native-country'].value_counts()

# Calculate the percentage of those earning more than 50K by country
percentage_more_than_50k = (more_than_50k_counts / total_counts) * 100

# Find the country with the highest percentage
highest_percentage_country = percentage_more_than_50k.idxmax()
highest_percentage = percentage_more_than_50k.max()

print(f"The country with the highest percentage of people earning more than 50K is {highest_percentage_country}, with a percentage of {highest_percentage:.2f}%.")


# In[114]:


highest_percentage_country


# In[115]:


more_than_50k = df[df['salary'] == '>50K']


# In[116]:


more_than_50k


# In[117]:


total_counts = df['native-country'].value_counts()


# In[118]:


total_counts


# In[119]:


more_than_50k_counts = more_than_50k['native-country'].value_counts()


# In[120]:


more_than_50k_counts


# ### Identify the most popular occupation for those who earn >50K in India.
# 

# In[128]:


df_high_salary=df[(df['salary']=='>50K') &(df['native-country']=='India')]


# In[129]:


df_high_salary


# In[130]:


most_common_occupation = df_high_salary['occupation'].value_counts().idxmax()


# In[131]:


most_common_occupation


# In[ ]:


jovian.commit()


# In[ ]:




