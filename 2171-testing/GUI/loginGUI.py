from tkinter import *
from tkinter import ttk

GUI

def loginGUI(self):
        def __init__ (self):

            super().__init__()
            self.geometry("780 x 500")
            self.resizable(False.False) #disables the resizing of the gui
            ##first screen that pops up
    #global screen
    def
    
    screen.geometry("300x300")
    screen.title("ASIMMS")
    screen.resizable(width=False,height=False)

    global login_state
    login_state=""
    global username
    username=StringVar()
    global password
    password=StringVar()
    global username_entered
    global password_entered
    global login_button
    global loggg
    
    Label(screen, text="Enter Credentials").pack()
    Label(screen,text="Username").pack()
    username_entered=Entry(screen, textvariable=username)
    username_entered.pack()
    Label(screen,text="Password").pack()
    password_entered=Entry(screen,textvariable=password)
    password_entered.pack()
    Label(screen, text="").pack()
    login_button= Button(text="Login",height=2,bg="lightgrey",activebackgroun="green",activeforeground="red",width="20",command=login).pack()
    Label(screen,height=2, text="").pack()
    Button(text="Create User",height=2,bg="lightgrey",width="20",command=create_user).pack()
    Label(screen, text="").pack()
    loggg=Label(screen, text="")
    
    
    screen.mainloop()#show screen

def login():    #check input against file to login
    global login_state
    #global mainscreenopen
    global mainscreenopen


    username_data=username.get()
    password_data=password.get()
    file=open("login_info.txt","r")
    #credential=file.readline()
    #credentials=credential.split(',')
    credential=file.readlines()
    print("usernamedata: "+username_data)
    print("passworddata: "+password_data)
    
 
    #result=Label(screen, text="Logged In").pack()
    #Label(screen, text=login_state).pack()
    
    for i in range(len(credential)):
        
        credentials=credential[i].split(',')
        credentials[1]=credentials[1].replace('\n','')#remove the newline character from end of string
        if username_data==credentials[0] and password_data==credentials[1] and mainscreenopen==0 :#//check password againts file working
            login_state="logged in"
            loggg.configure(text=login_state)
            loggg.pack()
            #print(login_state)
            open_program()
            mainscreenopen=1

        elif i>=len(credential)-1:
            
            login_state="Login Failed"
            loggg.configure(text=login_state)
            loggg.pack()
            #print(login_state)

    username_entered.delete(0,END)#clears the text that was input
    password_ente


def create_user():  
    print("create new user account")   
    reg_username=username.get()
    reg_password=password.get()
    file3=open("login_info.txt","a")
    file3.write("\n"+reg_username+","+reg_password)
    file3.close()
    loggg.configure(text="User created Sucessfully")
    loggg.pack()

    username_entered.delete(0,END)#clears the text that was input
    password_entered.delete(0,END)
red.delete(0,END)
    #file.close()