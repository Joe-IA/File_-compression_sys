from tkinter import *
from tkinter import filedialog, messagebox
from Main import Encoding
import json
import pickle
from bitarray import bitarray
encoding = Encoding()


def browseFile():
    filename = filedialog.askopenfilename()
    if filename != "" :
        name = filename.split("/")[-1]
        entryfile.delete(0, END)
        entryfile.insert(0, name)
        File.set(name.split(".")[0])
        print(File.get())   
        with open(filename, "r") as f:
            text.set(f.read())
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
        encoded_text, tree_code_table = encoding.adaptive_huffman_encoding(text.get())
        bits = bitarray()
        bits = bitarray([int(i) & 1 for i in encoded_text])
        with open(f"{Directory.get()}/{File.get()}.bin", "wb") as bf:
            pickle.dump((tree_code_table, bits), bf)
        messagebox.showinfo("Success", "The file was compressed correctly")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "The file was not compressed correctly.\nPlease try again.")
        
def decompress():
    try:
        with open(f"{Directory.get()}/{File.get()}.bin", "rb") as bf:
            tree_code_table, bits = pickle.load(bf)
        decoded_text = encoding.decode(bits.to01(), tree_code_table)
        with open(f"{Directory.get()}/{File.get()}.txt", "w") as f:
            f.write(decoded_text)
        messagebox.showinfo("Success", "The file was decompressed correctly")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "The file was not decompressed correctly.\nPlease try again.")

root = Tk()
root.title("File Compressor")
root.geometry("480x200")

File = StringVar()
Directory = StringVar()
text = StringVar()

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


root.mainloop()