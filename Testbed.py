import requests
from bs4 import BeautifulSoup

url1 = "https://www.1a.lv/c/berniem-mazuliem/lego-rotallietas-un-lelles/lego/37h?lf=1"
url = "https://www.ksenukai.lv/c/rotallietas-preces-berniem/lego/dgs?lf=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"#nepieciesams ksenukajam
}

page = requests.get(url, headers=headers)
print(page.status_code)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")

    product_sections = soup.select("div.catalog-taxons-product")
    print(f"Found {len(product_sections)} products")

    product_data = []
    for block in product_sections:
        gtm_div = block.find("div", class_="gtm-categories")
        if gtm_div:
            name = gtm_div.get("data-name", "N/A")
            price = gtm_div.get("data-price", "N/A")
            print(f"{name} - {price}€")
            product_data.append([name, price])
    print()
    print(product_data)
