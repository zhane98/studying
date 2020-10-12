import requests #.get and .content
from bs4 import BeautifulSoup, SoupStrainer

url_base = "https://www.monster.co.uk/jobs/search/?q="
job_title = "Software-Developer"
url_location = "&where="
location = "London"

new_url = url_base + job_title + url_location + location
# cal_url = f"{url_base}{job_title}{url_location}{location}"

page = requests.get(new_url)
# print(page.content) #prints out the HTML

# print(page) #200 - everything works, 400 - doesn't work.

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

for postings in job_elems:
    title = postings.find('h2', class_='title')
    company = postings.find('div', class_='company')
    location = postings.find('div', class_='location')
    # link = postings.find('a')['href']

    if None in (title, company, location):
        continue
 
    link = postings.find('a').get('href')
    
    if link is None:
        continue

    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(f"Link to job: {link} \n")
    print()