import tkinter as tk

time = 100
score = 0
press_enter = True

window = tk.Tk()
window.geometry("600x600+600+100")
window.resizable(False, False)
window.title("3311 - Game")
window.iconbitmap('pics/bomb.ico')


label = tk.Label(text="Для початку гри натисніть [ENTER]", font=('Comic Sans MS', 12, 'bold'))
label.pack()

label_time = tk.Label(text=f'Залишок часу {time}', font=('Comic Sans MS', 16, 'bold'))
label_time.pack()

label_score = tk.Label(text=f'Набрані бали {score}', font=('Comic Sans MS', 16, 'bold'))
label_score.pack()

img1 = tk.PhotoImage(file='pics/1.gif')
img2 = tk.PhotoImage(file='pics/2.gif')
img3 = tk.PhotoImage(file='pics/3.gif')
img4 = tk.PhotoImage(file='pics/4.gif')

label_bomb = tk.Label(image=img1)
label_bomb.pack()


def click():
    pass


button = tk.Button(text='Тикай сюди', font=('Comic Sans MS', 16, 'bold'), bg='black', fg='white', command=click)
button.pack()


window.mainloop()