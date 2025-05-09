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
					current.value = value 
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
		
	def filter_price(self, max_price):
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

		product_data = HashTable(6000)
	
		for page_number in range(1,last_page+1):
			search_url = f"{url}&page={page_number}"
			page = requests.get(search_url, headers=id)

			soup = BeautifulSoup(page.content, "html.parser")
			product_sections = soup.select("div.catalog-taxons-product")

			for block in product_sections:
				class_list = block.get("class", [])#nolasa klases ipasibas
				if "catalog-taxons-product--no-product" in class_list:#objekts nosaka ka produkts izpardots
					continue
            
				itemdata = block.find("div", class_="gtm-categories")
				itemimg = block.find("img", class_="catalog-taxons-product__image")#es šito

				if itemimg: 
					img = itemimg.get("data-src") or itemimg.get("src") #un vel šito ja tas svarīg(kad izlasi šo vari izdzēst, tas tā lai vieglāk atrast ko es pievienoju)
				if itemdata:
					name = itemdata.get("data-name")
					price = itemdata.get("data-price")
					index =+ 1
					product_data.insert(index, {"name": name, "price": float(price), "img": img})
				#TODO add excel functionality and mayb fix hash insert


def search2(url,id):#ja amazon/lego izmanto savadaku formatu
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


userid = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"#nepieciesams ksenukajam
}

#izmantojamie url meklesana
url1 = "https://www.1a.lv/c/berniem-mazuliem/lego-rotallietas-un-lelles/lego/37h?lf=1"
url2 = "https://www.ksenukai.lv/c/rotallietas-preces-berniem/lego/dgs?lf=1"
url3 = ""

index = 0

search1(url1,userid)
search1(url2,userid)