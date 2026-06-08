from tkinter import *
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb
from tkinter.ttk import *
from tabulate import tabulate

class Remove:

    def __init__(self, home):
        self.home_fn = home  

    def __getattr__(self, name):
        return getattr(self.home_fn, name)  
    
    def remove_pd(self):#This function is called when the vendor clicks on remove products
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
            self.lab_1.config(text="Hi '"+self.mail+"' !!! You can remove products here")
            self.label_11=tkinter.Label(self.win1,text='Product Name:',font=('ariel',20),fg='black',bg='bisque')
            self.label_11.place(anchor='center',relx=0.4,rely=0.5)
            
            self.ent5=Combobox(self.win1,font=('ariel',15),width=20,values=self.list2)
            self.ent5.place(anchor='center',relx=0.6,rely=0.5)

            self.but_15=tkinter.Button(self.win1,text='Remove',font=('ariel',15),fg='bisque',bg='black',command=self.get1)
            self.but_15.place(anchor='center',relx=0.5,rely=0.8)
            self.but_16=tkinter.Button(self.win1,text='<--Back',font=('ariel',15),fg='bisque',bg='black',command=self.call1)
            self.but_16.place(anchor='center',relx=0.6,rely=0.8)
            self.lab_spc=tkinter.Label(self.win1,text='',font=('ariel',15),bg='bisque',fg='black')
            self.lab_spc.place(anchor='center',relx=0.5,rely=0.9)
        else:
            self.add.add_pd()

    def get1(self):#Function verifies the content for removal and remove in table after verification
        if self.ent5.get()!=0 and self.ent5.get() in self.list2:
          var_1=mb.askyesno('Confirmation','Click "yes" to confirm removal of product',default='no')
          if var_1==True:
              self.cursor.execute("Delete from product where SellerId =? and ProductName=?",(self.id1,self.ent5.get()))
              self.conn.commit()
              val=self.cursor.execute("Select * from product")
              print(tabulate(val.fetchall(),headers=['Id','ProductName','Price','Quantity','Descriptions'],tablefmt='grid'))
              mb.showinfo('message','Process completed')
              self.login.exist()
          elif var_1==False:
              self.remove_pd()
            
        else:
          self.lab_spc.config(text="Fields doesn't match your products")
          self.lab_spc.after(3000,lambda:self.lab_spc.config(text=""))           