from tkinter import*
import mysql.connector
import tkinter
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234@567",database="signup")
mycursor=mydb.cursor()
# mycursor.execute("create database signup")

# mycursor.execute("create table detail(Name varchar(50),Email varchar(50),Gender varchar(50),Age int(3),Passwd varchar(30))")



mycursor.execute("select * from detail")
for tb in mycursor:
    print(tb)


signup = Tk()
signup.geometry('500x500')
signup.title("Registration Form")
signup.configure(bg='black')

label_0 = Label(signup, text="Registration form",width=20,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_0.place(x=150,y=0)

label_1 = Label(signup, text="FullName",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_1.place(x=0,y=40,)

entry_1 = Entry(signup,textvariable=label_1, bg="orange", fg="black", font="lucida 15")
entry_1.place(x=120,y=40)

label_2 = Label(signup, text="Email",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_2.place(x=0,y=80)

entry_2 = Entry(signup, textvariable=label_2, bg="orange", fg="black", font="lucida 15")
entry_2.place(x=120,y=80)

label_3 = Label(signup, text="Gender",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_3.place(x=0,y=120)

var = IntVar()
Radiobutton(signup, text="Male",padx = 5, variable=var, value=1).place(x=120,y=120)
Radiobutton(signup, text="Female",padx = 20, variable=var, value=2).place(x=200,y=120)

label_4 = Label(signup, text="Age:",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_4.place(x=0,y=160)

entry_3 = Entry(signup, textvariable=label_3, bg="orange", fg="black", font="lucida 15")
entry_3.place(x=120,y=160)

label_5 = Label(signup, text="Password:",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_5.place(x=0,y=200)

entry_5 = Entry(signup, textvariable=label_5, bg="orange", fg="black", font="lucida 15")
entry_5.place(x=120,y=200)

entry_1  = StringVar()
entry_2 = StringVar()
entry_3 = IntVar()
entry_4 = IntVar()
entry_5 = StringVar()

def signUP(signup):
    # message = tkinter.Frame(signup, bg='yellow')
    # message.place(x=100,y=280)
    Label(signup, text='welcome`{ Name }`User',font=("TitilliumWeb-Regular", 20),fg='black').place(x=100,y=280)

def data(label_1,label_2,label_3,label_4,label_5):
    cur = mydb.cursor()
    Name = entry_1 .get( )
    Email = entry_2.get( )
    Gender = entry_3.get( )
    Age = entry_4.get( )
    Passwd=entry_5.get()
    sql = 'insert into detail(Name,Email,Gender,Age,Passwd) values(%s,%s,%s,%s,%s)'
    values = (Name, Email, Gender, Age,Passwd)
    cur.execute(sql, values)

    cur.execute('commit')
    cur.close( )
    mydb.close( )

sign=Button(signup,width=7, height=1,text="SignUP",bg="black",fg="orange",font="lucida 15 bold",command=lambda:[signUP(signup),data(entry_1 ,entry_2,entry_3,entry_4,entry_5)])
sign.place(x=0,y=240)


def goback():
    signup.destroy( )
    import main


Button(signup, command=goback, text="Back", width=7, height=1,font=("TitilliumWeb-Regular", 20)).place(x=120,y=240)
signup.mainloop()