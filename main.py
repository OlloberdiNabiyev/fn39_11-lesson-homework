from abc import ABC,abstractmethod

# 1
# class Product(ABC):
#     def __init__(self,name,price,categories:list,in_stock):
#         self.__name = name
#         self.__price = price
#         self.categories = categories
#         self.in_stock = in_stock
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self,value):
#         self.__name = value
    
#     @name.deleter
#     def name(self):
#         del self.__name
    
#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self,value):
#         self.__price = value
    
#     @price.deleter
#     def price(self):
#         del self.__price

#     @property
#     def categorie(self):
#         return self.categories
    
#     @categorie.setter
#     def categorie(self,value):
#         self.categories.append(value)
#     @abstractmethod
#     def get_info(self):
#         pass

# class ElectronicProduct(Product):
#     def __init__(self, name, price, categories:list, in_stock,warranty_years):
#         super().__init__(name, price, categories, in_stock)
#         self.__warranty_years = warranty_years
#     @property
#     def warranty_years(self):
#         return self.__warranty_years
    
#     @warranty_years.setter
#     def warranty_years(self,value):
#         self.__warranty_years = value
    
#     @warranty_years.deleter
#     def warranty_years(self):
#         del self.__warranty_years

#     def get_info(self):
#         pass
# e1 = ElectronicProduct('phone',500,['smartphones','iphones'],5,1)
# e2 = ElectronicProduct('fridge',800,['fridges','refrigerators'],20,3)
# e1.categories = 'smartphones'
# print(hasattr(e1,'_Product__price'))
# print(getattr(e1,'_Product__price'))
# setattr(e1,'in_stock',10)
# delattr(e1,'_ElectronicProduct__warranty_years')
# print(e1.__dict__)
