import csv
class Item:
    
    pay_rate=0.8 
    all_item=[]
    def __init__(self,name: str,price:float,quantity=0):
        #Run validations to the received arguments
        assert price>=0, f"The price must be equal or greater than zero, {price} is less than zero"
        assert quantity>=0, f"The quantity must be equal or greater than zero, {quantity} is less than zero"

        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

        #Actions to execute
        Item.all_item.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv",'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
class Phone(Item):
    all=[]
    def __init__(self,name: str,price:float,quantity=0,broken_phones=0):
        #Run validations to the received arguments
        assert price>=0, f"The price must be equal or greater than zero, {price} is less than zero"
        assert quantity>=0, f"The quantity must be equal or greater than zero, {quantity} is less than zero"
        assert broken_phones, f"The number of broken phones must be equal or greater than zero, {broken_phones} is less than zero"

        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        self.broken_phones=broken_phones

        #Actions to execute
        Phone.all_item.append(self)
    

Iphone16=Phone('Iphone 16',500,5,1)
print(Iphone16.calculate_total_price())
