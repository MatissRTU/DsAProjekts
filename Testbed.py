import requests
from bs4 import BeautifulSoup
import openpyxl

url1 = "https://www.1a.lv/c/berniem-mazuliem/lego-rotallietas-un-lelles/lego/37h?lf=1"
url = "https://www.ksenukai.lv/c/rotallietas-preces-berniem/lego/dgs?lf=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"  # nepieciešams ksenukajam
}

page = requests.get(url, headers=headers)
print(page.status_code)  # temp code

if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")
    pagination = soup.select_one(".catalog-taxons-pagination .paginator__last")  # elements pēdējam lapas ciparam
    last_page = int(pagination.text.strip())  # atdala ciparu no elementa
    print(last_page)  # temp code

    product_data = []

    for page_number in range(1,1+1):#TODO replace 1(testcase) with last_page
        search_url = f"{url}&page={page_number}"
        print(page_number)  # temp code
        page = requests.get(search_url, headers=headers)
        print(page.status_code)

        soup = BeautifulSoup(page.content, "html.parser")
        product_sections = soup.select("div.catalog-taxons-product")


        #excel dokuments
        Excel = openpyxl.Workbook()
        doc = Excel.active#atver Excel
        doc.title = "LEGO komplektu akcijas buklets"

        doc.append(["Nosaukums","Cena","bilde"])#tabulu nosaukums

        for block in product_sections:
            class_list = block.get("class", [])
            if "catalog-taxons-product--no-product" in class_list:
                continue
            
            itemdata = block.find("div", class_="gtm-categories")
            itemimg = block.find("img", class_="catalog-taxons-product__image")
            itemimg = block.find("img", class_="catalog-taxons-product__image")
            img = None
            if itemimg: 
                img = itemimg.get("data-src") or itemimg.get("src")

            if itemimg: 
                img = itemimg.get("data-src") or itemimg.get("src") 
            if itemdata:
                name = itemdata.get("data-name")
                price = itemdata.get("data-price")
                product_data.append([name, price, img])
                
            
                #print(f"{name} - {price}€ - {img}")  # PRINTE NOFORMATETOS DATUS
                product_data.append([name, price, img])

            doc.append([name, price, img])

    Excel.save("LEGO komplektu akcijas buklets.xlsx") 


    print()
    print(len(product_data))  # temp code
    print(product_data[0]) 
    print(product_data[46])  
    print(product_data[-1])  # NEAPSTRADATIE DATI