from foodItem import FoodItem
from menu import Menu
from orders import Order
from restaurents import Restaurent
from users import User,Employee,Admin,Customer

restaurent=Restaurent("Mamar Restaurent")

def customer_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your Phone: ")
    address=input("Enter your address: ")
    customer=Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome to {customer.name}!!")
        print("1.View menu")
        print("2.Add item to cart")
        print("3.View cart")
        print("4.Paybill")
        print("5.Exit")

        choice=int(input("Enter your choiche: "))
        if choice==1:
            customer.view_menu(restaurent)
        elif choice==2:
            item_name=input("Enter item name: ")
            item_quantity=int(input("Enter item quantity: "))
            customer.add_to_cart(restaurent,item_name,item_quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.Pay_bill()
        elif choice==5:
            break
        else:
            print("Invalid input")


def admin_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your Phone: ")
    address=input("Enter your address: ")
    admin=Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome to {admin.name}!!")
        print("1.Add new item")
        print("2.Add new employee")
        print("3.View employee")
        print("4.View menu")
        print("5.Remove items")
        print("6.Exit")

        choice=int(input("Enter your choiche: "))
        if choice==1:
            item_name=input("Enter Item name: ")
            item_price=int(input("Enter item price: "))
            item_quantity=int(input("Enter item quantity: "))
            item=FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(restaurent,item)
        elif choice==2:
            name=input("Enter employee name: ")
            phone=input("Enter employee number: ")
            email=input("Enter employee email: ")
            address=input("Enter employee address: ")
            age=input("Enter employee age: ")
            designation=input("Enter employee designation: ")
            salary=input("Enter employee salary: ")
            employee=Employee(name=name,email=email,phone=phone,address=address,
                              age=age,designation=designation,salary=salary)
            admin.add_employee(restaurent,employee)
        elif choice==3:
            admin.view_employee(restaurent)
        elif choice==4:
            admin.view_menu(restaurent)
        elif choice==5:
            item_name=input("Enter item name: ")
            admin.remove_item(restaurent,item_name)
        elif choice==6:
            break
        else:
            print("Invalid input")


while True:
    print("Welcome !!!")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid syntax ")
