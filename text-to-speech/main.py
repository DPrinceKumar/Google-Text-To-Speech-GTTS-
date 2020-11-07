from tkinter import *
import platform
root = Tk()
root.geometry("450x600")
root.configure(bg='black')
root.title("Make Audio Book")
Label(root, text = "Welcome to GTTS", font=("TitilliumWeb-Regular", 20), bg ='#00ebc7', fg='#00214d').pack()
def login():
    root.destroy()
    import login
def signup():
    root.destroy( )
    import signup

log=Button(root, text = "Login", command = login,width=15,height=3,bg ='#00ebc7', fg='#00214d',)
reg=Button(root, text = "Register", command = signup ,width=15,height=3,bg ='#00ebc7', fg='#00214d')

if platform.system() == "Darwin":
    reg.configure(highlightbackground="#00ebc7", fg="#00214d")
    log.configure(highlightbackground="#00ebc7", fg="#00214d")
else:
    reg.configure(bg="#00ebc7", fg="#00214d")
    log.configure(bg="#00ebc7", fg="#00214d")

log.pack(side=LEFT)
reg.pack(side=RIGHT)
root.mainloop()