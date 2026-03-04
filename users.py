from abc import ABC
from orders import Order
#eta holo user class 
class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart=Order()
    
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("Item not found")
    
    def view_cart(self):
        print("** view_cart **")
        print("Name \t Price \t Quantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name} \t {item.price} \t {item.quantity}")
        print(f"total price {self.cart.total_price}")

    def Pay_bill(self):
        print(f"total {self.cart.total_price} paid successfully")
        self.cart.clear()


#eta holo employee class
class Employee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        super().__init__(name, email, phone, address)
        self.age=age
        self.designation=designation
        self.salary=salary

#eta admin class
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    #eta shudhu employee er jony
    def add_employee(self,Restaurent,employee):
        Restaurent.add_employee(employee)
    
    
    def view_employee(self,Restaurent):
        Restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()





# restaurent=Restaurent("Mamar Rstora")
 # mn=Menu()
# item=FoodItem("Pizza",12.45,30)
# item2=FoodItem("Burger",15,50)
# admin=Admin("imran","imran@gmail.com","01345","Dhaka")
# admin.add_new_item(restaurent,item)
# admin.add_new_item(restaurent,item2)
# mn.add_menu_item(item)
# mn.add_menu_item(item2)
#mn.show_menu()



# customer1=Customer("imran","imran@gmail.com","01345","Dhaka")
# customer1.view_menu(restaurent)

# item_name=input("Enter Item name:")
# item_quantity=int(input("Enter Item quantity:"))

# customer1.add_to_cart(restaurent,item_name,item_quantity)
# customer1.view_cart()


    
     
        