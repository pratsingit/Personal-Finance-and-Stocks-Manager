import tkinter as tk

path = "A:\\Final_Project\\dashboard_page\\"

class dashboard(tk.Frame) :
    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg='#093545')
        
        global img0, img1, img2, img3, img4, img5, img6, background_img
        
        self.controller = controller
        
        background_img = tk.PhotoImage (file =path + "dashboard0.png")
        
        bck_label = tk.Label(self, image=background_img,
                             relief="flat", bg="#093545")
        
        bck_label.place(x=0, y=0, width=1537, height=864)
        
        img0 = tk.PhotoImage(file = path + "dashboard1.png")
        
        def b0_clicked(): # Update Earnings
            print("Button Clicked")
        
        b0 = tk.Button(self,
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=b0_clicked,
            cursor="hand2",
            relief="flat")

        b0.place(
            x=47, y=202,
            width=290,
            height=49)
        
        img1 = tk.PhotoImage(file = path + "dashboard2.png")
        
        def b1_clicked(): # View Accounts
            print("Button Clicked")

        b1 = tk.Button(self,
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=b1_clicked,
            cursor="hand2",
            relief="flat")

        b1.place(
            x=47, y=120,
            width=290,
            height=49)
        
        img2 = tk.PhotoImage(file = path + "dashboard3.png")
        
        def b2_clicked(): # Update Investments
            print("Button Clicked")
        
        b2 = tk.Button(self,
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=b2_clicked,
            cursor="hand2",
            relief="flat")

        b2.place(
            x=47, y=368,
            width=290,
            height=49)
        
        img3 = tk.PhotoImage(file = path + "dashboard4.png")
        
        def b3_clicked(): # Browse new Investments
            print("Button Clicked")
        
        b3 = tk.Button( self,
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=b3_clicked,
            cursor="hand2",
            relief="flat")

        b3.place(
            x=47, y=451,
            width=290,
            height=93)
        
        img4 = tk.PhotoImage(file=path + "dashboard5.png")

        def b4_clicked(): # Riview Expenditure
            print ("Button Clicked")
            
        b4 = tk.Button(self,
            image=img4,
            bg = "#000000",
            borderwidth=0,
            highlightthickness=0,
            command=b4_clicked,
            cursor="hand2",
            relief="flat")

        b4.place(
            x=47, y=285,
            width=290,
            height=49)
        
        img5 = tk.PhotoImage(file= path + "dashboard6.png")
        
        def b5_clicked(): # Liability Details
            print("Button Clicked")

        b5 = tk.Button(self,
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            command=b5_clicked,
            cursor="hand2",
            relief="flat")

        b5.place(
            x=47, y=578,
            width=290,
            height=49)

        img6 = tk.PhotoImage(file= path + "dashboard7.png")
        
        def b6_clicked(): # logout
            controller.show_frame("login")
        
        b6 = tk.Button(self,
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=b6_clicked,
            cursor="hand2",
            relief="flat")

        b6.place(
            x=47, y=661,
            width=290,
            height=49)
        