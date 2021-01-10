import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 350, height = 350, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Image Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('verdana', 20))
canvas1.create_window(180, 60, window=label1)
label2 = tk.Label(root, text='Since you\'re too lazy to go online', bg = 'lightsteelblue2')
label2.config(font=('verdana', 10))
canvas1.create_window(180, 90, window=label2)

def getImage ():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    
browseButton = tk.Button(text="    Import Image   ", command=getImage, bg='royalblue', fg='white', font=('verdana', 12, 'bold'))
canvas1.create_window(180, 130, window=browseButton)

def convertToPNG ():
    global im1
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

def convertToJPG ():
    global im1
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveAsButton_PNG = tk.Button(text='Convert to PNG', command=convertToPNG, bg='royalblue', fg='white', font=('verdana', 12, 'bold'))
canvas1.create_window(180, 180, window=saveAsButton_PNG)

saveAsButton_JPG = tk.Button(text='Convert to JPG', command=convertToJPG, bg='royalblue', fg='white', font=('verdana', 12, 'bold'))
canvas1.create_window(180, 230, window=saveAsButton_JPG)

root.mainloop()