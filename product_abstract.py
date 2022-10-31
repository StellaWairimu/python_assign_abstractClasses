##Abstract classes
#concept in OOP whereby the core functionality is hidden from the user.
#You cannot call the class directly
#You cannot call the function directly.
#Its accesed through inheritance form the abstarct class.
#Serves as a point of reference

from abc import ABC , abstractmethod

class Product():
    productName =""
    color =""
    date_of_entry =""
    units =0
    date_of_expiry =""
    
   


class ProductAbstract(ABC):

    @abstractmethod
    def create_product(self):
        print("Product creation and entry")
    
    @abstractmethod
    def get_all_products(self):
        print("Product information")

    @abstractmethod
    def get_product_by_id(self , user_id):
        print("Displays the product by the unique ID entered on search")

    @abstractmethod
    def edit_product():
        print("Making changes to the product in realtime")

    @abstractmethod
    def upload_product_image():
        print("Enter the jpg image of the product")

    @abstractmethod
    def delete_product():
        print("Hard deleting the product from the database")

class ProductManagement(ProductAbstract):

    def create_product(self):
        pass

    def get_all_products(self):
        pass
    
    def get_product_by_id(self, user_id):
        return super().get_product_by_id(user_id)
    
    def edit_product():
        pass

    def upload_product_image():
        pass

    def delete_product():
        pass

prod=ProductManagement()
prod.create_product
prod.delete_product
prod.get_all_products
prod.get_product_by_id(100)
prod.upload_product_image

  