import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=software%20developer&l=San%20Diego%2C%20CA&vjk=370bd89a13a9d5b8'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="resultsCol")

job_elements = results.find_all('div', class_='slider_item')
'''
for job_element in job_elements:
    title_element = job_element.find('h2', class_='jobTitle')
    company_element = job_element.find('span', class_='companyName')
    location_element = job_element.find('div', class_='companyLocation')
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
'''
junior_dev_jobs = results.find_all(
    'h2', string=lambda text: 'junior' in text.lower()
)
