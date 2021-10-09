import tkinter as tk
from tkinter import font
import PyPDF2
from PIL import  Image, ImageTk
from tkinter.filedialog import askopenfile

from PyPDF2 import pagerange

root = tk.Tk()
Canvas =tk.Canvas(root, width =600,height=300)
Canvas.grid(columnspan=3,rowspan=3)

#image
img =Image.open('logo.png')
img = ImageTk.PhotoImage(img)
img_label = tk.Label(image=img)
img_label.image = img
img_label.grid(column = 1, row=0)

# instructions
instructions = tk.Label(root, text ="Select PDF file from your device to extract text: ")
instructions.grid(columnspan=3,row=1)

#define function
def open_file():
    #test
   #print("working")
   browse_txt.set("Loading...")
   file =askopenfile(parent=root,mode='rb',title="chose a pdf file",filetype=[("pdf file","*pdf")])
   if file:
       read_pdf =PyPDF2.PdfFileReader(file)
       page =read_pdf.getPage(0)
       page_cont = page.extractText()
       #print(page_cont)

       #text wedget box
       text_box = tk.Text(root,height=10,width=50,padx=15,pady=15)
       text_box.insert(1.0,page_cont)
       text_box.grid(columnspan=3,row=3)
       browse_txt.set("Browse")
#the browse Button
browse_txt = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_txt, command=lambda:open_file(), font="Times",bg="red",fg="white",height=2,width=14)
browse_txt.set("Browse")
browse_btn.grid(column =1,row=2)

#Canvas
Canvas = tk.Canvas(root,width=530,height=250)
Canvas.grid(columnspan=3)


root.mainloop()