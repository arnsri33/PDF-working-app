# Made By Arnav Srivastav For AP CSP PERIOD 1
#Code uses the Tkinter Library for the GUI that opens a PDF and reads it.
#Tutorial from "python simplified" from youtube.
#Has ability to export text as pdf aswell


# Basically imports all of the libraries that are needed
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter import END
from tkinter.filedialog import askopenfile
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas


#initializes the window
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#opens the logo of the program
logo = Image.open('scene.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)



# instructions for the layering and organization of the code
instructions = tk.Label(root, text="Select file for text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)


#BROWSE button code
def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        
        page_content = page.extract_text()

        # text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

#creates a browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#cc6699", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=0, row=2)






# Opens a text box for the individual to type into and export to the pdf
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
text_box.grid(column=1, row=3)



def save_pdf():
    text_content = text_box.get("1.0", END)
    print(text_content)
    
    
    
    
    # Sets the size of the pdf
    canvas = Canvas("FinalPDF.pdf", pagesize=LETTER)

  # Font used the the times roman, size 14
    canvas.setFont("Times-Roman", 14)

    
    canvas.drawString(1 * inch, 10 * inch, text_content)

    # Save the PDF file
    canvas.save()

 
    save_text.set("Saved!")







#save pdf button
save_text = tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text, command=lambda:save_pdf(), font="Raleway", bg="#cc6699", fg="white", height=2, width=15)
save_text.set("Save PDF")

save_btn.grid(column=2, row=2)

root.mainloop()

# End loop 
