#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[33]:


# URL of page to be scraped
url = 'https://www.indeed.com/salaries/data-analyst-Salaries'


# In[34]:


# Retrieve page with the requests module
response = requests.get(url)


# In[35]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[36]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[37]:


# results are returned as an iterable list
avg_salary = soup.find("strong",class_='cmp-salary-amount').text

print(avg_salary)



# In[38]:


options = soup.find("select",{"id":"cmp-salary-loc-select"}).findAll("option")
len(options)


# In[39]:


#pulling out the cities out
for option in options:
    print(option)
    print('-'*50)


# In[40]:


#pulling out the cities out
for option in options:
    print(option['value'])
    print(option['data-tn-element'])
    print('-'*50)


# In[49]:


regions = {'Northeast':['NJ','NY','PA','MA','VT','NH','CT','RI','ME'],
           'Midwest':['MN','ND','SD','IA','WI','OH','IL','NE','MO','KS','MI','IN'], 
           'South':['TX','LA','OK','AR','MS','AL','TN','KY','GA','FL','NC','SC','WV','VA','MD','DE','DC'], 
           'West':['WA','CA','OR','ID','MT','WY','CO','NM','NV','AZ','UT','AK','HI']}

base_url = 'https://www.indeed.com'

salaries_list = []

cities_list = []
d = {'cities': [], 'salary': []}


#pulling out the cities out
for option in options:
    
    if(option['data-tn-element']=='loc_city[]'):
        if(option['value'][-2:] in regions['South']):
            option_url = base_url + option['value']
            salary_info = requests.get(option_url)
            salary_soup = BeautifulSoup(salary_info.text, 'html.parser')
            avg_salaries = salary_soup.find("div",class_='cmp-sal-salary').text
            city_name = salary_soup.find("div",class_='cmp-sal-summary-caption').text
            print(city_name)
            print(avg_salaries)
            cities_list.append(city_name)
           
            salaries_list.append(avg_salaries)
            #print(option_url)
            print('-'*50)
    


# In[50]:


salaries_list


# In[51]:


cities_list
new_cities = []

for name in cities_list:
    city_value = name.split('Average in ')
    city_place = city_value[1]
    
    new_cities.append(city_place)
    
#print(new_cities)

d['cities'] = new_cities
   

    
   
d


# In[52]:



new_sal = []


for salary in salaries_list:
    if 'hour' in salary:
        arr = salary.split(' per hour')
        sal_num = arr[0][1::]
        real_num = float(sal_num)
        real_num *=2080
        print(real_num)
        new_sal.append(real_num)
        
    else:
        arr1 = salary.split(' per year')
        sal_n = arr1[0][1::]
        sal_n = sal_n.split(',')
        number = ''.join(sal_n) 
        real_n = int(number)
        print(real_n)
        new_sal.append(real_n)
        
        
d['salary'] = new_sal
        
    
    


# In[53]:


#new_sal

d


# In[54]:




df = pd.DataFrame(d, columns=['cities','salary'])

df


# In[55]:


df.to_json(orient='split')


# In[63]:


# Getting a list of six job openings 

for option in options:
    
    if(option['data-tn-element']=='loc_city[]'):
        if(option['value'][-2:] in regions['South']):
            option_url = base_url + option['value']
            job_info = requests.get(option_url)
            job_soup = BeautifulSoup(job_info.text, 'html.parser')
            job_title = job_soup.find("div",class_='sal-job-entry-jobtitle').text
            company_name = job_soup.find("div",class_='sal-job-entry-company').text
            job_city = job_soup.find("div",class_='sal-job-entry-jobsubtitle').text
            job_salary = job_soup.find("div",class_='sal-job-salary-amount').text
            print(job_title)
            print(company_name)
            print(job_city)
            print(job_salary)
            print('-'*50)



# In[ ]:




