import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/s?k=bags&crid=2IB2ZH4QDP4I9&sprefix=bags%2Caps%2C4132&ref=nb_sb_noss_1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    product_details = soup.find_all('div', {'data-asin': True})

    with open('amazon_products.csv', 'w', newline='') as csvfile:
        fieldnames = ['Product name', 'Product price', 'Product rating', 'Product review' 'Product URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    for product in product_details:
        name = product.find('span', {'class': 'a-text-normal'})
        product_name = name.get_text() if name else "Not Found"

        price = product.find('span', {'class': 'a-price-whole'})
        product_price = price.get_text() if price else "Not Found"

        rating = product.find('span', {'class': 'a-icon-alt'})
        product_rating = rating.get_text() if rating else "Not Found"

        reviews=soup.find('span', {'class': 'a-size-base s-underline-text'})
        product_reviews=reviews.get_text() if reviews else "Not Found"

        url = product.find('a', {'class': 'a-link-normal'})
        product_url = f"https://www.amazon.in{url['href']}" if url else ""
        
        print("Product_URL:", product_url)
        print("Product_name:", product_name)
        print("Product_price:", product_price)
        print("Product_rating:", product_rating)
        print("Product_reviews:", product_reviews)
        
        print("\n")

        if product_name and product_price and product_rating and product_url:
            writer.writerow({'Product name': product_name, 'Product price': product_price, 'Product rating': product_rating, 'Product review': product_reviews, 'Product URL': product_url})

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
