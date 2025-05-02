import requests
from bs4 import BeautifulSoup

class Node: 
	def __init__(self, key, value): 
		self.key = key 
		self.value = value 
		self.next = None


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
		
def search1(url,id):
	page = requests.get(url, headers=id)
	print(page.status_code)

	if page.status_code == 200:
		soup = BeautifulSoup(page.content, "html.parser")

		product_sections = soup.select("div.catalog-taxons-product")
		print(f"Found {len(product_sections)} products")

		product_data = []
		for block in product_sections:
			gtm_div = block.find("div", class_="gtm-categories")
			if gtm_div:
				name = gtm_div.get("data-name")
				price = gtm_div.get("data-price")
				print(f"{name} - {price}€")
				product_data.append([name, price])
		print()
		print(product_data)



def search2(url,id):
	page = requests.get(url, headers=id)
	print(page.status_code)

	if page.status_code == 200:
		soup = BeautifulSoup(page.content, "html.parser")

		product_sections = soup.select("div.catalog-taxons-product")
		print(f"Found {len(product_sections)} products")

		product_data = []
		for block in product_sections:
			gtm_div = block.find("div", class_="gtm-categories")
			if gtm_div:
				name = gtm_div.get("data-name")
				price = gtm_div.get("data-price")
				print(f"{name} - {price}€")
				product_data.append([name, price])
		print()
		print(product_data)


userid = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"#nepieciesams ksenukajam
}

url1 = "https://www.1a.lv/c/berniem-mazuliem/lego-rotallietas-un-lelles/lego/37h?lf=1"
url2 = "https://www.ksenukai.lv/c/rotallietas-preces-berniem/lego/dgs?lf=1"
url3 = ""

search1(url1,userid)
search1(url2,userid)