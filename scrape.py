# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

# Initialize browser
def init_browser(): 


    # Replace the path with your actual path to the chromedriver

    #Mac Users
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #return Browser('chrome', **executable_path, headless=False)
    exec_path = {'executable_path': '/app/.chromedriver/bin/chromedriver'}
    return Browser('chrome', headless=True, **exec_path)



def option_scrape():

    try:
       
        # Initialize browser 
        browsers = init_browser()

        # URL of page to be scraped
        url = 'https://www.indeed.com/salaries/data-analyst-Salaries'
        
        browsers.visit(url)

        # HTML Object
        html = browsers.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        

        options = soup.find("select",{"id":"cmp-salary-loc-select"}).findAll("option")
        len(options)

        
        return options 

    finally:
        browsers.quit() 

def region_scrape(region = 'South'):

    try:
        

        # Initialize browser 
        browsers = init_browser()

        # URL of page to be scraped
        url = 'https://www.indeed.com/salaries/data-analyst-Salaries'
        
        browsers.visit(url)

        # HTML Object
        html = browsers.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        


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
                if(option['value'][-2:] in regions[region]):
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
        
        cities_list
        new_cities = []

        for name in cities_list:
            city_value = name.split('Average in ')
            city_place = city_value[1]
            
            new_cities.append(city_place)
            
        #print(new_cities)

        d['cities'] = new_cities

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

        df = pd.DataFrame(d, columns=['cities','salary'])

        cities = df['cities']
        salaries = df['salary']


        city_salaries = {
            'cities':cities.tolist(),
            'salaries':salaries.tolist()
        }


        #app_json = json.dumps(city_salaries)

        return city_salaries 

    finally:
        browsers.quit() 

    print(df)