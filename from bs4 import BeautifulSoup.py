from bs4 import BeautifulSoup
#request lib requests information from a website behind the scenes and thats the whole
##point of importing requests while web-scrapping.
#import requests
##html_text =requests.get('https://www.seek.com.au/data-analyst-junior-jobs').text
##soup = BeautifulSoup(html_text, 'lxml')
#jobs = soup.find_all('div' , class_='_1wkzzau0 a1msqi72')
#print(jobs)

with open('https://www.seek.com.au/data-analyst-junior-jobs','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify)