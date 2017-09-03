#Registration page and Login page
import os
from tkinter import *
from urllib.request import urlopen
import tkinter.messagebox as tm
# import sqlite3
# FileName = "RegistrationData.db"
Counter = 0
def CallRegistrationPage():
	root.destroy()
	Register()
def CallLoginPage():
	root.destroy()
	Login()
def Register():
	def ClickRegisterButton():
		global Counter
		CheckRegistration()
		if Counter == 0:
			Result = urlopen("http://192.241.244.177/ChatApplication/Registration.php?UserId=" + UserId.get() + "&UserName=" + UserName.get() + "&Password=" + Password.get())
			for Value in Result:
				if int(Value.decode()) == 1:
					tm.showinfo("Registration details", "Successfully Registered")
				else:
					tm.showerror("Registration error", "Registration failed")
		# global Counter
		# Connection = sqlite3.connect(FileName)
		# CreateQuery = "CREATE TABLE IF NOT EXISTS " + TableName + "(UserId TEXT, UserName TEXT, Password TEXT, Status TEXT);"
		# Connection.execute(CreateQuery)
		# CheckRegistration()
		# if Counter == 0:
		# 	InsertQuery = "INSERT INTO " + TableName + " VALUES('%s', '%s', '%s', 'A')"
		# 	Connection.execute(InsertQuery %(UserId.get(), UserName.get(), Password.get()))
		# 	Connection.commit()
			
		# Connection.close()
			root.destroy()
			Login()

	def CheckRegistration():
		global Counter
		# Result = os.system("curl \"http://192.241.244.177/ChatApplication/CheckRegistration.php?UserId=" + UserId.get() +"\"")
		Result = urlopen("http://192.241.244.177/ChatApplication/CheckRegistration.php?UserId=" + UserId.get())
		# print(Result)
		for Value in Result:
			if int(Value.decode()) == 1:
				tm.showerror("Registration error", "User Id already exists")
				Counter = 1
		
		# Connection = sqlite3.connect(FileName)
		# SelectQuery = "SELECT UserId FROM " + TableName
		# Result = Connection.execute(SelectQuery)
		# for Attributes in Result:
		# 	for Counter in range(len(Result)):
		# 		print(Attributes[Counter])
		# 		if Attributes[Counter] == UserId.get():
		# 			tm.showerror("Registration error", "User Id already exists")
				# Counter = 1
		if Password.get() != RetypePassword.get():
			tm.showerror("Registration error", "Password not matched")
			Counter = 1
		if Password.get() == "" or UserId.get() == "":
			tm.showerror("Registration error", "Enter valid details")
			Counter = 1
	root = Tk(className = "Registration Page")
	root.geometry("500x500")
	RegisterLabel = Label(root, text = "Register", font = 30).grid(row = 0, column = 1)
	UserIdLabel = Label(root, text = "User Id:").grid(row = 1, sticky = "w")
	ExampleLabel = Label(root, text = "Example:Jhon123").grid(row = 2, column = 1)
	UserNameLabel = Label(root, text = "User Name:").grid(row = 3, sticky = "w")
	ExampleLabel = Label(root, text = "Example:Jhon Adem").grid(row = 4, column = 1)
	PasswordLabel = Label(root, text = "Password:").grid(row = 5, sticky = "w")
	RetypePasswordLabel = Label(root, text = "Re-type Password:").grid(row = 6, sticky = "w")
	UserId = Entry(root)
	UserName = Entry(root)
	Password = Entry(root, show = "*")
	RetypePassword = Entry(root, show = "*")
	RegisterButton = Button(root, text = "Register", fg = "blue", command = ClickRegisterButton).grid(row = 7, column = 1)
	UserId.grid(row = 1, column = 1)
	UserName.grid(row = 3, column = 1)
	Password.grid(row = 5, column = 1)
	RetypePassword.grid(row = 6, column = 1)
	root.mainloop()

def Login():
	def ClickLogin():
		# Content = os.system("curl \"http://192.241.244.177/ChatApplication/CheckLogin.php?UserId=" + UserId.get() + "&Password=" + Password.get() + "\"")
		Result = urlopen("http://192.241.244.177/ChatApplication/CheckLogin.php?UserId=" + UserId.get() + "&Password=" + Password.get())
		# print(Result.decode())
		for Value in Result:
			print(Value.decode())
			if int(Value.decode()) == 0:
				tm.showerror("Login error", "Invalid details")
			else:
				tm.showinfo("Login info", "Successfully logged in")
				
		# Counter = 0
		# Connection = sqlite3.connect(FileName)
		# SelectQuery = "SELECT UserId, Password FROM " + TableName 
		# Result = Connection.execute(SelectQuery)
		# for Attributes in Result:
		# 	# print(Attributes)
		# 	if Attributes[0] == UserId.get() and Attributes[1] == Password.get():
		
		# 		# Counter = 1
		# # if Counter == 0:
			

	root = Tk(className = "Login Page")
	root.geometry("500x500")
	Welcome = Label(root, text = "Welcome", font = 50).grid(row = 0,column = 1)
	UserId = Label(root, text = "User Id").grid(row = 1)
	Password = Label(root, text = "Password").grid(row = 2)
	UserId = Entry(root)
	Password = Entry(root, show = "*")
	UserId.grid(row = 1, column = 1)
	Password.grid(row = 2, column = 1)
	Login = Button(root, text = "Login", fg = "blue", command = ClickLogin).grid(row = 3, column = 1)
	root.mainloop()	

root = Tk(className = "Chat Application")
root.geometry("500x500")
MainLabel = Label(root, text = "Welcome to Chat Application", font = 30).grid(row = 0, column = 2)
SignUpButton = Button(root, text = "Sign Up", fg = "blue", command = CallRegistrationPage).grid(row = 7, column = 3)
LoginButton = Button(root, text = "Log In", fg = "blue", command = CallLoginPage).grid(row = 7, column = 5)
root.mainloop()