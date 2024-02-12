from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1920x1080")
window.configure(bg="#093545")
canvas = Canvas(
    window,
    bg="#093545",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=158, y=657,
    width=481,
    height=62)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    399.5, 489.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#224957",
    fg="white",  # set foreground color to white
    highlightthickness=0)

entry0.place(
    x=169.0, y=458,
    width=461.0,
    height=60)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    397.5, 579.0,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#224957",
    fg="white",  # set foreground color to white
    highlightthickness=0)

entry1.place(
    x=167.0, y=548,
    width=461.0,
    height=60)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    960.0, 540.0,
    image=background_img)

window.resizable(True, True)
window.mainloop()
