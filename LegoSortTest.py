
import requests
from bs4 import BeautifulSoup
import openpyxl

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
		
	def filter_price(self, max_price):#TODO REMOVE WHEN FINISHED WITH REWRITE
		entries_to_remove = []
		for bucket in self.table:
			current = bucket
			while current:
				value = current.value
				price = value.get("price")
				if isinstance(price, str):
					try:
						price = float(price)
					except ValueError:
						price = float("inf")
				if price > max_price:
					entries_to_remove.append(current.key)
				current = current.next

		for key in entries_to_remove:
			self.remove(key)
#hash implement end	


def search1(url,id):#prieks ksenukai/1alv

	page = requests.get(url, headers=id)
	if page.status_code == 200:
		soup = BeautifulSoup(page.content, "html.parser")
		pagination = soup.select_one(".catalog-taxons-pagination .paginator__last")  # elements pēdējam lapas ciparam
		last_page = int(pagination.text.strip())  # atdala ciparu no elementa
	
		for page_number in range(1,last_page+1):#KAD TESTE last_page samainit ar 1
			search_url = f"{url}&page={page_number}"
			page = requests.get(search_url, headers=id)

			soup = BeautifulSoup(page.content, "html.parser")
			product_sections = soup.select("div.catalog-taxons-product")
			print(f"{page_number}/{last_page}")

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
					itemdata.insert(float(price),[name, img])

def search2(url,id):# amazon meklētājs
	page = requests.get(url, headers=id)
	print(page.status_code)

	if page.status_code == 200:
		soup = BeautifulSoup(page.content, "html.parser")
		product_sections = soup.select("div.catalog-taxons-product")

		itemdata = []
		for block in product_sections:
			gtm_div = block.find("div", class_="gtm-categories")
			if gtm_div:
				name = gtm_div.get("data-name")
				price = gtm_div.get("data-price")
				print(f"{name} - {price}€")#PRINTE NOFORMATETOS DATUS 
				itemdata.append([name, price])
		print()
		print(itemdata)#NEAPSTRADATIE DATI

def sortExcel(price_range):
	
	Excel = openpyxl.Workbook()
	doc = Excel.active#atver Excel
	doc.title = "LEGO komplektu akcijas buklets" 
	doc.append(["Nosaukums","Cena","bilde"])
	### SEIT VEIKT FILTRESANU

	ranges = {
        	"25": (5, 25),
        	"50": (25, 50),
        	"100": (50, 100),
        	"200": (100, 200),
        	"200+": (200, float("inf"))
   	}
	
	min_price, max_price = ranges[price_range]
	
	keys_to_remove = set()
	for bucket in itemdata.table:
		current = bucket
		while current:
			key = current.key
			try:
				price = float(key)
				if price < min_price or price > max_price:
					keys_to_remove.add(key)
			except (ValueError, TypeError):
				keys_to_remove.add(key)
			current = current.next
		
		for key in keys_to_remove:
			try:
				itemdata.remove(key)
			except KeyError:
				pass

	for bucket in itemdata.table:
		current = bucket
		while current:
			value = current.value
			if isinstance(value[0], list):
				for item in value:
					doc.append([item[0], current.key, item[1]])
			else:
				doc.append([value[0], current.key, value[1]])
			current = current.next

	#=image("{img}") 
	Excel.save("LEGO komplektu akcijas buklets.xlsx")

userid1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"#nepieciesams ksenukajam
}
userid2 = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

#izmantojamie url meklesana
url1 = "https://www.1a.lv/c/berniem-mazuliem/lego-rotallietas-un-lelles/lego/37h?lf=1"
url2 = "https://www.ksenukai.lv/c/rotallietas-preces-berniem/lego/dgs?lf=1" 
url3 = "https://www.amazon.de/s?k=lego&i=toys&rh=n%3A12950651%2Cp_123%3A249943&dc&page=1&language=en&qid=1746980694&rnid=91049101031&xpid=D6Gb0ahu6t-Q5&ref=sr_pg_1"

itemdata = HashTable(6000)

#search1(url1,userid) #TODO FINISH AND UNCOMMENT
#search1(url2,userid) #TODO FINISH AND UNCOMMEET
search2(url3,userid1)
#sortExcel("50") #šitas ir tas kas nosaka pēc kuras vērtības skatās

itemdata.insert(1, ["test", "test"])#testa ievade
print(itemdata.search(1))
itemdata.insert(1, ["test1", "test1"])
print(itemdata.search(1))