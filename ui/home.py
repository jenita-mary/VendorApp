import tkinter 
from tkinter import *
from utils.validators import Validator
from .login import Login
from .add_product import Add
from .edit_product import Edit
from .remove_product import Remove
from .list_product import ListProd
from .sell_product import Sell


class HomeWindow:
    def __init__(self, db):
        self.db = db
        self.cursor  = self.db.cursor
        self.conn  = self.db.conn
        self.mail = None
        self.validator = Validator(self)
        self.login = Login(self)
        self.add = Add(self)
        self.edit = Edit(self)
        self.remove = Remove(self)
        self.listprod  = ListProd(self)
        self.sell  = Sell(self)

    #Function home acts like a basic window and called whenever a new window has to be created  
    def home(self):  
        self.win1=Tk()
        self.tit=self.win1.title('www.ShopKART.com')
        self.win1.configure(bg='bisque')
        self.win1.geometry('2000x1000')
        self.frame1 = tkinter.Frame(self.win1,bg="black",width=2000,height=100)
        self.frame1.place(x=0,y=0)
        self.lab_1=tkinter.Label(self.frame1,text='Welcome to shopKART',bg='black',fg='white',font=('times',25))
        self.lab_1.place(anchor='center',x=700,y=50)


    #Function content is used to place content and button in the homepage   
    def content(self):    
        self.lab_2=tkinter.Label(self.win1,text='ShopKART is a leading market place',bg='bisque',font=('times',20))
        self.lab_2.place(anchor='center',x=700,y=300)
        self.lab_3=tkinter.Label(self.win1,text='A happy place for vendors and customers',bg='bisque',font=('times',15))
        self.lab_3.place(anchor='center',x=700,y=400)     
        self.but_1=tkinter.Button(self.win1,text='Vendor Login',font=('ariel',15),fg='bisque',bg='black',command=self.seller)
        self.but_1.place(anchor='center',x=700,y=500)
        self.win1.mainloop()     

    def seller(self):#seller function-Register and Login for vendors
        self.win1.withdraw()
        self.win2=Tk()
        self.win2.title('www.ShopKART.com/vendor/')
        self.win2.configure(bg='bisque')
        self.win2.geometry('2000x1000')
        self.frame2 = tkinter.Frame(self.win2,bg="black",width=2000,height=100)
        self.frame2.place(x=0,y=0)
        self.lab_2=tkinter.Label(self.frame2,text='Welcome to shopKART Vendor',bg='black',fg='white',font=('times',25))
        self.lab_2.place(anchor='center',x=700,y=50)
        self.frame3 = tkinter.Frame(self.win2,bg="black",width=500,height=500)
        self.frame3.place(relx=0.1,rely=0.2)
        self.frame4 = tkinter.Frame(self.win2,bg="black",width=500,height=500)
        self.frame4.place(relx=0.55,rely=0.2)     
        tkinter.Label(self.frame3,text='Emailid:',font=('ariel',15),width=15,bg='black',fg='white').place(anchor='ne',relx=0.4,rely=0.3)
        self.ent1=tkinter.Entry(self.frame3,bd=4,font=('ariel',15),width=20)
        self.ent1.place(anchor='nw',relx=0.4,rely=0.3)
        tkinter.Label(self.frame3,text='Password:',font=('ariel',15),width=15,bg='black',fg='white').place(anchor='ne',relx=0.4,rely=0.4)
        self.ent2=tkinter.Entry(self.frame3,bd=4,font=('ariel',15),width=20,show='*')
        self.ent2.place(anchor='nw',relx=0.4,rely=0.4)
        self.lab1=tkinter.Label(self.frame3,text='',font=('ariel',10),bg='black',fg='white')
        self.lab1.place(anchor='center',relx=0.5,rely=0.7)
        tkinter.Label(self.frame4,text='Emailid:',font=('ariel',15),width=15,bg='black',fg='white').place(anchor='ne',relx=0.4,rely=0.3)
        self.ent3=tkinter.Entry(self.frame4,bd=4,font=('ariel',15),width=20)
        self.ent3.place(anchor='nw',relx=0.4,rely=0.3)
        tkinter.Label(self.frame4,text='Password:',font=('ariel',15),width=15,bg='black',fg='white').place(anchor='ne',relx=0.4,rely=0.4)
        self.ent4=tkinter.Entry(self.frame4,bd=4,font=('ariel',15),width=20,show='*')
        self.ent4.place(anchor='nw',relx=0.4,rely=0.4)
        self.lab2=tkinter.Label(self.frame4,text='',font=('ariel',10),bg='black',fg='white')
        self.lab2.place(anchor='center',relx=0.5,rely=0.8)  
        self.label_1=tkinter.Label(self.frame3,text='New Vendor',font=('ariel',20),fg='white',bg='black')
        self.label_1.place(anchor='center',relx=0.5,rely=0.2)
        self.label_2=tkinter.Label(self.frame4,text='Existing Vendor',font=('ariel',20),fg='white',bg='black')
        self.label_2.place(anchor='center',relx=0.5,rely=0.2)
        self.but_3=tkinter.Button(self.frame3,text='Register',font=('ariel',15),fg='black',bg='bisque',command=self.validator.verify)
        self.but_3.place(anchor='center',relx=0.5,rely=0.6)
        self.but_4=tkinter.Button(self.frame4,text='Login',font=('ariel',15),fg='black',bg='bisque',command=self.login.log)    
        self.but_4.place(anchor='center',relx=0.5,rely=0.6)
        self.but_new=tkinter.Button(self.frame4,text='Forgot Password',font=('ariel',15),fg='bisque',bg='black',relief='flat',command=self.login.forgot)    
        self.but_new.place(anchor='center',relx=0.5,rely=0.7)     
        self.win2.mainloop()       

    def call(self):#call is defined to call both the functions on command in button
        self.win1.withdraw()
        self.home()
        self.content()
        self.__init__(self.db)

    def call1(self):#call1 is defined to call both the functions on command in button
        self.win1.withdraw()
        self.login.exist()

