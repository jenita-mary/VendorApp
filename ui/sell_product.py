from tkinter import *
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb
from tkinter.ttk import *
from tabulate import tabulate

class Sell:

    def __init__(self, home):
        self.home_fn = home  

    def __getattr__(self, name):
        return getattr(self.home_fn, name)  
        
    def sell_pd(self):#This function is called when the vendor clicks on sell products
        self.win1.withdraw()
        tab=self.cursor.execute("select Id from seller where Email ='"+self.mail+"'")
        tab1=tab.fetchall()
        self.id1=tab1[0][0]
        tab2=self.cursor.execute("select ProductName from product where SellerId =?",(self.id1,))
        tab3=tab2.fetchall()
        list1=list(tab3)
        self.list2=[]
        for i in list1:
            self.list2.append(i[0])
     
        if len(tab3)>0:
            self.home()
            self.lab_1.config(text="Hi '"+self.mail+"' !!! You can sell you products  here")
            self.label_12=tkinter.Label(self.win1,text='Product Name:',font=('ariel',20),fg='black',bg='bisque')
            self.label_12.place(anchor='center',relx=0.4,rely=0.2)
            self.label_13=tkinter.Label(self.win1,text='Quantity:',font=('ariel',20),fg='black',bg='bisque')
            self.label_13.place(anchor='center',relx=0.4,rely=0.3)      
            self.ent5=Combobox(self.win1,font=('ariel',15),width=20,values=self.list2)
            self.ent5.place(anchor='center',relx=0.6,rely=0.2)      
            self.ent6=Combobox(self.win1,font=('ariel',15),width=20,values=(0,))
            self.ent6.place(anchor='center',relx=0.6,rely=0.3)

            self.but_15=tkinter.Button(self.win1,text='Refer',font=('ariel',15),fg='bisque',bg='black',command=self.refer_sell)
            self.but_15.place(anchor='center',relx=0.8,rely=0.2) 
            self.but_17=tkinter.Button(self.win1,text='Sell',font=('ariel',15),fg='bisque',bg='black',command=self.onsell)
            self.but_17.place(anchor='center',relx=0.5,rely=0.8)
            self.but_18=tkinter.Button(self.win1,text='<--Back',font=('ariel',15),fg='bisque',bg='black',command=self.call1)
            self.but_18.place(anchor='center',relx=0.6,rely=0.8)
            self.lab_spc=tkinter.Label(self.win1,text='',font=('ariel',15),bg='bisque',fg='black')
            self.lab_spc.place(anchor='center',relx=0.5,rely=0.9)      
        else:
            self.add.add_pd()  

    def refer_sell(self):#Generates reference for vendor to sell
        calc=self.cursor.execute("select Quantity from product where ProductName=? and SellerId=?",(self.ent5.get(),self.id1,))
        rep=calc.fetchall()
        self.quan=int(rep[0][0])
        self.ent6.config(values=list(range(1,self.quan+1)))

    def onsell(self):
        if self.ent5.get() not in self.list2:
            self.lab_spc.config(text="ProductName is invalid")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=''))
        elif int(self.ent6.get()) not in list(range(1,self.quan+1)):
            self.lab_spc.config(text="Quantity is not in range")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=''))
        else:
            quantity=(self.quan)-(int(self.ent6.get()))
            quantity=str(quantity)
            self.cursor.execute("Update product set Quantity=? where SellerId = ? and ProductName= ?",(quantity,self.id1,self.ent5.get(),))
            self.conn.commit()
            val=self.cursor.execute("Select * from product where SellerId =?",(self.id1,))
            rows=val.fetchall()
            #Uncomment below print statement for verification of Products table in cmd input/output
            #print(tabulate(rows,headers=['Id','ProductName','Price','Quantity','Descriptions'],tablefmt='grid'))
            calc=self.cursor.execute("select Price from product where ProductName=? and SellerId=?",(self.ent5.get(),self.id1,))
            rep=calc.fetchall()
            price=int(rep[0][0])
            tot=price*int(self.ent6.get())
            tot=str(tot)
            mb.showinfo('message','You have sold product for Rs."'+tot+'"')    
            if int(quantity)<5:
                mb.showwarning('Quantity Updated','Quantity is less than 5,Update quantity')
            else:
                mb.showinfo('message','Process completed')
            self.login.exist()   
