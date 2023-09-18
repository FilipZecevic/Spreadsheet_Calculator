import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pyautogui
from tkinter import filedialog
import calculations

#Function that gets called after the "New" button is pressed
#The function opens the window so the user can select a file path, it also provides the file path to the main function
def newFile():
    global file_path
    file_path = filedialog.asksaveasfilename(title="Select the path")
    global file
    print(file_path)
    file = open("C:/Users/Lenovo/Desktop/TESTFAJL.txt", "r+")


#Function that gets called after the "Open" button is pressed
#The Function opens the window so the user can select a file path to the exisitng file, it aslo returns the file path to the main function
def openFile():
    global file_path
    file_path = filedialog.askopenfilename(title="Select the path")
    global file
    print(file_path)
    file = open("C:/Users/Lenovo/Desktop/TESTFAJL.txt", "r+")


#Function that gets called after the "Save" button is pressed
#The FUnction opens the window and lets the user choose the file path to save the file
def saveFile():
    openFile()
    file.write(str(get_data_from_array()))
    print(str(get_data_from_array()))


#Function that gets called after the "Save As" button is pressed
#The Function saves the file at file path selected by user
def saveFileAs():
    newFile()
    data=str(get_data_from_array())
    file.write(data)
    print(data)
    return file_path


def ispisi():
    labell=tk.Label(root2, text="maj")
    labell.pack()
def get_data(event,cell):
    result=cell.get()
    cell.delete(0, tk.END)  # Clear current text
    cell.insert(0, calculations.equasion(result))
    print(cell.get())
def scroll_text(*args):
    root2.yview(*args)
def get_data_from_array():
    lista=[]
    content_array=[]
    for i in range(rows):
        for j in range(column):

            index=column*i+j

            if index % column ==0 or index<column:
                continue

            content_array.append(cells_array[index].get())
    print(content_array)
    return content_array





#vezi sa prozorom
root2=tk.Tk()
x = root2.winfo_screenwidth()
y = root2.winfo_screenheight()
root2.geometry("%dx%d" % (x,y))



root2.title("SpreadSheet Calculator")

navbar=tk.Frame(root2,border=3, width=x,bg="lightgreen")
label2=tk.Label(navbar, text="nav")
navbar.config(background="green")
navbar.pack(fill="x")
label2.pack( anchor=tk.NW)


label= tk.Label(
    root2,
    text="SpreadShit Calculator",
    font=("Ariel",16),
    width=x,
    height=2
)

label.pack()
cells= tk.Frame(root2, height=10, width=40,)

cells.columnconfigure(0,weight=1)
cells.columnconfigure(1,weight=1)
cells_array=[]

dict_with_excel_index={}

Ascii_number=65
Ascii_letter=""
number_for_column=1
number_of_letters=1

rows=4
column=10

for i in range(rows):
    for j in range(column):
        Ascii_letter=""
        if i==0 and j!=0:

            for k in range(number_of_letters):
                Ascii_letter+=chr(Ascii_number)

            cell= tk.Entry(cells,width=8, font=("Arial",16),justify='center')
            cell.insert(0,Ascii_letter)
            cell.config(state="disabled")
            Ascii_number+=1
            if Ascii_letter=="Z":
                Ascii_number=65
                number_of_letters+=1

        elif j==0 and i!=0:
            cell= tk.Entry(cells,width=2, font=("Arial",16),justify='center')
            cell.insert(0,number_for_column)
            cell.config(state="disabled")
            number_for_column+=1
        elif j==0 and i==0:
            cell= tk.Entry(cells,width=2, font=("Arial",16),justify='center')
            cell.insert(2,"-")
            cell.config(state="disabled")
        else:
            cell= tk.Entry(cells,width=8, font=("Arial",16))
        cell.grid(row=i,column=j)
        cell.bind('<Return>', lambda event, entry=cell: get_data(event, entry))
        cells_array.append(cell)
        #
cells.pack(side=tk.TOP, anchor=tk.NW,padx=(60,0), pady=(60,0))
navbar.config(background="#123332")



button = tk.Button(root2, text="Get Data from Entry 12", command=lambda: get_data_from_array())
button.pack()

#-----------------------------------------------------------------------------------------------------

root = ctk.CTk(fg_color = "#292430") #Sets the root as the main window
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.attributes("-alpha", True)
root.geometry("%dx%d" % (x,y),)
root.title("File")


label = tk.Label(root, width=x, text="SpreadShit Calculator").pack(side="top") #Label on top of the page

frame = tk.Frame(root, height=y, border=5).pack(side="left") #Makes a frame that the buttons will be placed in


#Makes the "New" button
new_button = tk.Button(
    frame,
    text="New",
    height= 3,
    width= 50,
    background= "#292430",
    foreground= "#d1d1d1",
    command=newFile,
    ).pack(anchor="w")


#Makes the "Open" button
open_button = tk.Button(
    frame,
    text="Open",
    height= 3,
    width= 50,
    background= "#292430",
    foreground= "#d1d1d1",
    command=openFile,
    ).pack(anchor="w")


#Makes the "Save" button
save_button = tk.Button(
    frame,
    text="Save",
    height= 3,
    width= 50,
    background= "#292430",
    foreground= "#d1d1d1",
    command= newFile,
    ).pack(anchor="w")


#Makes the "Save As" button
saveas_button = tk.Button(
    frame,
    text="Save As",
    height= 3,
    width= 50,
    background= "#292430",
    foreground= "#d1d1d1",
    command= saveFileAs,
    ).pack(anchor="w")


root.mainloop()

