import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.drawing.image import Image

class Node: 
	def __init__(self, key, value): 
		self.key = key 
		self.value = value 
		self.next = None

#hash implement
class HashTable: 
	def __init__(self, capacity): 
		self.capacity = capacity 
		self.size = 0
		self.table = [None] * capacity 

	def _hash(self, key): 
		return hash(key) % self.capacity 

	def insert(self, key, value): 
		index = self._hash(key) 

		if self.table[index] is None: 
			self.table[index] = Node(key, value) 
			self.size += 1
		else: 
			current = self.table[index] 
			while current: 
				if current.key == key: 
					if isinstance(current.value, list) and isinstance(current.value[0], list):
						current.value.append(value)
					else:
						current.value = [current.value, value]
					return
				current = current.next
			new_node = Node(key, value) 
			new_node.next = self.table[index] 
			self.table[index] = new_node 
			self.size += 1

	def search(self, key): 
		index = self._hash(key) 

		current = self.table[index] 
		while current: 
			if current.key == key: 
				return current.value 
			current = current.next

		raise KeyError(key) 

	def remove(self, key): 
		index = self._hash(key) 

		previous = None
		current = self.table[index] 

		while current: 
			if current.key == key: 
				if previous: 
					previous.next = current.next
				else: 
					self.table[index] = current.next
				self.size -= 1
				return
			previous = current 
			current = current.next

		raise KeyError(key) 

	def __len__(self): 
		return self.size 

	def __contains__(self, key): 
		try: 
			self.search(key) 
			return True
		except KeyError: 
			return False
#hash implement end	


def search1(url,id):#prieks ksenukai/1alv

	page = requests.get(url, headers=id)
	if page.status_code == 200:
		soup = BeautifulSoup(page.content, "html.parser")
		pagination = soup.select_one(".catalog-taxons-pagination .paginator__last")  # elements pēdējam lapas ciparam
		last_page = int(pagination.text.strip())  # atdala ciparu no elementa
	
		for page_number in range(1,1+1):#TODO KAD TESTE last_page samainit ar 1
			print(f"Searching({page_number}/{last_page})...")
			search_url = f"{url}&page={page_number}"
			page = requests.get(search_url, headers=id)

			soup = BeautifulSoup(page.content, "html.parser")
			product_sections = soup.select("div.catalog-taxons-product")

			for block in product_sections:
				class_list = block.get("class", [])#nolasa klases ipasibas
				if "catalog-taxons-product--no-product" in class_list:#objekts nosaka ka produkts izpardots
					continue
            
				itemdata = block.find("div", class_="gtm-categories")
				itemimg = block.find("img", class_="catalog-taxons-product__image")

				if itemimg: 
					img = itemimg.get("data-src") or itemimg.get("src")
				if itemdata:
					name = itemdata.get("data-name")
					price = itemdata.get("data-price")
					index =+ 1
					product_data.insert(float(price),[name, img])

def search2(url,id):# amazon meklētājs TODO remake to 220lv
	page = requests.get(url, headers=id)
	print(page.status_code)

	if page.status_code == 200:
		soup = BeautifulSoup(page.content, "html.parser")
		product_sections = soup.select("div.catalog-taxons-product")

		product_data = []
		for block in product_sections:
			gtm_div = block.find("div", class_="gtm-categories")
			if gtm_div:
				name = gtm_div.get("data-name")
				price = gtm_div.get("data-price")
				print(f"{name} - {price}€")#PRINTE NOFORMATETOS DATUS 
				product_data.append([name, price])
		print()
		print(product_data)#NEAPSTRADATIE DATI

def sort_to_excel(price_range):
	Excel = openpyxl.Workbook()
	doc = Excel.active#atver Excel
	doc.title = "LEGO komplektu akcijas buklets" 
	doc.append(["Nosaukums","Cena","Bilde"])
	### SEIT VEIKT FILTRESANU

	for block in product_data.table:
		current = block
		while current:
			key = current.key
			if key < price_range:
				value = current.value
				if isinstance(value[0], list):
					for item in value:
						doc.append([item[0], current.key, f'=IMAGE("{item[1]}")'])#TODO SALABOT IMAGE parvietojot linku uz nakamo rindu un refrencojot uz to 

				else:
					doc.append([value[0], current.key, f'=IMAGE("{value[1]}")'])

					
			current = current.next


	#=image("{img}") 
	Excel.save("LEGO komplektu akcijas buklets.xlsx")


userid = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"#nepieciesams ksenukajam
}

#izmantojamie url meklesana
url1 = "https://www.1a.lv/c/berniem-mazuliem/lego-rotallietas-un-lelles/lego/37h?lf=1"#                           |
url2 = "https://www.ksenukai.lv/c/rotallietas-preces-berniem/lego/dgs?lf=1" #                                     V rekur ir lapaspuses cipars
url3 = "https://www.amazon.de/-/en/s?i=toys&rh=n%3A12950651%2Cp_123%3A249943%2Cp_n_deal_type%3A26902994031&dc&page=1&language=en&qid=1746821762&rnid=26902991031&xpid=bVRkszM2eK61l&ref=sr_pg_1"
url4= "https://www.lego.com/en-lv/categories/sales-and-deals"

product_data = HashTable(6000)

search1(url1,userid) #TODO FINISH AND UNCOMMENT
#search1(url2,userid) #TODO FINISH AND UNCOMMENT
'''
product_data.insert(1, ["test", "test"])#testa ievade
print(product_data.search(1))
product_data.insert(1, ["test1", "test1"])
print(product_data.search(1))
'''

page = requests.get(url4, headers=userid)
print(page.status_code)
tester = input("test value: ")
sort_to_excel(float(tester))
# ~~~~~~~~~~~~~~~~~~	
#           _
#       .__(.)< (MEOW)
#        \___)   
# ~~~~~~~~~~~~~~~~~~-->