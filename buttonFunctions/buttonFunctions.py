import mysql.connector as mysql
import os
import tkinter as tk
from GUI import homepage

def login(username, password, frames):
    """ This function is to veryify login details """
    conn = mysql.connect(
        host= "localhost",
        user= os.environ.get("dbUser"),
        password= os.environ.get("dbPass"),
        database= "house"
    )

    cursor = conn.cursor()
    login_query = f"""
            SELECT firstName, lastName
            FROM users
            WHERE username='{username.get()}' 
            AND password='{password.get()}';
            """
    cursor.execute(login_query)

    row = cursor.fetchall() # store collected values

    if len(row) == 0: # if there are no compatible values 
        tk.messagebox.showinfo(
            'info', 
            'Incorrect username or password'
            )
        # Delete entered values
        username.delete(0,tk.END)
        password.delete(0,tk.END)
    else:
        """Change page """ # go to user homepage
        homepage.homepage(
            frames[0], 
            frames[1], 
            frames
            )
    
    conn.commit()
    conn.close()