from tkinter import *
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb
from tkinter.ttk import *
from tabulate import tabulate

class ListProd:

    def __init__(self, home):
        self.home_fn = home  

    def __getattr__(self, name):
        return getattr(self.home_fn, name)  
        
    def list_pd(self):#This function is called when the vendor clicks on list products
        self.win1.withdraw()
        tab=self.cursor.execute("select Id from seller where Email ='"+self.mail+"'")
        tab1=tab.fetchall()
        id1=tab1[0][0]
        
        tab2=self.cursor.execute("select ProductName from product where SellerId =?",(id1,))
        tab3=tab2.fetchall()
        list2=[]
        for i in tab3:
            list2.append(i[0])
        list3=[]
        for j in list2:
            tab4=self.cursor.execute("select Price from product where ProductName LIKE ('%'||?||'%')",(j,))
            tab5=tab4.fetchall()
            emp=[]
            for k in tab5:
                emp.append(int(k[0]))
            list3.append(sum(emp)//len(emp))  

        if len(tab3)>0:
            self.home()
            self.lab_1.config(text="Hi '"+self.mail+"' !!! Your Product List is here")      
            val=self.cursor.execute("Select ProductName,Price,Quantity,Descriptions from product where SellerId =?",(id1,))
            rows=val.fetchall()
            style = Style(self.win1)
            style.theme_use("clam")
            style.configure("Treeview", background="black", 
                        fieldbackground="black", foreground="bisque")
            #Uncomment below print statement for verification of Products table in cmd input/output
            #print(tabulate(val.fetchall(),headers=['Id','ProductName','Price','Quantity','Descriptions'],tablefmt='grid'))
            tree=Treeview(self.win1,column=('ProductName','Price','Quantity','Descriptions','Average Market Price'),show='headings')

            tree.column("#1", anchor=tkinter.CENTER)
            tree.heading("#1", text="ProductName")
            tree.column("#2", anchor=tkinter.CENTER)
            tree.heading("#2", text="Price")
            tree.column("#3", anchor=tkinter.CENTER)
            tree.heading("#3", text="Quantity")
            tree.column("#4", anchor=tkinter.CENTER)
            tree.heading("#4", text="Descriptions")
            tree.column("#5", anchor=tkinter.CENTER)
            tree.heading("#5", text="Average Market Price")      
            tree.place(anchor='center',relx=0.5,rely=0.3)
            
            for i,j in zip(rows,list3): 
                row=[]
                row.extend(i)
                row.append(j)
                tree.insert("", tkinter.END, values=row)      
            self.but_17=tkinter.Button(self.win1,text='<--Back',font=('ariel',15),fg='bisque',bg='black',command=self.call1)
            self.but_17.place(anchor='center',relx=0.6,rely=0.8)

        else:
            self.add.add_pd()