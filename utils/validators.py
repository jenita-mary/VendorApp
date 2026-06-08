from email_validator import validate_email, EmailNotValidError
from tkinter import *



class Validator:

    def __init__(self, home):
        self.home_fn = home
        print("Validating....")  


    def __getattr__(self, name):
        return getattr(self.home_fn, name)
    
    def is_valid_email(self,email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False
        
    def verify(self):#Function verify validates the email and password for the new vendor on button click
        testemail=self.ent1.get()
        testemail=testemail.casefold()
        match1=self.cursor.execute("select Id from seller where Email ='"+testemail+"'")
        match=match1.fetchall()
        pass1=self.ent2.get()
        id = 0
        con_u=0
        con_l=0
        con_d=0
        con_s=0
        for i in pass1:
            if i.isupper()==True:
                con_u+=1
            elif i.islower()==True:
                con_l+=1
            elif i.isdigit()==True:
                con_d+=1
            elif i.isalnum()==False:
                con_s+=1
        self.home_fn.mail= testemail

        if self.is_valid_email(testemail)==0:
            self.lab1.config(text="Invalid EmailId")
            self.after(id)
        elif len(match)==1:
            self.lab1.config(text="Email already exists")           
            self.after(id)
        elif len(pass1)!=8 or con_u==0 or con_l==0 or con_d==0 or con_s==0:
            self.lab1.config(text="Password Must contain 8 characters with atleast one upper,lower,special character and number")       
            id = 1
            self.after(id)
        else:
            self.cursor.execute("Insert Into seller(Email,Password) VALUES('"+testemail+"','"+pass1+"')")
            self.conn.commit()          
            val=self.cursor.execute("Select * from seller")
            #Uncomment below print statement line to see the sqlite3 vendortable in cmd input/output
            #print(tabulate(val.fetchall(),headers=['Id','Email','Password']))
            self.lab1.config(text="Registered Successfully")
            self.lab1.after(2000,lambda:self.lab1.config(text=""))
            self.but_3.config(text="Login",command=self.call2)    


    def after(self,id):#after() function is called to configure the label and go back to Login window
        self.lab1.after(2000,lambda:self.lab1.config(text=""))
        self.lab1.after(2000,lambda:self.ent2.delete(0,END))
        if not id:
            self.lab1.after(2000,lambda:self.ent1.delete(0,END))
            self.lab1.after(2000,lambda:self.win2.withdraw())
            self.lab1.after(2000,lambda:self.seller())       

    def call2(self):#call2 is defined to call both the functions on command in button
        self.win2.withdraw()
        self.add.add_pd()             
