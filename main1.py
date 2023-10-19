import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=bags&crid=2IB2ZH4QDP4I9&sprefix=bags%2Caps%2C4132&ref=nb_sb_noss_1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    product_details = soup.find_all('div', {'data-asin': True})
    for product in product_details:
        name = product.find('span', {'class': 'a-text-normal'})
        product_name = name.get_text() if name else "Not Found"

        price = product.find('span', {'class': 'a-price-whole'})
        product_price = price.get_text() if price else "Not Found"

        rating = product.find('span', {'class': 'a-icon-alt'})
        product_rating = rating.get_text() if rating else "Not Found"

        product_url = f"https://www.amazon.in{product.find('a', {'class': 'a-link-normal'})['href']}" if product.find('a', {'class': 'a-link-normal'}) else "Not Dound"

        reviews=soup.find('span', {'class': 'a-size-base s-underline-text'})
        product_reviews=reviews.get_text() if rating else "Not Found"
        print("Product_URL:", product_url)
        print("Product_name:", product_name)
        print("Product_price:", product_price)
        print("Product_rating:", product_rating)
        
        print("\n")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)