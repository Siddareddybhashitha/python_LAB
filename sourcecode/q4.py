import requests
link = ' https://catalog.umkc.edu/course-offerings/graduate/comp-sci/'
response = requests.get(link)
from bs4 import BeautifulSoup
content = BeautifulSoup(response.content, "html.parser")
content1=content.find('div',attrs={'class':'courses'})
content11=content1.find_all('p')
for course in content11:
  print(course.get_text())