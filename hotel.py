import os  # import os library
from random import randrange  # import randrange from random library
from tkinter import *  # import all things from tkinter library

FONT_CHAR = 'Arial'  # font charecter
FONT_SIZE = 18  # font size
FONT = (FONT_CHAR, FONT_SIZE)
FILENAME = 'users.txt'  # save users (file name)

AMOUNT = 500  # amount of rooms


def isFile(file):
    import os
    return os.path.isfile(file)


class Register:
    def __init__(self):
        """
        Register a New User for booking a Room (Room Number)
        """
        self.root = Tk()
        self.root.title("Register in Hotel")  # title of this page
        # size and position `WIDTHxHEIGHT+X+Y`
        self.root.geometry("500x30 0+500+300")

        # Variable for storing Data
        self.firstname_value = StringVar()  # for firstname
        self.lastname_value = StringVar()  # for lastname
        self.id_number_value = StringVar()  # for id number
        self.country_value = StringVar()  # country

    def create_room(self):
        """
        Create a New Room Number that is empty room
        return : room number `int`
        """
        room_number = randrange(1, AMOUNT)  # random number
        if isFile(FILENAME):  # file Exist
            with open(FILENAME, 'rt') as f:  # for opening `FILENAME`
                for line in f.readlines():  # assign line to lines of the file
                    _, _, id_number, _, roomnum = line.split(
                        ' ')  # get information from line of file
                    roomnum = roomnum[-1]  # bray pak kardan "\n"
                    # check if room number of this line from file equal to ranrange(1, ROOM_AMOUNT)
                    if roomnum == room_number:
                        self.create_number()  # go back to start method `Recursion`
        return room_number

    def clear(self):
        """
        Clear All Entry From Tkinter
        """
        self.firstname_value.set('')
        self.lastname_value.set('')
        self.id_number_value.set('')
        self.country_value.set('')

    def create_user(self):
        """
        Append New User to a file (FILENAME) 
        """
        room_num = self.create_room()  # assign room_num to self.creat_room() that return room number
        self.room_num.config(text=room_num)  # change room_num Label to ⬆
        # change room_text Label to `RoomNumber :`
        self.room_text.config(text='RoomNumber :')
        with open('users.txt', 'at') as f:
            # write the content in a file
            f.write(f'{self.firstname_value.get()} {self.lastname_value.get()} {self.id_number_value.get()} {self.country_value.get()} {room_num}\n')
        self.clear()  # clear all Entry

    def run(self):
        """
        Run The Registery Page
        """
        # First Name
        Label(master=self.root, width=15, text="FirstName",
              font=FONT).grid(row=0, column=0)
        Entry(master=self.root, textvariable=self.firstname_value,
              font=FONT).grid(row=0, column=1)

        # Last Name
        Label(master=self.root, width=15, text="LastName",
              font=FONT).grid(row=1, column=0)
        Entry(master=self.root, text='', textvariable=self.lastname_value,
              font=FONT).grid(row=1, column=1)

        # ID Number
        Label(master=self.root, width=15, text="ID NUMBER",
              font=FONT).grid(row=2, column=0)
        Entry(master=self.root, textvariable=self.id_number_value,
              font=FONT).grid(row=2, column=1)

        # Country
        Label(master=self.root, width=15, text="Country",
              font=FONT).grid(row=3, column=0)
        Entry(master=self.root, textvariable=self.country_value,
              font=FONT).grid(row=3, column=1)

        # Creating Submit button
        Button(master=self.root, text="Submit", font=FONT,
               command=self.create_user).grid(row=4, column=1)

        # Room Number
        self.room_text = Label(master=self.root, width=15, font=FONT)
        self.room_text.grid(row=5, column=0)

        self.room_num = Label(master=self.root, width=15, font=FONT)
        self.room_num.grid(row=5, column=1)

        self.root.mainloop()


class Search_Room:
    def __init__(self):
        """
        Search a Room
        if This Room Number DOES exist :show: All information about person's room
        if This Room Number DOESN'T exist :show: NOTHING
        """
        self.root = Tk()
        self.root.title('Search Room')

        # Variable for storing Data
        self.firstname_value = StringVar()
        self.lastname_value = StringVar()
        self.id_number_value = StringVar()
        self.country_value = StringVar()
        self.nationality_value = StringVar()
        self.room_value = StringVar()

    def clear(self):
        """
        Clear Room Value Entry
        """
        self.room_value.set('')

    def find_room(self):
        """
        Find The Given Room Number from file

        Raises:
            FileNotFoundError: `FILENAME` not found
        """
        if isFile(FILENAME):
            with open(FILENAME, 'rt') as f:
                for line in f.readlines():
                    firstname, lastname, id_number, country, roomnum = line.split(
                        ' ')
                    roomnum = roomnum[:-1]
                    if roomnum == self.room_value.get():
                        self.firstname_value.set("First Name : " + firstname)
                        self.lastname_value.set("Last Name : " + lastname)
                        self.id_number_value.set("ID Number : " + id_number)
                        self.country_value.set("Country : " + country)
        else:
            raise FileNotFoundError(FILENAME+' not found')
        self.clear()

    def run(self):
        """
        Run Search of the rooms 
        """
        # Room Number
        Label(self.root, text='Room Number',
              font=FONT).grid(row=0, column=0)
        Entry(self.root, textvariable=self.room_value,
              font=FONT).grid(row=0, column=1)

        # Submit Button
        Button(self.root, text='Submit', font=FONT, command=self.find_room).grid(
            row=1, column=1, columnspan=2)

        # First Name
        Label(self.root, textvariable=self.firstname_value,
              font=FONT).grid(row=2, column=0)

        # Last Name
        Label(self.root, textvariable=self.lastname_value,
              font=FONT).grid(row=3, column=0)

        # id number
        Label(self.root, textvariable=self.id_number_value,
              font=FONT).grid(row=4, column=0)

        # country
        Label(self.root, textvariable=self.country_value,
              font=FONT).grid(row=5, column=0)

        self.root.mainloop()


class Main:
    def __init__(self):
        """
        Select Options :
        1 - Register
        2 - Search Room
        """
        self.root = Tk()
        self.root.title('Options')
        self.root.geometry('250x100+650+350')

    def register(self):
        self.root.destroy()
        Register().run()

    def search_room(self):
        self.root.destroy()
        Search_Room().run()

    def run(self):
        """
        Run The Main Window
        """
        register = Button(self.root, text='Register Hotel',
                          font=FONT, bg='grey', command=self.register)
        register.pack()

        search_room = Button(self.root, text='Search Room',
                             font=FONT, bg='darkgrey', command=self.search_room)
        search_room.pack()

        self.root.mainloop()


if __name__ == "__main__":
    Main().run()
