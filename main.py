import requests
from bs4 import BeautifulSoup

url="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"}
r=requests.get(url, headers=header)
soup=BeautifulSoup(r.content, 'html.parser')
bags_div= soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small')
print(r)
description_list=''
link='https://amazon.in/'
for i in bags_div:
    product_url= soup.find('a', class_='a-link-normal s-no-outline')
    final_url=link+(product_url.get('href'))
    name=soup.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_name=name.text
    price=soup.find('span', class_='a-price-whole')
    product_price=price.text
    ratings=soup.find('span', class_='a-icon-alt')
    total_ratings=ratings.text
    reviews=soup.find('span', class_='a-size-base s-underline-text')
    total_reviews=reviews.text()
    requests.get(final_url)
    description=soup.find('ul', class_='a-unordered-list a-vertical a-spacing-mini')
    for i in description:
        description_list+=soup.find('span', class_='a-list-item')+'\n'

# https://www.amazon.in/Uppercase-Professional-Backpack-Resistant-Sustainable/dp/B0BWNBQXDZ/ref=sr_1_11_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1697613761&sprefix=ba%2Caps%2C283&sr=8-11-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1
# sspa/click?ie=UTF8&spc=MTo2MTE1MTMzMDkxOTM2NTU6MTY5NzYxMzc2MTpzcF9tdGY6MjAxMjU4OTk5MjA2OTg6OjA6Og&url=%2FUppercase-Professional-Backpack-Resistant-Sustainable%2Fdp%2FB0BWNBQXDZ%2Fref%3Dsr_1_11_sspa%3Fcrid%3D2M096C61O4MLT%26keywords%3Dbags%26qid%3D1697613761%26sprefix%3Dba%252Caps%252C283%26sr%3D8-11-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1

#creating csv(comma seperated value) file
'''var7=pd.DataFrame({'one':[1,2,3,4,5], 'two':[4,5,6,7,8], 'three':[3,4,5,6,7]})
print(var7)
#var7=var7.dropna(subset=['product_name'])
var7.to_csv('test_file.csv', index=False, header=['o','t','th'])'''