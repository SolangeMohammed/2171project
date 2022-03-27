from Inventory.inventory import Inventory
from Inventory.part import Part
from datetime import datetime

class InventoryManager():
    """
    Function to search the Inventory
    indx - index position in attribute array of search item
    search - item to search for
    parts - array of parts
    inventory - inventory object
    """
    def searchInventory(self, indx, search, inventory : Inventory):    

        searchResults = []
        
        for part in inventory.getParts():
            partAttributes = [part.id, part.name, part.qty, part.type, part.brand, part.reorderLevel, part.price]

            item = str(partAttributes[indx]).lower()
            if(not item.isnumeric()):
                if(str(search).lower() in item):
                    searchResults.append(part)
            else:
                if(int(search)==int(item)):
                    searchResults.append(part)
            
            
        return searchResults

    """
    Function to add a part
    """
    def addPart(self, id, name, qty, type, brand, reorderLevel, price, inventory : Inventory):
        #Add newpart to parts array
        parts = inventory.getParts()
        newPart = Part(id, name, qty, type, brand, reorderLevel, price)
        parts.append(newPart)
        #Update parts
        inventory.updateParts(parts)

        #Log Change
        self.logitem(newPart.getPart()[1], newPart.getPart()[2], datetime.now(), "Added")  

    """
    Function to edit a part
    """
    def editPart(self, id, attributeType, newValue, inventory : Inventory):

        #Find part to edit. Assuming only 1 item can be returned since searching by the ID
        found = self.searchInventory(0,id, inventory)
        part = found[0]

        #Change the attribute of the part
        if attributeType == '1': 
            part.setName(newValue)
        if attributeType == '2':
            part.setQty(newValue)
        if attributeType == '3':
            part.setType(newValue)
        if attributeType == '4':
            part.setBrand(newValue)
        if attributeType == '5':
            part.setReorderLevel(newValue)
        if attributeType == '6':
            part.setPrice(newValue)

        #Update the inventory file
        write_file=open('inventory_file.txt','w')
        for part in inventory.getParts():
            write_file.write(part)
        write_file.close()   

        #Log Change
        self.logitem(part.getPart()[1], part.getPart()[2], datetime.now(), "Edited")   

    def removePart(self, id, inventory : Inventory):
        #Find part to remove
        parts = inventory.getParts()
        parts.remove( self.searchInventory(0,id, inventory)[0] )

        #Update the inventory
        inventory.updateParts(parts)

        #Update the inventory file
        write_file=open('inventory_file.txt','w')
        for part in inventory.getParts():
            write_file.write(part)
        write_file.close() 

        self.logitem(part.getPart()[1], part.getPart()[2], datetime.now(), "Removed")   

    def logitem(self, name, qty, date, operation:str):
        file = open('LogFiles.txt', 'a')
        file.write(operation+" Item: "+str(name)+" "+str(qty)+" "+str(date)+"\n")
        file.close()


#--------------------------------------------------------

def newPart():
  part = Part
  part.id = input("Please enter an id: ")
  part.name = input("Please enter a name: ")
  part.qty = input("Please enter the quantity: ")
  part.type = input("Please enter a type: ")
  part.brand = input("Please enter the brand: ")
  part.reorderLevel = input("Please enter a reorder level: ")
  part.price = input("Please enter the price: ")
  addItem(part.id, part.name, part.qty, part.type, part.brand, part.reorderLevel, part.price)
  
def logitem(name, qty,date):
    file = open('LogFiles.txt', 'a')
    file.write("Added Item: "+name+" "+str(qty)+" "+str(date)+"\n")
    file.close()
    return 1

def addItem(id, name, qty, type, brand, reorderLevel, price):
    d=date.today()
    print("Adding Inventory")
    print("================")
    #name,brand,type='','',''
    #price=0.00
    #quantity,reorderLevel=0,0
    num=1
    
    if (name =='' or brand =='' or type =='' or price ==0.00 or qty ==0 or reorderLevel ==0):
        print("Missing infomation try again")
        num=0
        return "Missing infomation try again"


    #Adding New item to file, separated by ","
    file = open('inventory_file.txt', 'a')
    file.write( str(id)+ ',')
    file.write( name+ ',')
    file.write( str(qty)+ ',')
    file.write( type+ ',')
    file.write( brand+ ',')
    file.write( str(reorderLevel)+ ',')
    file.write( str(price))
    file.write("\n")
    file.close()
    #Adding Chnages to log file
    num=logitem(name,qty,d)
    #Sucesss Message
    if (num == 1):
        print("Success! New Item added to file")
        return "Success! New Item added to file"
    else:
        print("Error: Saving to Log failed")
        return "Error: Saving to Log failed"

def removeItem(idnum):
    print("Removing Item from Inventory")
    print("==================")
    #idnum= int(input("Enter the item id to remove from inventory: "))
     #read_file.close()

    read_file=open("inventory_file.txt",'r')
    lines = read_file.readlines()
    read_file.close()
       
    write_file=open('inventory_file.txt','w')
    write_file.write("")
    write_file.close()

    write_file=open('inventory_file.txt','a')
    for line in lines:
        attributes=line.split(",")
        if attributes[0].isdigit():
            if(int(attributes[0])!=idnum):
                write_file.write(line)
                
    write_file.close()        

    print("Success,item was removed from the inventory")
    return "Success,item was removed from the inventory"