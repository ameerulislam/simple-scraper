from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://ameerulislam.com/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_test.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary'])

for article in soup.find_all('article'):
#print(article.prettify())
  headline = article.header.div.h2.a.text

  #print(headline)

  summary = article.find('div', class_ = 'entry-content').text

  #print(summary)
  
  csv_writer.writerow([headline, summary])

csv_file.close
