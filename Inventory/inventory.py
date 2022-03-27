from Inventory.part import Part



class Inventory:

    """
    Read all the parts from the file and add it to the inventory class on initialization
    """
    def __init__(self):
        read_file = open("inventory_file.txt",'r')
        lines = read_file.readlines()
        parts = []

        for line in lines:
            attribute = line.rstrip("\n").split(",")
            parts.append(Part(attribute[0], attribute[1], attribute[2], attribute[3], attribute[4], attribute[5], attribute[6]))
            
        read_file.close()        
        self.parts = parts

    """
    Print current inventory to the console
    """
    def displayInventory(self):
        for part in self.parts:
            print(part)


    """
    Get current part array
    """
    def getParts(self):
        return self.parts
    
    """
    Set current part array to new part array
    """
    def updateParts(self, parts):
        self.parts = parts







