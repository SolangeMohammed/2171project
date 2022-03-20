from tkinter import *
from tkinter import ttk
from Inventory.inventoryManager import *
from Inventory.inventory import *
from Inventory.part import *
from GUI.loginGUI import *



#mainFrame=Frame()
screen=Tk()
screen.title("ASIMS")

#screen_main=Toplevel(screen)
#screen_main=Tk()


#mainFrame=Frame(screen_main)
#mainFrame.grid(row=0,column=1,rowspan=6,columnspan=2)

filepath="inventory_file.txt" 
mainscreenopen=0#check if main screen of program already open, 0 not open, 1 is open

#global searchedresults
#searchredesults=[""]*search.searchsize
searchedresults=[""]*4

global login_state
login_state=""
global table



def clear_screen():
    
    for widgets in mainFrame.winfo_children():
      widgets.destroy()




if __name__ == "__main__":
  """Inventory Class Testing"""
  Inventory = Inventory()
  Inventory.displayInventory()

  InventoryManager = InventoryManager()

  #-------------------------------------------------------------------------
  """Edit Part Testing"""
  id = input("Enter the id of the part you want to edit: ")
  attributeType = input("Enter what attribute of  the item you would like to change. Please pick from this list: 1. Name, 2. Quantity, 3. Type, 4. Brand, 5. Reorder Level, 6. Price: ") 
  attributes = {1:"Name", 2:"Quantity", 3:"Type", 4:"Brand", 5:"Reorder Level", 6:"Price"}

  newValue = input("Please enter the new item name: ")

  InventoryManager.editPart(id, attributeType, newValue, Inventory)
  print(f'{attributes[attributeType]} was updated to {newValue}')

  #-------------------------------------------------------------------------------------------
  """Search Inventory Testing"""
  while True:
      x = input("Please enter the number that corresponds with your search parameters:\n 1. ID\n 2. Product Name\n 4. Product Type\n 5. Product Brand\n")
      search = input("Please enter search criteria:\n")
      
      results = InventoryManager.searchInventory(int(x)-1, search, Inventory)
      
      for result in results:
          print(result)