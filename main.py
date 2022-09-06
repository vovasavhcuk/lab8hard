from tkinter import *
from Actor import Actor
from configparser import ConfigParser
import mysql
import mysql.connector
from mysql.connector import Error

database_name = "pythonDB"
user = "root"
password = "Hydroo2014$%"


class FirstWindow:

    def __init__(self, master):
        master.title('lab5')
        master.geometry('300x100')

        frame = Frame(master)
        frame.pack(fill=X)

        self.addButton = Button(frame, text='Add an Actor', command=self.open_window)
        self.addButton.pack(fill=BOTH)
        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(fill=BOTH)

    @staticmethod
    def open_window():
        root1.destroy()
        root2 = Tk()
        SecondWindow(root2)
        root1.mainloop()


class SecondWindow(FirstWindow):
    actorList = []
    filename = str()

    def __init__(self, master):
        master.protocol('WM_DELETE_WINDOW', self.close)
        var1 = StringVar()

        frame_top = Frame(master)
        frame_top.pack()
        frame1 = Frame(master)
        frame1.pack(side=TOP, fill=BOTH)

        self.label = Label(frame_top, text='Actor\'s name')
        self.label.grid(row=0, column=0, sticky=E)
        self.label1 = Label(frame_top, text='Actor\'s salary')
        self.label1.grid(row=1, column=0, sticky=E)
        self.label2 = Label(frame_top, text='Actor\'s role')
        self.label2.grid(row=2, column=0, sticky=E)
        self.label3 = Label(frame_top, text='Actor\'s film')
        self.label3.grid(row=3, column=0, sticky=E)

        self.txt = Entry(frame_top)
        self.txt.grid(row=0, column=1)
        self.txt1 = Entry(frame_top)
        self.txt1.grid(row=1, column=1)
        self.txt2 = Entry(frame_top)
        self.txt2.grid(row=2, column=1)
        self.txt3 = Entry(frame_top)
        self.txt3.grid(row=3, column=1)

        self.btn1 = Button(frame1, text='Save', command=self.write_to_file)
        self.btn1.pack(fill=X)
        self.showBtn = Button(frame1, text='Show list', command=self.show_btn_click)
        self.showBtn.pack(fill=X)
        self.delBtn = Button(frame1, text='delete by name', command=self.delete_line_by_name)
        self.delBtn.pack(fill=X)
        self.closeBtn = Button(frame1, text='Close', command=self.close)
        self.closeBtn.pack(fill=X)

    def write_to_file(self):

        conn = mysql.connector.connect(host='localhost', database=database_name, user=user, password=password)
        cursor = conn.cursor()

        add_person = ("INSERT INTO people " 
                      "( name, salary, role, film )"
                      "VALUES (%s, %s, %s, %s)")

        data_person = (self.txt.get(), self.txt1.get(), self.txt2.get(), self.txt3.get())

        cursor.execute(add_person, data_person)
        conn.commit()
        cursor.close()

        conn.close()

    def delete_line_by_name(self):

        cnx = mysql.connector.connect(host='localhost', database=database_name, user=user, password=password)
        cursor = cnx.cursor()

        delete_by_name = "DELETE FROM people WHERE name = %s "
        actor_name = (self.txt.get())

        cursor.execute(delete_by_name, (actor_name,))
        cnx.commit()
        cursor.close()

        cnx.close()

    def show_btn_click(self):
        cnxn = mysql.connector.connect(host='localhost', database=database_name, user=user, password=password)
        cursor = cnxn.cursor(buffered=True)
        query = "SELECT * FROM people"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        cnxn.commit()
        cursor.close()

        cnxn.close()

    @staticmethod
    def close():
        root1.quit()


if __name__ == '__main__':
    root1 = Tk()
    root1['bg'] = '#0319FC'
    root1.title('my son is gay')
    root1.geometry('300x200')
    a = FirstWindow(root1)
    root1.mainloop()



