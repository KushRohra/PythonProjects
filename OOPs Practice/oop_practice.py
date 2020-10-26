from json import dumps, loads

class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price
	def to_dict(self):
		return {"name": self.name, "price": self.price}

def add_Product(name, price):
	new_product = Product(name, price)
	products.append(new_product)

def save_products(products):
	product_save_list = []
	for product in products:
		product_save_list.append(product.to_dict())
	products_file = open("products.json", "w+")
	products_file.write(dumps(product_save_list))
	products_file.close()

def load_products():
	try : 
		products_file = open("products.json", "r")
	except IOError:
		return []
	products_json = products_file.read()
	product_data = loads(products_json)
	products_file.close()

	products = []
	for product in product_data:
		products.append(Product(product['name'], product['price']))
	return products

def list_products(products):
	for product in products:
		print(product.name, " Rs.", product.price)

def total_products(products):
	total = 0
	for product in products:
		total += product.price
	print("Your total cost of all the products is: "+str(total))

products = load_products()

while True:
	print("Type add to add a product.")
	print("Type quit to quit the program.")
	print("Type list to see list of all Products")
	print("Type total to see total cost of all the Products")
	command = input("Type a command: ")

	if command == 'quit':
		save_products(products)
		break 

	if command == 'add':
		product_name = input("Enter a name for your Product: ")
		try :
			product_price = float(input("Enter a price for your new Product in Rs: "))
		except ValueError:
			print("Enter a valid price")
			continue
		add_Product(product_name, product_price)

	if command == 'list':
		list_products(products)

	if command == 'total':
		total_products(products)