# jops search project 

from bs4 import BeautifulSoup
import requests

pages_number = int(input("Enter how many pages you want to scrape: "))
key = input("Enter a key for your search (few, 1, 2, 3, 4, 5) days ago: ")

for page in range(1, pages_number + 1):
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=python&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence={page}&startPage=1').text
    
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')  # Elements containing job information
    
    for index, job in enumerate(jobs, start=1):
        post_date = job.find('span', class_='sim-posted').text  # Extracting the post date
        if key in post_date:
            print(f"\nPage number ({page}) - Job number ({index}):\n")
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()  # Extracting the company name
            skills = job.find('span', class_='srp-skills').text.strip()  # Extracting the required skills
            
            print(f'''
            Company Name : {company_name}

            Required Skills: {skills}
            
            Post Date : {post_date} 
            ''')

print("\nEnd of program! *__*\n")
