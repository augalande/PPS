class product:
    def __init__(self,p_code,name,price):
        self.p_code=p_code
        self.name=name
        self.price=price
class STORE:
    def __init__(self):
        self.product_list=[]
    def add_products(self):
        p1=product(1,"Badminton Racquet",2000)
        self.product_list.append(p1)
        p2=product(2,"Cricket Bat",1500)
        self.product_list.append(p2)
        p3=product(3,"Basketball",500)
        self.product_list.append(p3)
        p4 = product(4, "Football", 1000)
        self.product_list.append(p4)
        p5 = product(5, "Volleyball", 250)
        self.product_list.append(p5)
    def display_product_list(self):
        print("Products in Store are ")
        for p in self.product_list:
            print("Code = ",p.p_code,"Name = ",p.name)
    def purchase_product(self,p_code):
        for p in self.product_list:
            if p.p_code==p_code:
                return p.price
        else:
            print("Product NOT Found !")
            return None
    def get_order(self):
        choice=1
        bill_amount=0
        while choice<5 and choice>0:
            choice=int(input("Enter choice \n (1) Purchase Product \n (2) Generate Bill \n (3) EXIT"))
            if choice==1:
                self.display_product_list()
                selected_code=int(input("Enter code of product to purchase"))
                price=self.purchase_product(selected_code)
                if price!=None:
                    bill_amount+=price
                else:
                    continue
            if choice==2:
                print("Current order bill is Rs. ",bill_amount)
            if choice==3:
                print("EXITED !")
store_1=STORE()
store_1.add_products()
store_1.get_order()