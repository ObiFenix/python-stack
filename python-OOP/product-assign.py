# ===================
# Assignment: Product
# ===================

# Objectives:
# ==================================================
# <>  Shall be able to making instances from a class
# <>  Shall be able to alter an instance's attributes
# <>  Shall access the methods and attributes of different instances
# ==================================================================

class Product:
    def __init__ (self, price, name, weight, brand):
        self.name = name
        self.brand = brand
        self.weight = float(weight[:-2])
        self.status = "for sale"  # Default attribute
        self.price = 0 if price <= 0 else price

    def displayAll( self ):
        product_info = "Item: {}\tBrand: {}\tWeight: {}lb\tPrice: ${}\tStatus: {}".format(
            self.name,
            self.brand,
            self.weight,
            self.price,
            self.status
        )
        print (product_info)
        return product_info

    def sell (self):
        self.status = "sold"
        return self

    def addTax (self, tax):
        if (self.status == "sold"): self.price += (self.price * tax)
        return self

    def returnItem(self, reason_for_return):
        self.status = "defective" if (reason_for_return == 'defective') else "like new"
        return self


if __name__ == '__main__':
    products = [
        Product(500, 'iPhoneX', '0.38lb', 'Apple'),
        Product(450, 'Note7', '0.37lb', 'Samsung'),
        Product(200, 'iPad', '1.6lb', 'Apple')
    ]
    products[1].sell()
    products[2].sell()
    products[0].sell()
    products[1].returnItem("defective")
    products[2].returnItem("")
    print ("\nProducts:\n" + "-"*len('Products'))
    for item in products: item.displayAll()
    print()
    # print (product1.returnItem("Wrong Item"))
