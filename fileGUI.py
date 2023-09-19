import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog
import calculations

cells_array=[]
#Function that gets called after the "New" button is pressed
#The function opens the window so the user can select a file path, it also provides the file path to the main function
def newFile():
    global file_path
    current_rows=input()
    current_column=input()
    
    if current_rows.isdigit():
        current_rows=int(current_rows)
    if current_column.isdigit():
        current_column=int(current_column)
    file_path= filedialog.asksaveasfilename(title="Select the path")
    print(file_path)
    arr=[]
    
    global cells_array
    cells_array=[]

    with open(file_path, "w+") as f:
        f.write(str(current_rows))
        f.write(" ")
        f.write(str(current_column))

        f.close()
    for cellss in cells_array:
        cellss.destroy() 

    cells_array=tabela(current_rows,current_column)
    
    
            

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
#Function that gets called after the "Open" button is pressed
#The Function opens the window so the user can select a file path to the exisitng file, it aslo returns the file path to the main function
def openFile():
    global file_path
    file_path = filedialog.askopenfilename(title="Select the path")
    global file
    print(file_path)
    #file = open(file_path, "r")
    current_rows,current_column=current_rows_and_columns()
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
            
            print(line)
            
            arr.append(line.split(","))
            
        print(arr)
        
        current_rows=int(current_rows)
        current_column=int(current_column)
        for i in range(current_rows):
            for j in range(current_column):
                index= current_column*i+j
                if index % current_column ==0 or index<current_column:
                    continue
                print("asdafs: "+ str(id) +"index: "+ str(index))
                arr[id][0]=arr[id][0].replace("{","")
                arr[id][0]=arr[id][0].replace("}","")
                
                
                print(arr[id][0])       
                cells_array[index].insert(0,arr[id][0])
                id+=1
    

def current_rows_and_columns():
    arr=[]
    dimenzije=[]
    with open(file_path, "r+") as f:
        for line in f:
            print(line+"safa")
            arr.append(line.split(","))
        
        x=arr[0]
        print(x[0])

        numbers_list = x[0].split()

# Convert the elements to integers
        number1 = int(numbers_list[0])
        number2 = int(numbers_list[1])
        
        
    return number1,number2

    


#Function that gets called after the "Save" button is pressed
#The FUnction opens the window and lets the user choose the file path to save the file
def saveFile():
    
    
    data=get_data_from_array()
    current_rows,current_column=current_rows_and_columns()
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

    file_path= filedialog.asksaveasfilename(title="Select the path")
    data=get_data_from_array()
    current_rows, current_column=current_rows_and_columns()

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
    print(data)
    


def ispisi():
    labell=tk.Label(root2, text="maj")
    labell.pack()
def get_data(event,cell):
    result=cell.get()
    cell.delete(0, tk.END)  # Clear current text
    cell.insert(0, calculations.equasion(result))
    print(cell.get())


def get_data_from_array():
    content_array=[]

    current_rows, current_column=current_rows_and_columns()
    for i in range(current_rows):
        for j in range( current_column):

            index= current_column*i+j

            if index %  current_column ==0 or index< current_column:
                continue
            if cells_array[index].get() =="":
                content_array.append(" ")
            else:
                content_array.append(cells_array[index].get())
    print(content_array)
    return content_array

def get_data_from_content_array_with_excel_index():
    excel_indexes_array=[]
    current_rows, current_column=current_rows_and_columns()
    for i in range(current_rows):
        for j in range(current_column):
            s=""
            index=current_column*i+j
            if index % current_column ==0 or index<current_column:
                continue
            s=cells_array[j].get()+str(i)
            excel_indexes_array.append(s)
            print(s,end=" ")
        print()
    
    return  excel_indexes_array

def making_dictionary():
    content_array=get_data_from_array()
    array_with_excel_indexes= {}
    id=0
    for i in range(len(get_data_from_content_array_with_excel_index())):
        array_with_excel_indexes[i+2]= dict({
            "key": get_data_from_content_array_with_excel_index()[id],
            "content": content_array[id]
            })
        id+=1
        
    return array_with_excel_indexes



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


dict_with_excel_index={}




cells= tk.Frame(root2, height=10, width=40,)

cells.columnconfigure(0,weight=1)
cells.columnconfigure(1,weight=1)
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
    command= saveFile,
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

