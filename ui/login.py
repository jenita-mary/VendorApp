from tkinter import *
import tkinter
from .email_service import send_password


class Login:

    def __init__(self, home):
        self.home_fn = home  

    def __getattr__(self, name):
        return getattr(self.home_fn, name)
    
    def log(self):#log() function allows existing vendor to login after validation
        testemail=self.ent3.get()
        testemail=testemail.casefold()
        match1=self.cursor.execute("select Password from seller where Email ='"+testemail+"'")
        match=match1.fetchall()
        self.home_fn.mail= testemail


        id  = 0
        
        if len(match)!=1:
            self.lab2.config(text='EmailId does not Exist.Please Register')    
            self.afterlog(id) 
        elif match[0][0]!=self.ent4.get():
            self.lab2.config(text='Wrong Password,Try Again')  
            id = 1  
            self.afterlog(id)    
        else:
            val=self.cursor.execute("Select * from seller")
            #Uncomment below print statement line to see the sqlite3 vendor table in cmd input/output
            #print(tabulate(val.fetchall(),headers=['Id','Email','Password']))
            self.ent1.delete(0,END)
            self.ent2.delete(0,END)
            self.ent3.delete(0,END)
            self.ent4.delete(0,END)
            self.win2.withdraw()
            self.exist()  

    def afterlog(self,id):#after() function is called to configure the label and go back to Login window
        self.lab2.after(2000,lambda:self.lab2.config(text=""))
        self.lab2.after(2000,lambda:self.ent4.delete(0,END))
        if not id:
            self.lab2.after(2000,lambda:self.ent3.delete(0,END))
            self.lab2.after(2000,lambda:self.win2.withdraw())
            self.lab2.after(2000,lambda:self.seller())     

    def forgot(self):#forgot() sends the password in email
        testemail=self.ent3.get()
        testemail=testemail.casefold()
        match1=self.cursor.execute("select Password from seller where Email ='"+testemail+"'")
        match=match1.fetchall()
        if self.ent3.get()=='':
            self.lab2.config(text='Enter your EmailId')
            self.lab2.after(3000,lambda:self.lab2.config(text=""))
        elif len(match)!=1:
            self.lab2.config(text='EmailId does not exist')
            self.lab2.after(3000,lambda:self.lab2.config(text=""))         
        else:  
            self.lab2.config(text="check mail")
            match = self.cursor.execute("SELECT Password FROM seller WHERE Email=?",(testemail,)).fetchone()

            if match:
                send_password(testemail, match[0])

            self.lab2.after(3000,lambda:self.lab2.config(text=""))        

    def exist(self):#After login exist() function will show the options for the vendor
            self.win1.withdraw()
            self.home()
            self.frame5 = tkinter.Frame(self.win1,bg="bisque",width=1000,height=500)
            self.frame5.place(anchor='center',relx=0.5,rely=0.5)           
            self.lab_1.config(text="Hi '"+self.mail+"' !!!")
            self.but_6=tkinter.Button(self.frame5,text='Add Product',font=('ariel',20),fg='bisque',bg='black',command=self.add.add_pd)
            self.but_6.place(anchor='center',relx=0.5,rely=0.085)
            self.but_7=tkinter.Button(self.frame5,text='Edit Product',font=('ariel',20),fg='bisque',bg='black',command=self.edit.edit_pd)
            self.but_7.place(anchor='center',relx=0.5,rely=0.285)
            self.but_8=tkinter.Button(self.frame5,text='Remove Product',font=('ariel',20),fg='bisque',bg='black',command=self.remove.remove_pd)
            self.but_8.place(anchor='center',relx=0.5,rely=0.485)
            self.but_9=tkinter.Button(self.frame5,text='Sell Product',font=('ariel',20),fg='bisque',bg='black',command=self.sell.sell_pd)
            self.but_9.place(anchor='center',relx=0.5,rely=0.685)
            self.but_10=tkinter.Button(self.frame5,text='List Product',font=('ariel',20),fg='bisque',bg='black',command=self.listprod.list_pd)
            self.but_10.place(anchor='center',relx=0.5,rely=0.885)
            self.but_5=tkinter.Button(self.frame1,text='Logout',font=('ariel',15),fg='bisque',bg='black',command=self.call)
            self.but_5.place(anchor='center',x=1250,y=70)            