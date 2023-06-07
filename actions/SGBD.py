import pandas as pd

class mySGBD():
    def __init__(self) -> None:
        # initialize the tables
        self.prd = pd.read_csv("./actions/products.csv", sep=',')

        self.prd['category'] = self.prd['category'].str.lower()
        self.allowed_categories = list(self.prd['category'].unique()) # list of the allowed categories
           
        self.allowed_RAMs = [] 
        self.allowed_processors = [] 
        self.allowed_storage_capacities = []
        self.allowed_brand_price = []
        self.allowed_brands = []
        self.allowed_quantity = 1 # product quantity in stock
    
    #get available RAMs for the chosen category
    def get_RAM_by_category(self, category):

        self.allowed_prd = self.prd[self.prd['category'].str.lower() == category.lower()]
        self.allowed_RAMs = list(self.allowed_prd['RAM'].unique())
        
        return self.allowed_RAMs

     #get available processors for the chosen category
    def get_processor_by_RAM(self, RAM):

        self.allowed_prd = self.allowed_prd[self.allowed_prd['RAM'] == RAM]
        self.allowed_processors = list(self.allowed_prd['processor'].unique())
        
        return self.allowed_processors
    
     #get available processors for the chosen category
    def get_storage_capacity_by_processor(self, processor):

        self.allowed_prd = self.allowed_prd[self.allowed_prd['processor'] == processor]
        self.allowed_storage_capacities = list(self.allowed_prd['storage_capacity'].unique())
        
        return self.allowed_storage_capacities

     #get available processors for the chosen category
    def get_brand_by_storage_capacity(self, storage_capacity):

        self.allowed_prd = self.allowed_prd[self.allowed_prd['storage_capacity'] == storage_capacity]
        self.allowed_brand_price = self.allowed_prd[['brand', 'price']].values.tolist()
        self.allowed_brands = self.allowed_prd['brand'].tolist()
        
        return self.allowed_brand_price
    
    def get_product_quantity_by_brand(self, brand):

        self.allowed_prd = self.allowed_prd[self.allowed_prd['brand'] == brand]
        self.allowed_quantity = self.allowed_prd['quantity'].tolist()[0]

        return self.allowed_quantity
    
    def update_quantity(self, ordered_quantity):
        product_info = self.allowed_prd.values.tolist()
        product_id = product_info[0][0]
         
        self.prd.loc[self.prd['id'] == product_id, 'quantity'] -= int(ordered_quantity)

        self.prd = self.prd[self.prd['quantity'] > 0]

    
if __name__ == '__main__':

    # #code to test the functions
    # sgbd = mySGBD()
    # categories = sgbd.allowed_categories
    # print(categories)

    # RAM = sgbd.get_RAM_by_category('Laptop')
    # print(RAM)

    # processors = sgbd.get_processor_by_RAM('32GB')
    # print(processors)

    # capacities = sgbd.get_storage_capacity_by_processor('Intel Core i9')
    # print(capacities)

    # brands = sgbd.get_brand_by_storage_capacity('1TB SSD')
    # print(brands)

    # quantity = sgbd.get_product_quantity_by_brand('HP')
    # print(sgbd.allowed_prd)
    # print(quantity)

    # sgbd.update_quantity(5)

    pass
