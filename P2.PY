inventory ={}
def add_product():
    name=input("Product:").strip().lower()
    try:
        qty=int(input("Quantity:"))
        price=float(input("Price:"))
        if qty < 0 or price < 0:
            print("Invalid values.")
            return
        inventory[name]={"qty":qty,"price":price}
        print("Saved.")
    except ValueError:
        print("Inavalid number.")
def show_products():
        if not inventory:
            print("No products.")        
            return
        total=0
        print("\nProduct qty price")
        for name,data in sorted(inventory.items()):
            value=data["qty"]*data["price"]
        total+=value
        print(f"{name.title():<16}{data['qty']:<10}{data['price']:.2f}")
def update_product():
    name=input("Product:").strip().lower()
    if name not in inventory:
        print("Not found.")
        return
    change=int(input("Quantity change:"))
    new_qty=inventory[name]["qty"]+change
    if new_qty>=0:
        inventory[name]["qty"]=new_qty   
while True:
    print("\n1 Add 2 Update 3 Show 4 Search 5 Exit")
    choice=input("choice:")
    if choice=="1":
        add_product()
    elif choice=="2":
        update_product()                     
    elif choice=="3":
        show_products()  
    elif choice=="4":
        key=input("Search:").lower()
        print(inventory.get(key,"Not found"))
    elif choice=="5":
        break
    else:
        print("Invalid choice")          