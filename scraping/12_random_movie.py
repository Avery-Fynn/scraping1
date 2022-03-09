from tkinter import *

root = Tk()
root.title("HELLO GUI")
root.geometry("640x480")  # 가로 * 세로


def change():
    photo2 = PhotoImage(
        file="/Users/gwonminjeong/Desktop/merge/web/movie_2015_3.jpg")
    label1 = Label(root, image=photo2)
    label1.pack()


photo = PhotoImage(file="gui_basic/icon.png")
label2 = Label(root, image=photo)
label2.pack()


btn = Button(root, text="안녕?", command=change)
btn.pack()


root.mainloop()
