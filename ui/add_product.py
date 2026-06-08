from tkinter import *
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb

class Add:

    def __init__(self, home):
        self.home_fn = home  

    def __getattr__(self, name):
        return getattr(self.home_fn, name)

    def add_pd(self):#This function is called when the vendor clicks on add products
        self.win1.withdraw()
        self.home()
        self.lab_1.config(text="Hi '"+self.mail+"' !!! You can add products here")
        self.label_3=tkinter.Label(self.win1,text='Product Name:',font=('ariel',20),fg='black',bg='bisque')
        self.label_3.place(anchor='center',relx=0.4,rely=0.2)
        self.label_4=tkinter.Label(self.win1,text='Quantity:',font=('ariel',20),fg='black',bg='bisque')
        self.label_4.place(anchor='center',relx=0.4,rely=0.3)
        self.label_5=tkinter.Label(self.win1,text='Price:',font=('ariel',20),fg='black',bg='bisque')
        self.label_5.place(anchor='center',relx=0.4,rely=0.4)
        self.label_6=tkinter.Label(self.win1,text='Details:',font=('ariel',20),fg='black',bg='bisque')
        self.label_6.place(anchor='n',relx=0.4,rely=0.5)
        self.ent5=tkinter.Entry(self.win1,bd=4,font=('ariel',15),width=20)
        self.ent5.place(anchor='center',relx=0.6,rely=0.2)
        self.ent6=tkinter.Entry(self.win1,bd=4,font=('ariel',15),width=20)
        self.ent6.place(anchor='center',relx=0.6,rely=0.3)
        self.ent7=tkinter.Entry(self.win1,bd=4,font=('ariel',15),width=20)
        self.ent7.place(anchor='center',relx=0.6,rely=0.4)
        self.ent8=ScrolledText(self.win1,bd=4,font=('ariel',15),width=30,height=5)
        self.ent8.place(anchor='n',relx=0.6,rely=0.5)
 
        self.but_11=tkinter.Button(self.win1,text='ADD',font=('ariel',15),fg='bisque',bg='black',command=self.add_check)
        self.but_11.place(anchor='center',relx=0.5,rely=0.8)
        self.but_12=tkinter.Button(self.win1,text='<--Back',font=('ariel',15),fg='bisque',bg='black',command=self.call1)
        self.but_12.place(anchor='center',relx=0.6,rely=0.8)
        self.lab_spc=tkinter.Label(self.win1,text='',font=('ariel',15),bg='bisque',fg='black')
        self.lab_spc.place(anchor='center',relx=0.5,rely=0.9)  

    def add_check(self):#Verification of the added products and insertion to the table 
        name=(self.ent5.get().replace(" ","")).lower()
        quant=self.ent6.get()
        price=self.ent7.get()
        desc=self.ent8.get('1.0', 'end-1c')
        tab=self.cursor.execute("select Id from seller where Email ='"+self.mail+"'")
        tab1=tab.fetchall()
        id1=tab1[0][0]
        repetition=self.cursor.execute("select * from product where ProductName=? and SellerId=?",(name,id1,))
        rep=repetition.fetchall()
        
        if len(rep)>0:
            self.lab_spc.config(text="Product Name already exists in your Id,Can't add product with same name")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))
        elif name=="" or quant=="" or price=="" or desc=="":
            self.lab_spc.config(text="Fields can not be empty")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))
        elif quant.isdigit()==False or int(quant)>9999:
            self.lab_spc.config(text="Quantity Field will accept only numbers within 9999")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))
        elif price.isdigit()==False:
            self.lab_spc.config(text="Price Field will accept only numbers")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))
        else:
            self.cursor.execute("Insert Into product values(?,?,?,?,?)",(id1,name,price,quant,desc,))
            self.conn.commit()
            val=self.cursor.execute("Select * from product")
            #Uncomment below line to see the sqlite3 product table in cmd input/output
            #print(tabulate(val.fetchall(),headers=['Id','ProductName','Price','Quantity','Descriptions'],tablefmt='grid'))
            mb.showinfo('message','Process completed')
            self.win1.withdraw()
            self.login.exist()          