import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pyautogui
from tkinter import filedialog

#Function that gets called after the "New" button is pressed
#The function opens the window so the user can select a file path, it also provides the file path to the main function
def newFile():
    global file_path
    file_path = filedialog.asksaveasfilename(title="Select the path")
    global file
    file = open(file_path, "rw")
    return file_path


#Function that gets called after the "Open" button is pressed
#The Function opens the window so the user can select a file path to the exisitng file, it aslo returns the file path to the main function
def openFile():
    global file_path
    file_path = filedialog.askopenfilename(title="Select the path")
    global file
    file = open(file_path, "rw")
    return file_path


#Function that gets called after the "Save" button is pressed
#The FUnction opens the window and lets the user choose the file path to save the file
#def saveFile():
#    file.write(data)


#COLOR PALLET
#292430 -grey, #1ecbe1 - cyan, #d1d1d1 - light gray(text)


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
#SAVE AS BUTTON TO BE ADDED SOON...



root.mainloop()

