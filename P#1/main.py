
from P1 import Item, Book, SoccerBall, Candle, CoffeeMachine, Customer,Amazon

#*****************************

amazon=Amazon()


Arezoo_ID=amazon.create_account(name="Arezoo")
Negin_ID=amazon.create_account(name="Negin")

amazon.customers[Arezoo_ID].deposit(amount=1000)
amazon.customers[Negin_ID].deposit(amount=1000)


# amazon.customers[Arezoo_ID].withdraw(2000)
Sankara_ID=amazon.create_account(name="Sankara")
Sandeep_ID=amazon.create_account(name="Sandeep")
# print(amazon.customers)
amazon.check_Customer_id(Negin_ID)


# amazon.delete_account(Sankara_ID)
# print(amazon.customers)



book1=Book()
book2=Book()
book3=Book()
coffee1=CoffeeMachine()
coffee2=CoffeeMachine()
coffee3=CoffeeMachine()
candle=Candle()
socer=SoccerBall()


amazon.add_to_cart(Arezoo_ID,book1)
amazon.add_to_cart(Arezoo_ID,book2)
amazon.add_to_cart(Arezoo_ID,book3)
amazon.add_to_cart(Arezoo_ID,coffee1)
amazon.add_to_cart(Arezoo_ID,coffee2)
amazon.add_to_cart(Arezoo_ID,candle)
amazon.add_to_cart(Arezoo_ID,socer)
amazon.show_cart(Arezoo_ID)



# print(amazon.remove_from_cart(Arezoo_ID,coffee2))
# amazon.show_cart(Arezoo_ID)
# print(amazon.remove_from_cart(Arezoo_ID,coffee1))
# amazon.show_cart(Arezoo_ID)
# print(amazon.remove_from_cart(Arezoo_ID,candle))
# amazon.show_cart(Arezoo_ID)
# print(amazon.remove_from_cart(Arezoo_ID,socer))
# amazon.show_cart(Arezoo_ID)
# print(amazon.remove_from_cart(Arezoo_ID,book1))
# amazon.show_cart(Arezoo_ID)

# print(amazon.remove_from_cart(Arezoo_ID,coffee3))
# amazon.show_cart(Arezoo_ID)


# amazon.clear_cart(Arezoo_ID)
# amazon.buy_item(Arezoo_ID,book1)
# print(amazon.customers[Arezoo_ID].balance)
# print(amazon.customers[Arezoo_ID].money_spent)
# print("**************")

# amazon.buy_item(Arezoo_ID,socer)
# amazon.show_cart(Arezoo_ID)
# print(amazon.customers[Arezoo_ID].balance)
# print(amazon.customers[Arezoo_ID].money_spent)
# print("**************")

# amazon.buy_item(Arezoo_ID,book2)
# print(amazon.customers[Arezoo_ID].balance)
# print(amazon.customers[Arezoo_ID].money_spent)
# print("**************")
#


#
# # print(amazon.customers[Arezoo_ID].balance)
# print(amazon.remove_from_cart(Arezoo_ID,book1))
# amazon.show_cart(Arezoo_ID)
# print(amazon.remove_from_cart(Arezoo_ID,socer))
# amazon.show_cart(Arezoo_ID)
# print(amazon.remove_from_cart(Arezoo_ID,coffee2))
# amazon.show_cart(Arezoo_ID)
#
# amazon.buy_entire_cart(Arezoo_ID)
# amazon.show_cart(Arezoo_ID)
# print(amazon.customers[Arezoo_ID].balance)
# print(amazon.customers[Arezoo_ID].money_spent)












