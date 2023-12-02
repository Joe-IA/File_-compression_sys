from tkinter import *
from tkinter import filedialog, messagebox
from Main import *



encoding = Encoding()

opciones = ["Texto .txt", "Imagen .bmp", "Audio .wav", "Video .mp4"]


"""
    Functions

    In this section all the functions that are called by the widgets are declared.

    browseFile: 
        This function opens a file dialog and saves the name of the file in the entry widget.

    browseDir: 
        This function opens a directory dialog and saves the name of the directory in the entry widget.

    compress: 
        This function calls the compress methods from the Compresion class depending on the file type selected. 

    decompress: 
        This function calls the decompress methods from the Compresion class depending on the file type selected.

"""
def browseFile():
    filename = filedialog.askopenfilename()
    if filename != "" :
        name = filename.split("/")[-1]
        entryfile.delete(0, END)
        entryfile.insert(0, name)
        File.set(name.split(".")[0])
        print(File.get())
    else:
        messagebox.showerror("No file", "The file was not correctly uploaded")

def browseDir():
    directory = filedialog.askdirectory()
    if directory != "":
        name = "/".join(directory.split("/")[-3:])
        entrydir.delete(0, END)
        entrydir.insert(0, name)
        Directory.set(directory)
        print(Directory.get())
    else:
        messagebox.showerror("No directory", "The directory was not correctly uploaded")


def compress():
    try:
        if File_Type.get() == "Texto .txt":
            Compresion.compress_text(Directory.get(), File.get(), encoding)
        elif File_Type.get() == "Imagen .bmp":
             Compresion.compress_image(Directory.get(), File.get(), encoding)
        elif File_Type.get() == "Audio .wav":
            Compresion.compress_audio(Directory.get(), File.get(), encoding)
        elif File_Type.get() == "Video .mp4":
            Compresion.compress_video(Directory.get(), File.get(), encoding)
        messagebox.showinfo("Success", "The file was compressed correctly")
    except Exception as e:
        messagebox.showerror("Error", "The file was not compressed correctly.\nPlease try again.")
        print(e)
        

def decompress():
    try:
        if File_Type.get() == "Texto .txt":
            Compresion.decompress_text(Directory.get(), File.get(), encoding)
        elif File_Type.get() == "Imagen .bmp":
            Compresion.decompress_image(Directory.get(), File.get(), encoding)
        elif File_Type.get() == "Audio .wav":
            Compresion.decompress_audio(Directory.get(), File.get(), encoding)
        elif File_Type.get() == "Video .mp4":
            Compresion.decompress_video(Directory.get(), File.get(), encoding)
        messagebox.showinfo("Success", "The file was decompressed correctly")
    except Exception as e:
        messagebox.showerror("Error", "The file was not decompressed correctly.\nPlease try again.")
        print(e)


"""
    GUI
    In this section all the variables and widgets are declared and placed in the window. In runs within a loop that keeps the window open until the user closes it.

"""
root = Tk()
root.title("File Compressor")
root.geometry("480x200")

File = StringVar()
Directory = StringVar()
File_Type = StringVar(root)
File_Type.set(opciones[0])

menu = Menu(root)
root.config(menu=menu)

title_label = Label(root, text="File Compressor", font=("Helvetica", 20))
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

labelfile = Label(root, text="Select file")
labelfile.grid(row=1, column=0, padx=10, pady=10)
entryfile = Entry(root, width=50)
entryfile.grid(row=1, column=1, padx=10, pady=10)

button = Button(root, text="Browse", command=browseFile)
button.grid(row=1, column=2, padx=10, pady=10)

labeldir = Label(root, text="Directory")
labeldir.grid(row=2, column=0, padx=10, pady=10)
entrydir = Entry(root, width=50)
entrydir.grid(row=2, column=1, padx=10, pady=10)


buttondir = Button(root, text="Browse", command=browseDir)
buttondir.grid(row=2, column=2, padx=10, pady=10)

button_frame = Frame(root)
button_frame.grid(row=3, column=0, padx=10, pady=10, columnspan=3)


buttoncomp = Button(button_frame, text="Compress", command=compress)
buttoncomp.grid(row=0, column=0, padx=10, pady=5)

buttondecomp = Button(button_frame, text="Decompress", command=decompress)
buttondecomp.grid(row=0, column=1, padx=10, pady=5)

select = OptionMenu(button_frame, File_Type, *opciones)
select.grid(row=0, column=2, padx=10, pady=5)


root.mainloop()