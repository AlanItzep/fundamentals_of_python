#Web Scraping (Data Extraction) with BeautifulSoup


import requests
from bs4 import BeautifulSoup
"""
def get_html():
    return "<html><body><h1>Title</h1><p>Price: $19.99</p><p>In stock: Yes</p></body></html>"
"""
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return str(response.text)
    else:
        return ""


def extract_info(soup):
    title_tag = soup.find("h1")
    price_tag = soup.find_all("p")[0]
    stock_tag = soup.find_all("p")[1]

    title = str(title_tag.text)
    price_text = str(price_tag.text)
    stock_text = str(stock_tag.text)

    price_value = 0.0
    if "$" in price_text:
        dollar_index = price_text.find("$")
        number_part = price_text[dollar_index + 1 : dollar_index + 6]
        price_value = float(number_part)

    in_stock = False
    if "Yes" in stock_text:
        in_stock = True

    print("Product title:", title)
    print("Price:", price_value)
    print("Available:", in_stock)

# html = get_html()
html = get_html("http://www.cs.upc.edu/~jalonso/test.html")
soup = BeautifulSoup(html, "html.parser")
extract_info(soup)
