import pandas as pd 
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

web_page = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers)
soup = BeautifulSoup(web_page,'lxml')
# soup.find_all('h1')[0].text
# soup.find_all('h2')
# for i in soup.find_all('h2'):
#     print(i.text.strip())
# for i in soup.find_all('p'):
#     print(i.text.strip())
# soup.find_all('p',class_= 'rating')
compony = soup.find_all('div' , class_='company-content-wrapper')
print(len(compony))
name = []
rating = []
reviews = []
ctype = []
hq = []
old = []
empoyees = []
for i in compony:
    name.append(i.find_all('h2').text.strip())
    rating.append(i.find('p',class_='rating')[0].text.strip())
    reviews.append(i.find('a',class_ = 'review-count').text.strip())
    ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
    hq.append(i.find_all('p',class_='infoEntity')[0].text.strip())
    old.append(i.find_all('p',class_='infoEntity')[0].text.strip())
    empoyees.append(i.find_all('p',class_='infoEntity')[0].text.strip())
d = {'name':name,'rating':rating,'reviews':reviews,'type':ctype,'hq':hq,'old':old,'empoyees':empoyees}
df = pd.DataFrame(d)
final = pd.DataFrame()
for j in range(1,11):
    url = 'https://www.ambitionbox.com/list-of-companies?page={}'.format(j)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    soup = BeautifulSoup(web_page,'lxml')





