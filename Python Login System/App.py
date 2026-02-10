from tkinter import *
import Database
root = Tk()


root.geometry("600x400")
root.title('My IG Login')

sUserName = StringVar()
sPassword = StringVar()


def Login():
    username = sUserName.get()
    password = sPassword.get()

    
    if Database.login(username,password):
        print('Login Successful')
    else:
        print('Incorrect Username and Password')
    


lblHeading = Label(root,text='My IG Login',font=('footlight mt light',24),bg='hot pink')
lblHeading.place(x=230,y=50)

lblValue1 = Label(root,text='User Name   ',bg='lavender')
lblValue1.place(x=150,y=190)

txtValue1 = Entry(root,textvariable = sUserName)
txtValue1.place(x=250,y=190)


lblValue2 = Label(root,text='Password  ',bg='lavender')
lblValue2.place(x=150,y=230)
txtValue2 = Entry(root,textvariable = sPassword,show='*')
txtValue2.place(x=250,y=230)

btnAdd = Button(root,text='  Login  ',command = Login,bg='skyblue')
btnAdd.place(x=250,y=270)

root.mainloop()
