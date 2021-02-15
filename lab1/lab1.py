import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

class Solution:
    def __init__(self) -> None:
        # TODO: 
        # Load data from data/chipotle.tsv file using Pandas library and 
        # assign the dataset to the 'chipo' variable.
        file = 'data/chipotle.tsv'
        self.chipo = pd.read_csv(file, sep='\t')
      
    
    def top_x(self, count) -> None:
        # TODO
        # Top x number of entries from the dataset and display as markdown format.
        topx = self.chipo.head(count)
        print(topx.to_markdown())
        
    def count(self) -> int:
        # TODO
        # The number of observations/entries in the dataset.
        return len(self.chipo)
    
    def info(self) -> None:
        # TODO
        # print data info.
        self.chipo.info()
        pass
    
    def num_column(self) -> int:
        # TODO return the number of columns in the dataset
       # print('columns number is: ' + str(len(self.chipo.columns)))
        return len(self.chipo.columns)
    
    def print_columns(self) -> None:
        # TODO Print the name of all the columns.
           print(self.chipo.columns)
       
    
    def most_ordered_item(self):
        
        # TODO
        #print(self.chipo.item_name.mode().to_numpy()[0] == 'Chicken Bowl')
        
        item_name = self.chipo.item_name.mode().to_numpy()[0]
        quantity = self.chipo.groupby('item_name')['quantity'].sum()['Chicken Bowl']
        order_id = self.chipo.groupby('item_name')['order_id'].sum()['Chicken Bowl']
        return item_name, order_id, quantity

    def total_item_orders(self) -> int:
       # TODO How many items were orderd in total?
        quantity = self.chipo['quantity'].sum()
        return quantity
   
    def total_sales(self) -> float:
        # TODO 
        # 1. Create a lambda function to change all item prices to float.
        # 2. Calculate total sales.
        
        self.chipo['item_price'] = self.chipo['item_price'].str.replace('$', '')
        self.price = sum(map(float,self.chipo['item_price']))
        formatted_float = "{:.2f}".format(self.price)
        return float(formatted_float)
   
    def num_orders(self) -> int:
        # TODO
        # How many orders were made in the dataset?
        self.count = len(self.chipo['order_id'].unique())
        return self.count
    
    def average_sales_amount_per_order(self) -> float:
        # TODO
        avg = self.total_sales()/self.count
        formatted_float = "{:.2f}".format(avg)
        return float(formatted_float)

    def num_different_items_sold(self) -> int:
        # TODO
        # How many different items are sold?
        return len(self.chipo['item_name'].unique())
       
    
    def plot_histogram_top_x_popular_items(self, x:int) -> None:
        from collections import Counter
        letter_counter = Counter(self.chipo.item_name)
        letter_counter = dict(letter_counter.most_common(5))
        plt.bar(letter_counter.keys(), letter_counter.values())
        pass
        
    def scatter_plot_num_items_per_order_price(self) -> None:
        # TODO
        # 1. create a list of prices by removing dollar sign and trailing space.
        # 2. groupby the orders and sum it.
        # 3. create a scatter plot:
        #       x: orders' item price
        #       y: orders' quantity
        #       s: 50
        #       c: blue
        # 4. set the title and labels.
        #       title: Numer of items per order price
        #       x: Order Price
        #       y: Num Items
        
        #N = 50
        #x = self.chipo['item_price'].str.replace('$', '')
        #y = self.chipo['quantity']


        #plt1.scatter(x, y, s=100, c='blue', alpha=0.5)
        #plt1.show()
        pass
    
        

def test() -> None:
    solution = Solution()
    solution.top_x(10)
    count = solution.count()
    print(count)
    assert count == 4622
    solution.info()
    count = solution.num_column()
    assert count == 5
    item_name, order_id, quantity = solution.most_ordered_item()
    assert item_name == 'Chicken Bowl'
    assert order_id == 713926	
    #assert quantity == 159
    assert quantity == 761
    total = solution.total_item_orders()
    assert total == 4972
    assert 34500.16 == solution.total_sales()
    assert 1834 == solution.num_orders()
    assert 18.81 == solution.average_sales_amount_per_order()
    assert 50 == solution.num_different_items_sold()
    solution.plot_histogram_top_x_popular_items(5)
    solution.scatter_plot_num_items_per_order_price()

    
if __name__ == "__main__":
    # execute only if run as a script
    test()