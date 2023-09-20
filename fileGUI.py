import tkinter as tk
from tkinter import ttk, Canvas, Scrollbar
import customtkinter as ctk
from tkinter import filedialog
import calculations


def newFile():
    """Function that gets called after the "New" button is pressed
    The function opens the window so the user can select a file path, it also provides the file path to the main function"""
    global file_path
    current_rows = 21
    current_column = 11
    file_path= filedialog.asksaveasfilename(title="Select the path")
    
    arr=[]
    
    global cells_array
    

    with open(file_path, "w+") as f:
        f.write(str(current_rows))
        f.write(" ")
        f.write(str(current_column))

        f.close()
    for cellss in cells_array:
        cellss.destroy() 

    cells_array=tabela(current_rows,current_column)
    global row
    row= current_rows
    global column
    column=current_column
    home_button.configure(background = "#1ecbe1", command = goToHome, font = "12", width=15, state = "disabled")
    file_button.configure(state = "active")
    file_frame.pack_forget()
    home_frame.pack(anchor = "nw", fill = "both")
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    #save_button.configure(state = "active")
    #saveas_button.configure(state = "active")

    
    
            

def tabela(current_rows,current_column):
    cells_array=[]
    Ascii_number=65
    Ascii_letter=""
    number_for_column=1
    number_of_letters=1
    for i in range(int(current_rows)):
        for j in range((current_column)):
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
            
    return cells_array


def openFile():
    """Function that gets called after the "Open" button is pressed
    The Function opens the window so the user can select a file path to the exisitng file, it aslo returns the file path to the main function"""
    global file_path
    file_path = filedialog.askopenfilename(title="Select the path")
    global file
    
    #file = open(file_path, "r")
    current_rows,current_column=current_rows_and_columns(file_path)
    arr=[]
    #arr=[" " for i in range((current_column-1)*(current_rows-1))]
    #file.close()
    id=1
    global cells_array
    for cellss in cells_array:
        cellss.destroy()    
    cells_array= []
    cells_array=tabela(current_rows,current_column) 
    arr.append(str(current_rows)+" "+str(current_column))
    with open(file_path, 'r+') as file:
        lines = file.readlines()[1:]  # Read all lines except the first one
        for line in lines:
            
        
            
            arr.append(line.split(","))
            
        
        
        current_rows=int(current_rows)
        current_column=int(current_column)
        for i in range(current_rows):
            for j in range(current_column):
                index= current_column*i+j
                if index % current_column ==0 or index<current_column:
                    continue
                if not arr[id][0]:
                    arr[id][0]=arr[id][0].replace("{","")
                    arr[id][0]=arr[id][0].replace("}","")
                
                
                      
                cells_array[index].insert(0,arr[id][0])
                if arr[id][0]==" ":
                    cells_array[index].delete(0,tk.END)
                id+=1
    global row
    row= current_rows
    global column
    column=current_column
    home_button.configure(background = "#1ecbe1", command = goToHome, font = "12", width=15, state = "disabled")
    file_button.configure(state = "active")
    file_frame.pack_forget()
    home_frame.pack(anchor = "nw", fill = "both")
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    #save_button.configure(state = "active")
    #saveas_button.configure(state = "active")
    

def current_rows_and_columns(file_path):
    arr=[]
    dimenzije=[]
    with open(file_path, "r+") as f:
        for line in f:
            
            arr.append(line.split(","))
        
        x=arr[0]
        

        numbers_list = x[0].split()

# Convert the elements to integers
        number1 = int(numbers_list[0])
        number2 = int(numbers_list[1])
        
        
    return number1,number2


def add_x_area():
    global file_path
    global cells_array
    current_rows,current_column=current_rows_and_columns(file_path)
    content_array=[]
    
    current_rows+=1
    id=1
    content_array.append(str(current_rows)+" "+str(current_column))
    for i in range(current_rows):
        for j in range( current_column):

            index= current_column*i+j
            
            if index %  current_column ==0 or index< current_column:
                continue
            
            if index>= current_column*(current_rows-1):
                    
                content_array.append(" ")
            else:
                
                if cells_array[index].get() =="":
                    content_array.append(" ")
                else:
                    content_array.append(cells_array[index].get())
    with open(file_path, "w+") as f:
        f.write(str(current_rows))
        f.write(" ")
        f.write(str(current_column))
        f.write("\n")
        
        for i in range(current_rows-1):
            for j in range(current_column-1):
                index=(current_column-1)*i+j
            
            
                f.write(content_array[index]+",")
            
                f.write("\n")
    
    for cellss in cells_array:
        cellss.destroy()
    cells_array=tabela(current_rows,current_column)
    
    with open(file_path, 'r+') as file:
        
        for i in range(current_rows):
            for j in range(current_column):
                index= current_column*i+j
                if index % current_column ==0 or index<current_column:
                    continue

                
                      
                cells_array[index].insert(0,content_array[id])
                if content_array[id][0]==" ":
                    cells_array[index].delete(0,tk.END)
                id+=1
    global row
    row= current_rows
    global column
    column=current_column
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def add_y_area():
    global file_path
    global cells_array
    current_rows,current_column=current_rows_and_columns(file_path)
    content_array=[]
    
    current_column+=1
    id=1
    br=1
    indexx=0
    content_array.append(str(current_rows)+" "+str(current_column))
    for i in range(current_rows):
        for j in range( current_column):

            index= current_column*i+j
            
            if index %  current_column ==0 or index< current_column:
                continue
            
            if index % (current_column)== current_column-1:
                
                content_array.append(" ")
                br+=1
            else:

                if cells_array[index-br].get() =="":
                    content_array.append(" ")
                else:
                    content_array.append(cells_array[index-br].get())
    with open(file_path, "w") as f:
        f.write(str(current_rows))
        f.write(" ")
        f.write(str(current_column))
        f.write("\n")
        
        for i in range(current_rows-1):
            for j in range(current_column-1):
                index=(current_column-1)*i+j
            
            
                f.write(content_array[index]+",")
            
                f.write("\n")
    
    for cellss in cells_array:
        cellss.destroy()
    cells_array=tabela(current_rows,current_column)
    
    with open(file_path, 'r+') as file:
        
        for i in range(current_rows):
            for j in range(current_column):
                index= current_column*i+j
                if index % current_column ==0 or index<current_column:
                    continue

                
                
                      
                cells_array[index].insert(0,content_array[id])
                if content_array[id][0]==" ":
                    cells_array[index].delete(0,tk.END)
                id+=1   
    global row
    row= current_rows
    global column
    column=current_column
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

#Function that gets called after the "Save" button is pressed
#The FUnction opens the window and lets the user choose the file path to save the file
def saveFile():
    
    global file_path
    
    current_rows,current_column=current_rows_and_columns(file_path)
    data=get_data_from_array(current_rows,current_column)
    with open(file_path, "w+") as f:
        f.write(str(current_rows))
        f.write(" ")
        f.write(str(current_column))
        f.write("\n")

        for i in range(current_rows-1):
            for j in range(current_column-1):
                index=(current_column-1)*i+j
            
            
                f.write(data[index]+",")
            
                f.write("\n")
        
        

            
            
        
  
    


#Function that gets called after the "Save As" button is pressed
#The Function saves the file at file path selected by user
def saveFileAs():
    global file_path
    file_path= filedialog.asksaveasfilename(title="Select the path")
    
    global row

    global column

    data=get_data_from_array(row,column)
    with open(file_path, "w+") as f:
        f.write(str(row))
        f.write(" ")
        f.write(str(column))
        f.write("\n")
        for i in range(row-1):
            for j in range(column-1):
                index=(column-1)*i+j
                
                
                f.write(data[index]+",")
                
                f.write("\n")
    
    


def ispisi():
    labell=tk.Label(root, text="maj")
    labell.pack()
def get_data(event,cell):
    result=cell.get()
    cell.delete(0, tk.END)  # Clear current text
    cell.insert(0, calculations.equasion(result))
    


def get_data_from_array(current_rows,current_column):
    content_array=[]
    global file_path
    print(str(current_column)+" "+ str(current_rows))
    global cells_array
    for i in range(current_rows):
        for j in range( current_column):

            index= current_column*i+j

            if index %  current_column ==0 or index< current_column:
                continue
            

            if cells_array[index].get() =="":
                content_array.append(" ")
            else:
                content_array.append(cells_array[index].get())
    return content_array

def get_data_from_content_array_with_excel_index():
    excel_indexes_array=[]
    global file_path
    current_rows, current_column=current_rows_and_columns(file_path)
    for i in range(current_rows):
        for j in range(current_column):
            s=""
            index=current_column*i+j
            if index % current_column ==0 or index<current_column:
                continue
            s=cells_array[j].get()+str(i)
            excel_indexes_array.append(s)
            
    
    return  excel_indexes_array

def making_dictionary():
    global row

    global column
    content_array=get_data_from_array(row,column)
    array_with_excel_indexes= {}
    id=0
    for i in range(len(get_data_from_content_array_with_excel_index())):
        array_with_excel_indexes[i+2]= dict({
            "key": get_data_from_content_array_with_excel_index()[id],
            "content": content_array[id]
            })
        id+=1
        
    return array_with_excel_indexes

#Function that changes from home page to file page
def goToFile():
    home_frame.pack_forget()
    file_frame.pack(side = "left", anchor = "nw", fill = "both")
    file_button.configure(state = "disabled")
    home_button.configure(state = "active")
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    

#Function that changes from file gage to home page
def goToHome():
    file_frame.pack_forget()
    home_frame.pack(anchor = "nw", fill = "both")
    home_button.configure(state = "disabled")
    file_button.configure(state = "active")
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


#vezi sa prozorom   
root = ctk.CTk()
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("%dx%d" % (x,y))
root.title("SpreadSheet Calculator")
root.configure(bg = "#292430")

#Frame for the home page
home_frame = tk.Frame(root, background = "#292430")
   
canvas = Canvas(home_frame, background = "#292430", width = x, height = y)

#Vertical scrollbar
scrollbar_y = Scrollbar(home_frame, orient = "vertical", command = canvas.yview)
scrollbar_y.pack(side = "right", fill = "y", anchor = "e")

scroll_frame = tk.Frame(home_frame, background="#292430", width = x)

scrollbar_x = Scrollbar(home_frame, orient = "horizontal", command = canvas.xview)
scrollbar_x.pack(side = "bottom", fill = "x", anchor = "s")

canvas.pack(anchor = tk.NW, padx = (30, 0), pady = (30, 0), fill = "both", expand=True)
canvas.config(yscrollcommand=scrollbar_y.set, xscrollcommand = scrollbar_x.set)

#Home page elements
navbar = tk.Frame(root, border = 3, width = x, background = "#1ecbe1",)

file_button = tk.Button(
    navbar,
    text = "File",
    background = "#1ecbe1",
    command = goToFile,
    font = "12",
    width=15,
    state = "disabled")

home_button = tk.Button(
    navbar,
    text = "Home",
    background = "#1ecbe1",
    command = goToHome,
    font = "12",
    width=15,
    state = "disabled")
navbar.config(background = "#292430")
navbar.pack(fill="x")
home_button.pack(side = "left", anchor = "n")
file_button.pack(side = "left", anchor = "n")




cells= tk.Frame(canvas, height=10, width=40)
cells.columnconfigure(0, weight=1)
cells.columnconfigure(1, weight=1)
cells_array = []

plus_x_button= tk.Button(
    home_frame,
    width=10,
    height=2,
    text="Add Row",
    command=add_x_area,
    font = ("Arial", 13, "bold")
    

).pack(side=tk.LEFT, padx=(40,0),pady=(15,10))
plus_y_button= tk.Button(
    home_frame,
    width=10,
    height=2,
    text="Add Column",
    command=add_y_area,
    font = ("Arial", 13, "bold")

).pack(side=tk.LEFT, padx=(30,0),pady=(15,10))

cells.pack(side = tk.LEFT, anchor = tk.NW, padx = (30,0), pady = (30,0))
navbar.config(background = "#1ecbe1")


canvas.create_window((0, 0), window=cells, anchor=tk.NW)
scroll_frame.pack(anchor = "s", fill = "x", side = "bottom")

# Update the canvas scroll region
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

#-----------------------------------------------------------------------------------------------------


#292430 -grey, #1ecbe1 - cyan
#Frame where the file page
file_frame = tk.Frame(root, width = x, height = y, background = "#292430",)

# label = tk.Label(file_frame, width = x, background = "#1ecbe1", text = "Neki tekstt").pack(side = "top") #Label on top of the page
frame = tk.Frame(file_frame, height = y, border = 5).pack(side = "left", fill = "y") #Makes a frame that the buttons will be placed in

#"New" button
new_button = tk.Button(
    file_frame,
    text = "New",
    height = 3,
    width = 40,
    font = 12,
    background = "#292430",
    foreground = "#d1d1d1",
    command = newFile,
    ).pack(anchor = "w")


#"Open" button
open_button = tk.Button(
    file_frame,
    text ="Open",
    height = 3,
    width = 40,
    font = 12,
    background = "#292430",
    foreground = "#d1d1d1",
    command = openFile,
    ).pack(anchor = "w")


#"Save" button
save_button = tk.Button(
    file_frame,
    text ="Save",
    height = 3,
    width = 40,
    font = 12,
    background = "#292430",
    foreground = "#d1d1d1",
    command = saveFile,
    #state = "disabled"
    ).pack(anchor = "w")

#"Save As" button
saveas_button = tk.Button(
    file_frame,
    text = "Save As",
    height = 3,
    width = 40,
    font = 12,
    background = "#292430",
    foreground = "#d1d1d1",
    command = saveFileAs,
    #state = "disabled"
    ).pack(anchor = "w")
file_frame.pack(side = "left", anchor = "nw", fill = "both")

root.mainloop()
