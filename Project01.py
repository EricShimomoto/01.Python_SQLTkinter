from os import stat_result
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('My first datapbase applicartion')
root.geometry("400x400")

#Database

#Create a database or connect
conn = sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

# Create a table
# c.execute("""CREATE TABLE addresses(
#         first_name text, 
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#         )""")

#Create labels
f_name_label = Label(root,text='First Name')
f_name_label.grid(row=0,column=0,padx=20)
l_name_label = Label(root,text='Last Name')
l_name_label.grid(row=1,column=0)
add_label = Label(root,text='Address')
add_label.grid(row=2,column=0)
city_label = Label(root,text='City')
city_label.grid(row=3,column=0,padx=20)
state_label = Label(root,text='State')
state_label.grid(row=4,column=0,padx=20)
z_code_label = Label(root,text='Zip Code')
z_code_label.grid(row=5,column=0,padx=20)


#Create text box
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)
add = Entry(root,width=30)
add.grid(row=2,column=1)
city = Entry(root,width=30)
city.grid(row=3,column=1)
state = Entry(root,width=30)
state.grid(row=4,column=1)
z_code = Entry(root,width=30)
z_code.grid(row=5,column=1)

#create submit button
subimit_but = Button(root, text="Add", command = lambda:submit())
subimit_but.grid(row=6,column=0, columnspan=2, pady=5,padx=10, ipadx=150)

#create submit function to database
def submit():

    #Create a database or connect
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    #Inser into a table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :add, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'add': add.get(),
                'city': city.get(),
                'state' : state.get(),
                'zipcode' : z_code.get()
            }    
        )

    #commit changes
    conn.commit()

    #Close connection
    conn.close()

    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    add.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    z_code.delete(0,END)


#create a view button
view_but = Button(root, text="View", command = lambda:view())
view_but.grid(row=7,column=0, columnspan=2, pady=5,padx=10, ipadx=150)

#create submit function to database
def view():

    #Create a database or connect
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    #Inser into a table
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    print(records)

    #commit changes
    conn.commit()

    #Close connection
    conn.close()



#create a view button
clearall_but = Button(root, text="Clear All", command = lambda:clearall())
clearall_but.grid(row=8,column=0, columnspan=2, pady=5,padx=10, ipadx=150)

#create submit function to database
def clearall():

    #Create a database or connect
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    #Inser into a table
    c.execute("DELETE FROM addresses")



    #commit changes
    conn.commit()

    #Close connection
    conn.close()



#commit changes
conn.commit()

#Close connection
conn.close()


root.mainloop()