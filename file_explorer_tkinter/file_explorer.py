from tkinter import filedialog
from tkinter import * # type: ignore

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Text files", "*.txt*"),("all files", "*.*")))

    label_file_explorer.configure(text="File Opened: "+filename)

root = Tk()
root.title('File Explorer')
root.geometry("500x500")
root.config(background="white")

label_file_explorer = Label(root, text="File explorer using Tkinter", width=100, height=4, fg="blue")

button = Button(root, text="Browse Files", command = browseFiles)

button_exit = Button(root, text="Exit", command=exit)

label_file_explorer.grid(column = 1, row = 1)
 
button.grid(column = 1, row = 2)
 
button_exit.grid(column = 1,row = 3)
 
# Let the window wait for any events
root.mainloop()