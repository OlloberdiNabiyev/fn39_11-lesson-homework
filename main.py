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




# 2
# class Team(ABC):
#     def init(self,team_name,coach,players,country):
#         self.team_name = team_name
#         self.__coach = coach
#         self.players = players
#         self.country = country
        
#     @property
#     def team_name(self):
#         return self.__team_name
    
#     @team_name.setter
#     def team_name(self,value):
#         self.__team_name = value
    
#     @team_name.deleter
#     def team_name(self):
#         del self.__team_name
    

#     @property
#     def coach(self):
#         return self.__coach
    
#     @coach.setter
#     def coach(self,value):
#         self.__coach = value
    
#     @coach.deleter
#     def coach(self):
#         del self.__coach

#     @property
#     def player(self):
#         return self.players
#     @player.setter
#     def player(self,value):
#         self.players.append(value)

#     @abstractmethod
#     def get_info(self):
#         pass


# class FotballTeam(Team):
#     def __init(self, team_name, coach, players, country,stadium):
#         super().init(team_name, coach, players, country)
#         self.stadium = stadium

#     @property
#     def stadium(self):
#         return self.__stadium

#     @stadium.setter
#     def stadium(self,value):
#         self.__stadium = value
    
#     @stadium.deleter
#     def stadium(self):
#         del self.__stadium

#     def get_info(self):
#         pass

#     @staticmethod
#     def is_full_team(players_list):
#         count = 0
#         for player in players_list:
#             count += 1
#         return count >= 11
# f1 = FotballTeam('Navbahor','Kapadze',['Azim Ahmedov','Igor golban','Quvondiq Ro\'ziyev','Doniyor Abdumannopov','Zabihillo O`rinboyev','Otkir yusupov','Ruslanbek Jiyanov','Jamshid boltaboyev','Jovan Đokić','Jasurbek Yaxshiboyev','Abror Ismoilov'],'Uzbekistan','Namangan Markaziy Stasioni')
# f2 = FotballTeam('Neftchi','Islombek Ismoilov',['Botirali Ergashev','Eldorbek Suyunov','Akbar Turaev','Shohruhbek Yoqubjonov','Anvarjon Gofurov','Ibrohimkhalil Yoldoshev','Farrukh Sayfiyev','Mukhsin Ubaydullayev','Izzatillo Polatov','Ratinho','Jamshid Iskanderov'],'Uzbekistan','Istiqlol stadium')
# f1.player = 'Anri Chichinadze'
# print(f1.player)
# print(f1.is_full_team(f1.player))
# print(f1.coach)
# f1.stadium = 'Navbahor markaziy stadioni'
# del f1.country
# print(f1.__dict)
# print(hasattr(f2,'coach'))
# print(getattr(f2,'coach'))
# setattr(f2,'country','O\'zbekiston')
# delattr(f2,'stadium')
# print(f2.dict)
# print(f2.is_full_team(f2.player))