from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#093545")
canvas = Canvas(
    window,
    bg = "#093545",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    374.5, 372.0,
    image = entry0_img)

entry0_font = ("Lexend Deca", 20)
entry0 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    font = entry0_font ,
    highlightthickness = 0)


entry0.place(
    x = 144.0, y = 341,
    width = 461.0,
    height = 60)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    374.5, 554.0,
    image = entry1_img)

entry1_font = ("Lexend Deca", 20)
entry1 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    font = entry1_font,
    highlightthickness = 0)

entry1.place(
    x = 144.0, y = 523,
    width = 461.0,
    height = 60)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    374.5, 736.0,
    image = entry2_img)

entry2_font = ("Lexend Deca", 20)
entry2 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    font = entry2_font,
    highlightthickness = 0)

entry2.place(
    x = 144.0, y = 705,
    width = 461.0,
    height = 60)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 550, y = 841,
    width = 266,
    height = 62)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    1040.5, 368.0,
    image = entry3_img)

entry3_font = ("Lexend Deca", 20)
entry3 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    font = entry3_font,
    highlightthickness = 0)

entry3.place(
    x = 810.0, y = 337,
    width = 461.0,
    height = 60)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    1038.5, 550.0,
    image = entry4_img)

entry4_font = ("Lexend Deca", 20)
entry4 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    font = entry4_font,
    highlightthickness = 0)

entry4.place(
    x = 808.0, y = 519,
    width = 461.0,
    height = 60)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    1038.5, 732.0,
    image = entry5_img)

entry5_font = ("Lexend Deca", 20)
entry5 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    font = entry5_font,
    highlightthickness = 0)

entry5.place(
    x = 808.0, y = 701,
    width = 461.0,
    height = 60)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    1133.0, 364.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
