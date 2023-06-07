import pandas as pd

class mySGBD():
    def __init__(self) -> None:
        # initialize the tables
        self.prd = pd.read_csv("./actions/products.csv", sep=',')


        self.allowed_categories = list(self.prd['category'].unique()) # list of the allowed categories
        
        self.allowed_RAM = [] # list of the allowed colors for the chosen category
        
        self.allowed_sizes = [] # list of the allowed sizes for the chosen color
        
        self.allowed_prd = None # table of the allowed products for the chosen size
        self.allowed_products = [] # list of the allowed products

        self.allowed_quantity = 1 # product quantity in stock
    
    #get available RAMs for the chosen category
    def get_RAM_by_category(self, category):

        self.allowed_prd = self.prd[self.prd['category'].str.lower() == category.lower()]
        self.allowed_RAM = list(self.allowed_prd['RAM'].unique())
        
        return self.allowed_RAM

     #get available processors for the chosen category
    def get_processor_by_RAM(self, RAM):

        self.allowed_prd = self.allowed_prd[self.allowed_prd['RAM'] == RAM]
        self.allowed_processor = list(self.allowed_prd['processor'].unique())
        
        return self.allowed_processor
    
     #get available processors for the chosen category
    def get_storage_capacity_by_processor(self, processor):

        self.allowed_prd = self.allowed_prd[self.allowed_prd['processor'] == processor]
        self.allowed_storage_capacity = list(self.allowed_prd['storage_capacity'].unique())
        
        return self.allowed_storage_capacity

     #get available processors for the chosen category
    def get_brand_by_storage_capacity(self, storage_capacity):

        self.allowed_prd = self.allowed_prd[self.allowed_prd['storage_capacity'] == storage_capacity]
        self.allowed_brand = list(self.allowed_prd['brand', 'price'].unique())
        
        return self.allowed_brand
    
    # #get available processors for the chosen category
    # def get_price_by_brand(self, brand):

    #     self.allowed_prd = self.allowed_prd[self.allowed_prd['brand'] == brand]
    #     self.allowed_price = list(self.allowed_prd['price'].unique())
        
    #     return self.allowed_price
    
    # #get available product's quantity for the chosen product name
    # def get_product_quantity_by_size(self):

    #     self.allowed_quantity = self.allowed_prd_s['size_quantity'].tolist()[0]

    #     return self.allowed_quantity
    
    # #update the quantity of the ordered product
    # def update_quantity(self, product, color, size, ordered_quantity):
        
    #     self.prd_s.loc[(self.prd_s['product_id'] == product.id) & (self.prd_s['color_id'] == color.id) & (self.prd_s['size'].str.lower() == size.lower()), 'size_quantity'] -= ordered_quantity

        
    #     self.prd_s = self.prd_s[self.prd_s['size_quantity'] > 0]

        
    #     self.prd_c.loc[(self.prd_c['product_id'] == product.id) & (self.prd_c['id'] == color.id), 'color_quantity'] -= ordered_quantity

        
    #     self.prd_c = self.prd_c[self.prd_c['color_quantity'] > 0]

         
    #     self.prd.loc[self.prd['id'] == product.id, 'quantity'] -= ordered_quantity

        
    #     self.prd = self.prd[self.prd['quantity'] > 0]



    
if __name__ == '__main__':

    #code to test the functions
    sgbd = mySGBD()
    categories = sgbd.allowed_categories
    print(categories)

    RAM = sgbd.get_RAM_by_category('Laptop')
    print(sgbd.allowed_prd)
    print(RAM)