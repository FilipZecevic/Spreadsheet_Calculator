from tkinter import *
import tkinter as tk
import customtkinter as ctk
import calculations 

def ispisi():
    labell=tk.Label(root, text="majmuni mrtvi")
    labell.pack()
def get_data(event,cell):
    result=cell.get()
    cell.delete(0, tk.END)  # Clear current text
    cell.insert(0, calculations.equasion(result))
    print(cell.get())
def scroll_text(*args):
    root.yview(*args)
def get_data_from_array():
    lista=[]
    content_array=[]
    for i in range(rows):
        for j in range(column):
            
            index=column*i+j
            
            if index % column ==0 or index<column:
                continue
            if cells_array[index].get()=="":
                content_array.append("NaN")
            else:
                content_array.append(cells_array[index].get())      
    print(content_array)
    making_dictionary(content_array)
    return content_array
            
def get_data_from_content_array_with_excel_index():
    excel_indexes_array=[]
    
    for i in range(rows):
        for j in range(column):
            s=""
            index=column*i+j
            if index % column ==0 or index<column:
                continue
            s=cells_array[j].get()+str(i)
            excel_indexes_array.append(s)
            print(s,end=" ")
        print()
    
    return  excel_indexes_array

#with A1 B2 C3 indexing
def making_dictionary(content_array):
    array_with_excel_indexes= {}
    for i in range(len(excel_indexes_array)):
        array_with_excel_indexes[i]= dict({"key": excel_indexes_array[i], "content": content_array[i]})
        print(array_with_excel_indexes[i])


#vezi sa prozorom
root=tk.Tk()
x = root.winfo_screenwidth() 
y = root.winfo_screenheight() 
root.geometry("%dx%d" % (x,y))



root.title("SpreadSheet Calculator")

navbar=tk.Frame(root,border=3, width=x,bg="lightgreen")
label2=tk.Label(navbar, text="nav")
navbar.config(background="green")
navbar.pack(fill="x")
label2.pack( anchor=tk.NW)

label= tk.Label(
    root,
    text="SpreadShit Calculator",
    font=("Ariel",16), 
    width=x, 
    height=2
)

label.pack()
cells= tk.Frame(root, height=10, width=40,)

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
excel_indexes_array=[]
excel_indexes_array=get_data_from_content_array_with_excel_index()
#content_array=[]
#content_array=get_data_from_array()



button = tk.Button(root, text="excel indexing", command=lambda: get_data_from_array())
button.pack()
root.mainloop()

