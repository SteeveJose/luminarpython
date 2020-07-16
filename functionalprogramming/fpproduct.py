class Product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price
    def __str__(self):
        return self.name
lst=[]
ob=lst.append(Product(101,"lux","soap",25))
ob=lst.append(Product(102,"colgate","toothpaste",50))
ob=lst.append(Product(103,"nike","shoe",1000))
def con(name):
    return name.upper()
print(con("nike"))
namelist=list(map(lambda product:product.name.upper(),lst))
print(namelist)
pricelist=list(filter(lambda product:product.price>50,lst))
for value in pricelist:
    print(value)