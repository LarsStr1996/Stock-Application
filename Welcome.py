from tkinter import *
from runner import *

from personal_wallet import Personal_wallet
from live_plot import plots
from message_screen import log
import os
from create_wallet import Create_wallet


class Welcome(object):
       screen = Tk()
       def delete_10():
              self.screen10.destroy()
              log.log_list.append('Return to previous screen')
              print(log.log_list)
       def delete2():
              self.screen3.destroy()
       def delete3():
              self.screen4.destroy()
       def delete4():
              self.screen5.destroy()
   
       def access_system(self):
              self.screen6 = Toplevel(self.screen)
              self.screen6.title("Succes")
              self.screen6.geometry("300x300")
              Label(self.screen6,text="Welcome to your Wallet").pack()
              Buttons.button_access_system(self.screen6)
              
       def login_succes(self):
              self.screen3 = Toplevel(self.screen)
              self.screen3.title("Succes")
              self.screen3.geometry("300x250")
              self.screen3.configure(bg='dimgray')
              Label(self.screen3,text="Login succes").pack()
              Button(self.screen3,text='Quit', command = Welcome.delete2).pack()
              button_access = Button(self.screen3,text='Access System', command = Welcome().access_system)
              button_access.pack()
              
       def password_not_recognised(self):
              self.screen4 = Toplevel(self.screen)
              self.screen4.title("Succes")
              self.screen4.geometry("150x100")
              Label(self.screen4,text="Password Error").pack()
              Button(self.screen4,text='OK', command = Welcome.delete3).pack()

       def user_not_found(self):
              self.screen5 = Toplevel(self.screen)
              self.screen5.title("Succes")
              self.screen5.geometry("150x100")
              Label(self.screen5,text="User Not Found").pack()
              Button(self.screen5,text='OK', command = Welcome.delete4).pack()
              
       def register_user(self):
              username_info = username.get()
              password_info = password.get()

              file = open(username_info,"w")
              file.write(username_info+"\n")
              file.write(password_info)
              file.close()

              username_entry.delete(0, END)
              password_entry.delete(0, END)

              Label(screen1,text="",bg = 'dimgray').pack()
              Label(screen1,bg = 'dimgray', text = "Registration Succesful",height="1",fg = "white",font=("calibri",11)).pack()

       def login_verify():
              username1 = username_verify.get()
              password1 = password_verify.get()
              username_entry1.delete(0,END)
              password_entry1.delete(0,END)
              
              list_of_files = os.listdir()
              if username1 in list_of_files:
                     file1 = open(username1,"r")
                     verify = file1.read().splitlines()
                     if password1 in verify:
                            Welcome().login_succes()
                     else:
                            Welcome().password_not_recognised()
              else:
                     Welcome().user_not_found()
                     
       def register(self):
              self.screen1 = Toplevel(self.screen)
              self.screen1.title("Register")
              self.screen1.geometry("300x250")
              self.screen1.configure(bg='dimgray')
              
              global username
              global password
              global username_entry
              global password_entry
              username = StringVar()
              password = StringVar()

              Label(self.screen1,text="Please enter details below",bg = 'gold',width="300",height="2",font = ("Calibri",13)).pack()
              Label(self.screen1,text="",bg = 'dimgray').pack()
              Label(self.screen1,text="Username * ",bg = 'dimgray',width="300",fg='white').pack()
              username_entry = Entry(self.screen1,textvariable = username)
              username_entry.pack()
              Label(self.screen1,text="Password * ",bg = 'dimgray',width="300",fg='white').pack()
              password_entry = Entry(self.screen1,textvariable = password)
              password_entry.pack()
              Label(screen1,text="",bg = 'dimgray').pack()
              Button(self.screen1, text="Register",width = 10,height = 1,command = Welcome().register_user).pack()              
        
       def login(self):
              self.screen2 = Toplevel(self.screen)
              self.screen2.title("login")
              self.screen2.geometry("300x250")
              self.screen2.configure(bg='dimgray')
              Label(self.screen2,text="Please enter details below",bg = 'gold',width="300",height="2",font = ("Calibri",13)).pack()
              Label(self.screen2,text="",bg = 'dimgray',height="1").pack()

              global username_verify
              global password_verify

              username_verify = StringVar()
              password_verify = StringVar()

              global username_entry1
              global password_entry1
              
              Label(self.screen2,text="Username * ",bg = 'dimgray',width="300",fg='white').pack()
              username_entry1 = Entry(self.screen2,textvariable = username_verify,bg = 'white',width=10)
              username_entry1.pack()
              Label(self.screen2,text="",bg = 'dimgray',width="300",height="1").pack()
              Label(self.screen2,text="Password * ",bg = 'dimgray',width="300",fg='white').pack()
              password_entry1 = Entry(self.screen2,textvariable = password_verify,bg = 'white',width=10)
              password_entry1.pack()
              Label(self.screen2,text="",bg = 'dimgray',width="300").pack()
              Button(self.screen2, text = "Login",bg = 'white',width = 10,height=1,command = Welcome.login_verify).pack()

       def main_screen(self):
              self.screen = self.screen
              self.screen.geometry("300x200")
              self.screen.configure(bg='dimgray')
              self.screen.title("Stock Wallet")
              Label(text="Stock Wallet",bg="gold",width = "300",height = "2",font = ("Calibri",13)).pack()
              Label(text="",bg='dimgray').pack()
              Button(text = "Login",bg = 'white',height="2",width="30",command = Welcome().login).pack()
              Label(text="",bg='dimgray').pack()
              Button(text = "Register",bg = 'white',height="2",width="30",command = Welcome().register).pack()
              self.screen.mainloop()
Welcome().main_screen()


