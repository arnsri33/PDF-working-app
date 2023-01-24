# Made by arnav srivastav for the AP CSP class
# Does not work currently as the module is retired,  the PDF reader one


import tkinter as tk
import PyPDF2
import PdfReader
from PIL import  Image , ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas =tk.Canvas(root , width = 600 , height = 300)
canvas.grid(columnspan=3 , rowspan=3)

#logo 
logo =Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)

logo_label =tk.Label(image=logo)
logo_label.image = logo

logo_label.grid(column = 1 , row = 0)


#instructions of the thing
intstructions = tk.Label (root , text = "Select A PDF from your COMP to extract the text from it.")
intstructions.grid(columnspan=3, row= 1)

def open_file():
    browse_text.set("Loading.....")
    file = askopenfile(parent = root , mode= 'rb',  title=  "choose a file" , filetype = [("Pdf file ", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extract_text()
        print(page_content)
        

#making a browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root , textvariable = browse_text,  command=lambda:open_file() ,bg="#20bebe" ,fg = "white" , height = 2 , width = 15)

browse_text.set("Broswe")
browse_btn.grid(column = 1, row = 2)

canvas =tk.Canvas(root , width = 600 , height = 250)
canvas.grid(columnspan=3 , rowspan=3)


root.mainloop()