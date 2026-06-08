from tkinter import *
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb
from tkinter.ttk import *

class Edit:

    def __init__(self, home):
        self.home_fn = home  

    def __getattr__(self, name):
        return getattr(self.home_fn, name)
        
    def edit_pd(self):#This function is called when the vendor clicks on edit products
        self.win1.withdraw()
        tab=self.cursor.execute("select Id from seller where Email ='"+self.mail+"'")
        tab1=tab.fetchall()
        self.id1=tab1[0][0]
        
        tab2=self.cursor.execute("select ProductName from product where SellerId =?",(self.id1,))
        tab3=tab2.fetchall()
        list1=list(tab3)
        list2=[]
        for i in list1:
            list2.append(i[0])
        if len(tab3)>0:
            self.home()
            self.lab_1.config(text="Hi '"+self.mail+"' !!! You can edit products here")
            self.label_7=tkinter.Label(self.win1,text='Product Name:',font=('ariel',20),fg='black',bg='bisque')
            self.label_7.place(anchor='center',relx=0.4,rely=0.2)
            self.label_8=tkinter.Label(self.win1,text='Quantity:',font=('ariel',20),fg='black',bg='bisque')
            self.label_8.place(anchor='center',relx=0.4,rely=0.3)
            self.label_9=tkinter.Label(self.win1,text='Price:',font=('ariel',20),fg='black',bg='bisque')
            self.label_9.place(anchor='center',relx=0.4,rely=0.4)
            self.label_10=tkinter.Label(self.win1,text='Details:',font=('ariel',20),fg='black',bg='bisque')
            self.label_10.place(anchor='n',relx=0.4,rely=0.5)
            
            self.ent5=Combobox(self.win1,font=('ariel',15),width=20,values=list2)
            self.ent5.place(anchor='center',relx=0.6,rely=0.2)
            self.ent6=tkinter.Entry(self.win1,bd=4,font=('ariel',15),width=20)
            self.ent6.place(anchor='center',relx=0.6,rely=0.3)

            self.ent7=tkinter.Entry(self.win1,bd=4,font=('ariel',15),width=20)
            self.ent7.place(anchor='center',relx=0.6,rely=0.4)

            self.ent8=ScrolledText(self.win1,bd=4,font=('ariel',15),width=30,height=5)
            self.ent8.place(anchor='n',relx=0.6,rely=0.5)
            self.entry1=self.ent6.get()
            self.entry2=self.ent7.get()
            self.entry3=self.ent8.get('1.0', 'end-1c')

            self.but_15=tkinter.Button(self.win1,text='Refer',font=('ariel',15),fg='bisque',bg='black',command=self.refer)
            self.but_15.place(anchor='center',relx=0.8,rely=0.2)  

            self.but_13=tkinter.Button(self.win1,text='Edit',font=('ariel',15),fg='bisque',bg='black',command=self.edit_check)
            self.but_13.place(anchor='center',relx=0.5,rely=0.8)
            self.but_14=tkinter.Button(self.win1,text='<--Back',font=('ariel',15),fg='bisque',bg='black',command=self.call1)
            self.but_14.place(anchor='center',relx=0.6,rely=0.8)
            
            self.lab_spc=tkinter.Label(self.win1,text='',font=('ariel',15),bg='bisque',fg='black')
            self.lab_spc.place(anchor='center',relx=0.5,rely=0.9)
        else:
            self.add.add_pd()

    def edit_check(self):#verify the edited content by vendor and updates the content in table
        name=self.ent5.get()
        quant=self.ent6.get()
        price=self.ent7.get()
        desc=self.ent8.get('1.0', 'end-1c')        

        if name=="" or quant=="" or price=="" or desc=="":
            self.lab_spc.config(text="Fields can not be empty")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))
        elif quant.isdigit()==False or int(quant)>9999:
            self.lab_spc.config(text="Quantity Field will accept only numbers within 9999")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))
        elif price.isdigit()==False:
            self.lab_spc.config(text="Price Field will accept only numbers")
            self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))
        else:
            self.cursor.execute("Update product set (ProductName,Price,Quantity,Descriptions) = (?,?,?,?) where SellerId = ? and ProductName= ?",(name,price,quant,desc,self.id1,self.name,))
            self.conn.commit()
            val=self.cursor.execute("Select * from product")
            #print(tabulate(val.fetchall(),headers=['Id','ProductName','Price','Quantity','Descriptions'],tablefmt='grid'))
            mb.showinfo('message','Process completed')
            self.win1.withdraw()
            self.login.exist()
                
    def refer(self):#on click after selection of product name gives reference for the vendor for remaining entries
        if (self.entry1!=None and self.entry2!=None and self.entry3!=None):
            self.ent6.delete(0,END)
            self.ent7.delete(0,END)
            self.ent8.delete('1.0', tkinter.END)
        repetition=self.cursor.execute("select ProductName,Price,Quantity,Descriptions from product where ProductName=? and SellerId=?",(self.ent5.get(),self.id1,))
        rep=repetition.fetchall()
        rep=list(rep[0])
        self.name=rep[0]
        self.ent6.insert(0,rep[2])
        self.ent7.insert(0,rep[1])
        self.ent8.insert(tkinter.INSERT,rep[3])        