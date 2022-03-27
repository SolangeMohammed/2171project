
class Part:          

    def __init__(self, id, name, qty, type, brand, reorderLevel, price):
        self.id = id
        self.name = name 
        self.qty = qty
        self.type = type
        self.brand = brand
        self.reorderLevel = reorderLevel
        self.price = price

    def description(self):                
        return f"The {self.name} part costs {self.price} dollars"

    def setId(self, id):
        self.id = id
        return f"{self.name} ID changed to {self.id}"
        
    def setName(self, name):
        self.name = name
        return f"Name changed to {self.name}"

    def setQty(self, qty):
        self.qty = qty
        return f"{self.name} qty updated to {self.qty}"

    def setType(self, type):
        self.type = type
        return f"{self.name} type changed to {self.type}"

    def setBrand(self, brand):
        self.brand = brand
        
    def setReorderLevel(self, reorderLevel):
        self.reorderLevel = reorderLevel
        return f"{self.name} reorder level changed to {self.reorderLevel}"

    def setPrice(self, price):
        self.price = price
        return f"{self.name} price changed to {self.price}"

    def getPart(self): 
        return [self.id, self.name, self.qty, self.type, self.brand, self.reorderLevel, self.price]

    def isLow(self):
        if self.qty < self.reorderLevel:
            return(True)
            
    def CheckStock(self,isLow):
        if isLow:
            print(f"The current stock is {self.reorderLevel} please restock")
        else:
            print(f"The current stock is {self.reorderLevel} no need to restock")

    def __str__(self):
        return f'{self.id},{self.name},{self.qty},{self.type},{self.brand},{self.reorderLevel},{self.price}'


