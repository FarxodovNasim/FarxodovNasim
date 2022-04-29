import smtplib
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import ANCHOR




class SampleAPP(tk.Tk):
    def __init__(self, *args, **kwargs,):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,ListPage,Window,userPage,Page1,Page2,Page3,Page4):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#ccccb3",)
        self.controller = controller
        self.controller.title("Meros Pharm")
        self.controller.state("normal")
        
        
# Login Parol qism

        headingLabel1 = tk.Label(self, text="Welcome to Meros Pharm", font=("Calibri (Основной текст)", 40, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        my_login1 ="lolo"
        my_login="nasim"
        my_login2 ="samo"
        login_label = tk.Label(self, text="Login kiriting", font=("Calibri (Основной текст)", 15, "bold"), bg="#ccccb3")
        login_label.pack(pady=10)

        login_entry = tk.Entry(self, textvariable=my_login, font=("Calibri (Основной текст)", 15, "bold"))
        login_entry.pack()

        password_label=tk.Label(self,text="Parol kiriting",font = ("Calibri (Основной текст)", 15, "bold"),bg="#ccccb3")
        password_label.pack()

        my_password2="0000"
        my_password1="pepe"
        my_password="2121"
        password_entry=tk.Entry(self,textvariable=my_password,font = ("Calibri (Основной текст)", 15, "bold"))
        password_entry.pack()
        def check_password():
            if password_entry.get()== my_password and login_entry.get()==my_login:
                controller.show_frame("ListPage")

            if password_entry.get()== my_password1 and login_entry.get()==my_login1:
                controller.show_frame("Window")
            
            if password_entry.get()== my_password2 and login_entry.get()==my_login2:
                controller.show_frame("userPage")


            else:
                wrong_password_label.config(text="Login yoki Parol xato")


    
# Kirish knopka
        input_button=tk.Button(self,text="Kirish",font = ("Calibri (Основной текст)", 12, "bold"), bg = "#ffffff",command=check_password)
        input_button.pack(pady=18)
        wrong_password_label=tk.Label(self,text="",font = ("Calibri (Основной текст)", 15, "bold"),bg="#ccccb3")
        wrong_password_label.pack()

# Zakaz oynasi
class ListPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ccccb3")
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Mahsulotlarni buyurtma qilish", font=("Times New Roman", 30, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("StartPage")
            
        return_button = tk.Button(self,text="Orqaga",font = ("Times New Roman", 15, "bold"), bg = "#b3b3b3",command=page_return)
        return_button.place(x=1200, y=600)





        listbox = Listbox(self,x=100,y=200,width=80,height=20,selectmode=MULTIPLE)
        listbox.place(x=100,y=100)

        listbox1 = Listbox(self,x=100,y=200,width=80,height=20,selectmode=MULTIPLE)
        listbox1.place(x=750,y=100)
        

        def delete():
            selection = listbox_listbox.curselection()

            listbox_listbox.delete(selection[0])

        def add():
            new_listbox = listbox_entry.get()
            listbox_listbox.insert(0, new_listbox)
        listbox_entry = tk.Entry(self,width=10)
        listbox_entry.place(x=500,y=530, width=400, height=25)
        
        add_button = Button(self,text="Qo'shish", command=add).place(x=500,y=570, width=400, height=25)
        listbox_listbox = tk.Listbox(self,selectmode=MULTIPLE)
        listbox_listbox.place(x=500,y=630, width=400, height=50,)
        listbox_listbox.insert(END, "Trimol")
       

        delete_button = tk.Button(self,text="O'chirish", command=delete).place(x=500,y=600, width=400, height=25,)



#Listbox, < Dorilar bo'limi > bo'limi
 


        

        

        
        for i in ["Spirt","Yod","Bint","Giliserin","Vitamin","Parasetamol","Ampisilin","Makropen","Koraksan","Kagosel","Vazooket","Pirasetam","Lorista""Spirt","Yod","Bint","Giliserin","Vitamin","Parasetamol","Ampisilin","Makropen","Koraksan","Kagosel","Vazooket","Pirasetam","Lorista""Spirt","Yod","Bint","","Vitamin","Parasetamol","Ampisilin","Makropen","Koraksan","Kagosel","Vazooket","Pirasetam","Lorista"]:


            listbox.insert(END," " +i+ " ")
            



        def moveTo(listbox,listbox1):
            indexList = listbox.curselection()
            if indexList:
                    index = indexList[0]
                    val=listbox.get(index)
                    listbox.delete(index)
                    listbox1.insert(END,val)

                   

        

        return_button5= tk.Button(self,text=" > ",font = ("Times New Roman", 15, "bold"), bg = "#b3b3b3",command= lambda: moveTo(listbox,listbox1))
        return_button5.place(x=650, y=200)

        return_button6 = tk.Button(self,text=" < ",font = ("Times New Roman", 15, "bold"), bg = "#b3b3b3",command= lambda: moveTo(listbox1,listbox))
        return_button6.place(x=650, y=250)











# Hisoblash Oynasi

class Window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ccccb3")
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Dorilar buyurtma berish bo'limiga xush kelibsiz", font=("Times New Roman", 30, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("StartPage")
        return_button = tk.Button(self,text="back",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=page_return)
        return_button.place(x=1200, y=630)

        def button1():
            controller.show_frame("Page1")
        return_button = tk.Button(self,text="Активный",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=button1)
        return_button.place(x=1100, y=455,width=150,height=30)
        def button2():
            controller.show_frame("Page2")
        return_button = tk.Button(self,text="Черновик",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=button2)
        return_button.place(x=1100, y=500,width=150,height=30)
        def button3():
            controller.show_frame("Page3")
        return_button = tk.Button(self,text="Cборка",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=button3)
        return_button.place(x=1100, y=545,width=150,height=30)
        def button4():
            controller.show_frame("Page4")
        return_button = tk.Button(self,text="B доставке",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=button4)
        return_button.place(x=1100, y=590,width=150,height=30)











        listbox = Listbox(self,x=100,y=200,width=80,height=20,selectmode=MULTIPLE)
        listbox.place(x=100,y=100)

        listbox1 = Listbox(self,x=100,y=200,width=80,height=20,selectmode=MULTIPLE)
        listbox1.place(x=750,y=100)



        for i in [str(123),str(200),"Bint 200","Giliserin","Vitamin","Parasetamol"]:


            listbox.insert(END," " +i+ " ")
            



        def moveTo(listbox,listbox1):
            indexList = listbox.curselection()
            if indexList:
                    index = indexList[0]
                    val=listbox.get(index)
                    listbox.delete(index)
                    listbox1.insert(END,val)


        

        return_button5= tk.Button(self,text=" > ",font = ("Times New Roman", 15, "bold"), bg = "#b3b3b3",command= lambda: moveTo(listbox,listbox1))
        return_button5.place(x=650, y=200)

        return_button6 = tk.Button(self,text=" < ",font = ("Times New Roman", 15, "bold"), bg = "#b3b3b3",command= lambda: moveTo(listbox1,listbox))
        return_button6.place(x=650, y=250)


        



class userPage(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent, bg="#ccccb3")
        self.controller = controller
        headingLabel1 = tk.Label(self, text="kalkulyator", font=("Times New Roman", 30, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("StartPage")
        return_button = tk.Button(self,text="back",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=page_return)
        return_button.place(x=1200, y=600)





#knopka oknolar

class Page1(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent, bg="#ccccb3")
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Mahsulot jarayoni ", font=("Times New Roman", 30, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("Window")
        return_button = tk.Button(self,text="back",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=page_return)
        return_button.place(x=1200, y=600)


class Page2(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent, bg="#ccccb3")
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Qoralama", font=("Times New Roman", 30, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("Window")
        return_button = tk.Button(self,text="back",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=page_return)
        return_button.place(x=1200, y=600)



class Page3(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent, bg="#ccccb3")
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Mahsulotlar holati", font=("Times New Roman", 30, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("Window")
        return_button = tk.Button(self,text="back",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=page_return)
        return_button.place(x=1200, y=600)



class Page4(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent, bg="#ccccb3")
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Yetkazib berish bo'limi", font=("Times New Roman", 30, "bold"), bg="#ccccb3")
        headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("Window")
        return_button = tk.Button(self,text="back",font = ("Times New Roman", 15, "bold"), bg = "#ccccb3",command=page_return)
        return_button.place(x=1200, y=600)








if __name__ == "__main__":
    app = SampleAPP()
    app.mainloop()