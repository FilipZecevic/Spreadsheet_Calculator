import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog
import calculations
import re

#Function that gets called after the "New" button is pressed
#The function opens the window so the user can select a file path, it also provides the file path to the main function
def newFile():
    global file_path
    file_path = filedialog.asksaveasfilename(title = "Select the path")
    global file
    print(file_path)
    file = open(file_path, "w")


#Function that gets called after the "Open" button is pressed
#The Function opens the window so the user can select a file path to the exisitng file, it aslo returns the file path to the main function
def openFile():
    global file_path
    file_path = filedialog.askopenfilename(title = "Select the path")
    global file
    print(file_path)
    file = open(file_path, "r")
    arr = []
    id = 0
    with open(file_path, "r") as f:
        for line in f:
            arr.append(line.split(","))
        print(arr)
        for i in range(rows):
            for j in range(column):
                index = column * i + j
                if index % column == 0 or index < column:
                    continue
                
                cells_array[index].delete(0, tk.END)
                cells_array[index].insert(0, arr[id][0])
                id += 1


#Function that gets called after the "Save" button is pressed
#The FUnction opens the window and lets the user choose the file path to save the file
def saveFile():
    file = open(file_path, "w")
    data = get_data_from_array()
    for i in range(rows - 1):
        for j in range(column - 1):
            index=(column - 1) * i + j
            if (index+1) % (column - 1) == 0:
                file.write(data[index])
            else:
                file.write(data[index] + ",")
    file.close()


#Function that gets called after the "Save As" button is pressed
#The Function saves the file at file path selected by user
def saveFileAs():
    newFile()
    data = get_data_from_array()
    for i in range(rows - 1):
        for j in range(column - 1):
            index=(column - 1) * i + j
            file.write(data[index] + ",")
            file.write("\n")    
    file.close()
    print(data)
    return file_path


#Function that returns the anwser to equasions insicde cells
def get_data(event,cell):
    result=cell.get()
    cell.delete(0, tk.END)  # Clear current text
    cell.insert(0, calculations.equasion(result))
    print(cell.get())


#Function that returns the contents of cells
def get_data_from_array():
    lista = []
    content_array = []
    for i in range(rows):
        for j in range(column):
            index = column * i + j
            if index % column == 0 or index<column:
                continue
            if cells_array[index].get() == "":
                content_array.append(" ")
            else:
                content_array.append(cells_array[index].get())
    print(content_array)
    return content_array


#Function that changes from home page to file page
def goToFile():
    home_frame.pack_forget()
    file_frame.pack()


#
def goToHome():
    file_frame.pack_forget()
    home_frame.pack()

#Main window where all the gui is located
root = ctk.CTk()
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("%dx%d" % (x,y))
root.title("SpreadSheet Calculator")

#Makes the frame for the home page
home_frame = tk.Frame(root, background = "#292430")

#Home page elements
navbar = tk.Frame(root, border = 3, width = x, background = "#1ecbe1",)

file_button = tk.Button(
    navbar,
    text = "File",
    background = "#1ecbe1",
    command = goToFile,
    font = "12",
    width=15)

home_button = tk.Button(
    navbar,
    text = "Home",
    background = "#1ecbe1",
    command = goToHome,
    font = "12",
    width=15)
navbar.config(background = "#292430")
navbar.pack(fill="x")
home_button.pack(side = "left", anchor = "n")
file_button.pack(side = "left", anchor = "n")


cells= tk.Frame(home_frame, height=10, width=40)
cells.columnconfigure(0, weight=1)
cells.columnconfigure(1, weight=1)
cells_array = []
dict_with_excel_index = {}
Ascii_number = 65
Ascii_letter = ""
number_for_column = 1
number_of_letters = 1
rows = 4
column = 10


for i in range(rows):
    for j in range(column):
        Ascii_letter = ""
        if i == 0 and j != 0:
            for k in range(number_of_letters):
                Ascii_letter += chr(Ascii_number)
            cell= tk.Entry(cells, width = 8, font=("Arial", 16), justify = 'center')
            cell.insert(0, Ascii_letter)
            cell.config(state = "disabled")
            Ascii_number += 1
            if Ascii_letter == "Z":
                Ascii_number = 65
                number_of_letters += 1
        elif j == 0 and i != 0:
            cell = tk.Entry(cells, width = 2, font = ("Arial", 16), justify = 'center')
            cell.insert(0, number_for_column)
            cell.config(state="disabled")
            number_for_column += 1
        elif j == 0 and i == 0:
            cell = tk.Entry(cells,width=2, font=("Arial",16),justify='center')
            cell.insert(2, "-")
            cell.config(state = "disabled")
        else:
            cell = tk.Entry(cells, width = 8, font = ("Arial", 16))
        cell.grid(row = i, column = j)
        cell.bind('<Return>', lambda event, entry = cell: get_data(event, entry))
        cells_array.append(cell)
cells.pack(side = tk.LEFT, anchor = tk.NW, padx = (30,0), pady = (30,0))
navbar.config(background = "#1ecbe1")


"""button = tk.Button(home_frame, text="Get Data from Entry 12", command = lambda: get_data_from_array())
button.pack()"""

home_frame.pack()
#-----------------------------------------------------------------------------------------------------


#292430 -grey, #1ecbe1 - cyan
#Frame where the file page
file_frame = tk.Frame(root, width = x, height = y, background = "#292430")

label = tk.Label(file_frame, width = x, background = "#1ecbe1", text = "Neki tekstt").pack(side = "top") #Label on top of the page
frame = tk.Frame(file_frame, height = y, border = 5).pack(side = "left") #Makes a frame that the buttons will be placed in

#"New" button
new_button = tk.Button(
    file_frame,
    text = "New",
    height = 3,
    width = 50,
    background = "#292430",
    foreground = "#d1d1d1",
    command = newFile,
    ).pack()


#"Open" button
open_button = tk.Button(
    file_frame,
    text ="Open",
    height = 3,
    width = 50,
    background = "#292430",
    foreground = "#d1d1d1",
    command = openFile,
    ).pack()


#"Save" button
save_button = tk.Button(
    file_frame,
    text ="Save",
    height = 3,
    width = 50,
    background = "#292430",
    foreground = "#d1d1d1",
    command = saveFile,
    ).pack()


#"Save As" button
saveas_button = tk.Button(
    file_frame,
    text = "Save As",
    height = 3,
    width = 50,
    background = "#292430",
    foreground = "#d1d1d1",
    command = saveFileAs,
    ).pack()

root.mainloop()