import requests
from bs4 import BeautifulSoup
import re
import pandas

url="https://www.amazon.in/s?k=bags&crid=2IB2ZH4QDP4I9&sprefix=bags%2Caps%2C4132&ref=nb_sb_noss_1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
r=requests.get(url, headers=headers)
soup=BeautifulSoup(r.content, 'html.parser')

def url(soup):
    link='https://amazon.in/'
    try:
        product_url=soup.find('a', class_='a-link-normal')
        print(product_url)
        product_link=product_url.get_href
        print(product_link)
        pattern = r'.*\/dp\/([A-Z0-9]+)\/'
        final = re.search(pattern, product_link)
        final_url= link+final.text

    except Exception as e:
        final_url=''
        print(e,2000)
    print(final_url)
    return final_url
url(soup)

def name(soup):
    try:
        pro_name=soup.find('span', class_='a-size-medium a-color-base a-text-normal')
        product_name=pro_name.text
    except:
        product_name=''
    return product_name


def price(soup):
    try:
        pro_price=soup.find('span', class_='a-price-whole')
        product_price=pro_price.text
    except:
        product_price=''
    return product_price

def ratings(soup):
    try:
        pro_ratings=soup.find('span', class_='a-icon-alt')
        product_ratings=pro_ratings.text
    except:
        product_ratings=''
    return product_ratings

def review(soup):
    try:
        pro_review=soup.find('span', class_='a-size-base s-underline-text')
        product_review=pro_review
    except:
        product_review=''
    return product_review

def product_details(soup):
    try:
        print(1)
        requests.get(url(soup))
        try:
            description_list=''
            print(233)
            description=soup.find('ul', class_='a-unordered-list a-vertical a-spacing-mini')
            print(description)
            for i in description:
                description_list+=soup.find('span', class_='a-list-item')+'\n'
                print(2)
        except Exception as e:
            description_list=''
            print(e)
        
        try:
            asin=soup.find('ol', class_='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list')
            asin[1].find('span', class_='a-list-item')
            print(asin[1].find('span', class_='a-list-item').text)
            print(3)

            
        except:
            print('ni chat ra')
            pass
    except Exception as e:
        print(e)
product_details(soup)
        
#ref=mp_s_a_1_1_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1697711335&sprefix=ba%2Caps%2C283&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9zZWFyY2hfYXRm&psc=1
#ref=mp_s_a_1_1_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1697722429&sprefix=ba%2Caps%2C283&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9zZWFyY2hfYXRm&psc=1
#https://www.amazon.in/Zebronics-Compartment-Backpacks-15-6-inch-Black/dp/B0C6KZS555

# a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal
# "/Zebronics-Compartment-Backpacks-15-6-inch-Black/dp/B0C6KZS555/ref=rvi_sccl_1/260-6641117-2077613?pd_rd_w=Y8M6W&content-id=amzn1.sym.2fa5ef78-d215-4b54-bdb7-fa3d3620b822&pf_rd_p=2fa5ef78-d215-4b54-bdb7-fa3d3620b822&pf_rd_r=DZPB285SSF5DEEPF938J&pd_rd_wg=WU2V4&pd_rd_r=4f6a9f41-4998-4944-b408-31528c96f598&pd_rd_i=B0C6KZS555&psc=1"
# a-link-normal
print(soup)
a=soup.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div')
print(a)

pages=soup.find('a', class_='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator')
total_pages=pages.get_href
for i in range(1,21):
    pass
