import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file(e=None):
    file_name = filedialog.askopenfilename(title='3311 - Open file', defaultextension='txt', filetypes=(('Text files', '*.txt'),('All files', '*.*')))
    if file_name != '':
        f = open(file_name, 'r', encoding='utf-8')
        txt = f.read()
        if txt != None:
            text.delete('1.0', 'end')
            text.insert('end', txt)
            window.title(f"3311 - TextEditor - {file_name}")


def save_file(e=None):
    file_name = filedialog.asksaveasfilename(title='3311 - Save file', defaultextension='txt', filetypes=(('Text files', '*.txt'),('All files', '*.*')))
    if file_name != '':
        f = open(file_name, 'w', encoding='utf-8')
        txt = text.get('1.0', 'end')
        f.write(txt)
        window.title(f"3311 - TextEditor - {file_name}")
        messagebox.showinfo('3311 - TextEditor', 'File saved!')

def new_file(e=None):
    window.title(f"3311 - TextEditor")
    text.delete('1.0', 'end')

window = tk.Tk()

window.title("3311 - TextEditor")
window.geometry("600x400+600+200")

img1 = tk.PhotoImage(file='folder-open-custom.png')
img2 = tk.PhotoImage(file='content-save-custom.png')


menu = tk.Menu()
window.config(menu=menu)

file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file, image=img1, compound='left', accelerator='Ctrl-O')
file_menu.add_command(label='Save As..', command=save_file, image=img2, compound='left', accelerator='Ctrl-S')
file_menu.add_separator()
file_menu.add_command(label='Exit')

menu.add_cascade(label='File', menu=file_menu)







text = tk.Text()
text.pack(fill='both', expand=1)

window.bind('<Control-o>', open_file)
window.bind('<Control-s>', save_file)

window.mainloop()