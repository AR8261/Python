import uuid

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'{self.name}:{self.price}$--{self.id}'
# ****************************
class Book(Item):
    def __init__(self,name="Book",price=15):
        super().__init__(name=name,price=price)
# ****************************
class CoffeeMachine(Item):
    def __init__(self,name="CoffeeMachine",price=100):
        super().__init__(name=name,price=price)
# ****************************
class SoccerBall(Item):
    def __init__(self,name="SoccerBall",price=25):
        super().__init__(name=name,price=price)
# ****************************
class Candle(Item):
    def __init__(self,name="Candle",price=5):
        super().__init__(name=name,price=price)
# ****************************
class Customer:
    def __init__(self, name):
        self.id = uuid.uuid1()
        self.name = name
        self.cart = []
        self.balance = 0
        self.money_spent = 0

    def __repr__(self):
        return f"Name:{self.name} ,balance:{self.balance}$,Money Spent:{self.money_spent}$ "

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(" You don't have sufficient funds ")
        self.balance -= amount
# ***************************************************************
class Amazon():
    def __init__(self):
        self.customers = {}
#*****************************************
    def create_account(self, name):
        customer = Customer(name=name)
        self.customers[customer.id]=customer
        return customer.id

#*********************************************************
    def check_Customer_id(self,customer_id):
        if (customer_id in self.customers):
            pass
        else :
            raise ValueError("customer_id does not exist")

# *****************************************
    def delete_account(self,customer_id):
        self.check_Customer_id(customer_id)
        if customer_id in self.customers:
            del self.customers[customer_id]
# *****************************************
    def add_to_cart(self,customer_id,item):
        self.check_Customer_id(customer_id)
        self.customers[customer_id].cart.append(item)
# *****************************************
    def remove_from_cart(self,customer_id,item):
        self.check_Customer_id(customer_id)
        if item in self.customers[customer_id].cart:
            self.customers[customer_id].cart.remove(item)
            removed_item = item
        else:
            removed_item = None
        return removed_item
#********************************************************
    def buy_item(self,customer_id,item):
        self.check_Customer_id(customer_id)
        if item in self.customers[customer_id].cart:
            if self.customers[customer_id].balance >= item.price:
                self.customers[customer_id].money_spent += item.price
                self.customers[customer_id].balance-=self.customers[customer_id].money_spent
                self.customers[customer_id].cart.remove(item)
            else:
                raise ValueError("You don't have sufficient fund in your balance")
        else:
            raise ValueError("item was not found in your cart")
#*****************************************************
    def buy_entire_cart(self,customer_id):
        self.check_Customer_id(customer_id)
        total_amount=0
        book_counter=0
        coffemachine_counter=0
        candle_counter=0
        soccer_counter=0
        for item in range(0, len(self.customers[customer_id].cart)):
            if isinstance(self.customers[customer_id].cart[item], Book):
                book_counter += 1
            elif isinstance(self.customers[customer_id].cart[item], CoffeeMachine):
                coffemachine_counter += 1
            elif isinstance(self.customers[customer_id].cart[item], Candle):
                candle_counter += 1
            else:
                soccer_counter += 1

            total_amount += (self.customers[customer_id].cart[item].price)
        if (book_counter >=3 or coffemachine_counter>=3 or candle_counter>=3 or soccer_counter>=3):
            total_amount*=0.9
        if self.customers[customer_id].balance >= total_amount:
            self.clear_cart(customer_id)
            self.customers[customer_id].money_spent+=total_amount
            self.customers[customer_id].balance -= total_amount
        else:
            raise ValueError("You don't have sufficient fund in your balance to buy these items")
# ***************************************************
    def clear_cart(self,customer_id):
        self.check_Customer_id(customer_id)
        self.customers[customer_id].cart.clear()
# *****************************************************
    def show_cart(self,customer_id):
        book_counter = 0
        coffemachine_counter = 0
        candle_counter = 0
        soccer_counter = 0
        self.check_Customer_id(customer_id)
        print(f"Total  # of items: {len(self.customers[customer_id].cart)}")
        for item in range(0, len(self.customers[customer_id].cart)):
            # print(f"{self.customers[customer_id].cart[item].name}")
            if isinstance(self.customers[customer_id].cart[item],Book):
                book_counter +=1
            elif isinstance(self.customers[customer_id].cart[item], CoffeeMachine):
                coffemachine_counter+=1
            elif isinstance(self.customers[customer_id].cart[item], Candle):
                candle_counter+=1
            else :
                soccer_counter+=1
        print(f"Total  # of books:{book_counter}")
        print(f"Total # of candles :{candle_counter}")
        print(f"Total # of coffee machines :{coffemachine_counter}")
        print(f"Total  # of soccer balls :{soccer_counter}")

        print("Cart Contents:")
        for item in self.customers[customer_id].cart:
            print(f"{item}")



