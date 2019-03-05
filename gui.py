import tkinter as tk
import resizer as rz
from tkinter import StringVar
from tkinter import filedialog
from tkinter import messagebox

def browse_button():
    global file_dir
    filename = filedialog.askdirectory()
    file_dir = filename
    messagebox.showinfo('Successful', 'Directory selected successfully')
    
def resize():
    width = int(input_width.get())
    height = int(input_height.get())
    rz.resize_images(file_dir, width, height)
    messagebox.showinfo(
        'Successful', 'All images have been resized successfully\nYou can find them inside the Resized directory')

def rename():
    rz.rename_files(file_dir)
    messagebox.showinfo(
        'Successful', 'All images have been renamed successfully')

screen = tk.Tk()
screen.geometry('300x250')
screen.title('Image Resizer')
title_frame = tk.Frame(screen)
title_frame.pack()
tk.Label(title_frame, text='Image Resizer', bg='gray',
                height='2', width='300', font=('Calibri,13')).pack()
frame1 = tk.Frame(screen)
frame1.pack()

tk.Label(frame1, text='Select the folder containing the images',
             font=('Calibri, 10')).pack()
btn = tk.Button(frame1, text='Browse', fg='white', bg='black',
                    width='8', command = browse_button)
btn.pack()

frame2 = tk.Frame(screen)
frame2.pack()
frame3 = tk.Frame(screen)
frame3.pack()
frame4 = tk.Frame(screen)
frame4.pack()

input_height = StringVar()
input_width = StringVar()

tk.Label(frame2, text=' ').pack()

tk.Label(frame2, text='Height: ').pack(side='left')
tk.Entry(frame2, textvariable = input_height).pack(side='right')

tk.Label(frame3, text=' ').pack()

tk.Label(frame3, text='Width: ').pack(side='left')
tk.Entry(frame3, textvariable = input_width).pack(side='right')

tk.Label(frame4, text=' ').pack()
    
height = input_height.get()
width = input_width.get()
    
tk.Button(frame4, text='Rename', fg='white', bg='black',
              width='8', command = rename).pack(side = 'left')

tk.Label(frame4, text='             ').pack(side = 'left')

tk.Button(frame4, text='Resize', fg='white', bg='black',
            width='8', command = resize).pack(side = 'right')

screen.mainloop()
