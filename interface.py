import tkinter as tk
from tkinter import ttk


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.w, self.h))
        self.sty = ttk.Style()
        self.root.option_add('*TCombobox*Listbox*Background', Colors().guinda)
        self.root.option_add('*TCombobox*Listbox*Foreground', Colors().white)
        self.root.option_add('*TCombobox*Listbox*selectBackground', Colors().high_guinda)
        self.root.option_add('*TCombobox*Listbox*selectForeground', Colors().white)
        self.sty.map('TCombobox', fieldbackground=[('readonly', Colors().guinda)])
        self.sty.map('TCombobox', selectbackground=[('readonly', Colors().guinda)])
        self.sty.map('TCombobox', selectforeground=[('readonly', Colors().golden)])
        self.sty.map('TCombobox', background=[('readonly', Colors().high_guinda)])
        self.sty.map('TCombobox', background=[('readonly', Colors().golden)])
        
        self.frm_back = tk.Frame(self.root, highlightthickness=0,border=0)
        self.lbl_bg1 = tk.Label(self.frm_back,image=Images().background,highlightthickness=0,border=0)
        self.lbl_bg2 = tk.Label(self.frm_back,image=Images().background,highlightthickness=0,border=0)
        
        self.frm_back.place(x=0,y=0,relx=0.0,rely=0.0,relwidth=1,relheight=1)
        self.lbl_bg1.pack(side='left',expand=True, fill='both')
        self.lbl_bg2.pack(side='right',expand=True,fill='both')
        self.frm_top_bar = tk.Frame(
            self.root,
            background = Colors().guinda,
            bd = 2
        )
        self.can_top_bar = tk.Canvas(
            self.frm_top_bar,
            background = Colors().guinda,
            width = self.w,
            height = 140, 
        ).configure(highlightthickness=0)       

        self.frm_tool_bar = tk.Frame(
            self.frm_top_bar,
            width = self.w,
            height = 128,
            bg = Colors().dark_guinda
        )


        self.frm_emblem = tk.Frame(
            self.root,
            bg = Colors().guinda,
            relief = 'raised',
            border=4
        )
        self.can_emblem = tk.Canvas(
            self.frm_emblem,
            background = Colors().guinda,
            width = 204, 
            height = 144,
            highlightthickness = 0,
            bd = 3,
            relief = 'raised'
        )


    def main_loop(self):
        self.root.title("Empires Ascendant")
        self.root.iconphoto(True, Images().main_icon)
        self.root.resizable(True, True)
        self.root.configure(background=Colors().golden, border=5, relief="groove")
        self.root.mainloop()
#        self.top_bar()
        

#   ----- Background -----

 #   ----- TopBar -----
    def top_bar(self):
        tk.Label(
            self.frm_top_bar,
            image = Images().border_ver,
            background = Colors().guinda,
            height = 105,
            anchor = 'e'
            ).pack(side='right')
        tk.Label(
            self.frm_top_bar,
            image = Images().border_ver,
            background = Colors().guinda,
            height = 105,
            anchor = 'w'
        ).pack(side='left')
        tk.Label(
            self.frm_top_bar,
            image = Images().border_hor,
            background = Colors().guinda,
            height = 105,
            anchor = 'n'
        ).pack(side='top')
        tk.Label(
            self.frm_top_bar,
            image = Images().border_hor,
            background = Colors().guinda,
            height = 105,
            anchor = 's'
        ).pack(side = 'bottom')
        tk.Label(
            self.frm_top_bar,
            image = Images().wildfire,
            background = Colors().guinda,
            width = 120,
            height = 90
        ).pack(side='right')
        tk.Label(
            self.frm_top_bar,
            image = Images().logo,
            background = Colors().guinda,
            height = 110,
            width = 220,
        ).pack(side='left')
#   ----- ToolBar -----
        self.frm_top_bar.pack(side='top', fill='x', expand=False)
        self.frm_tool_bar.pack(side='top', fill='x', expand=False)
        #self.btn_exit.grid(row=0,column=0, padx=5, pady=5, ipadx=2, ipady=2)
        #self.btn_open_emblem.grid(row=0,column=1, padx=25, pady=5, ipadx=2, ipady=2)







class Colors:
    def __init__(self):
#        ----- Black -----
        self.black = '#000000'
        self.dark = '#232323'
        self.carbon = '#404040'
#       ----- Red -----
        self.red = '#FF0000'
        self.dark_guinda = "#2D0200"
        self.guinda = '#5E2129'
        self.high_guinda ='#480000'
#       ----- Yellow #####
        self.yellow = '#FFFF00'
        self.high_vanilla = '#E8BE4B'
        self.vanilla = '#FFDE7B'
        self.dark_vanilla = '#B29B56'
#       ----- Gold -----
        self.dark_golden='#61501F'
        self.golden = '#947B49'
        self.high_golden = '#AC7D27'
#       ----- Metal -----
        self.silver = '#C1C3C2'
        self.white = '#FFFFFF'

class Images:
    def __init__(self):
# ----- Window -----
        self.main_icon = tk.PhotoImage(file='./images/logos/window logo.png')
        self.background = tk.PhotoImage(file='./images/gui/background.png')
        self.logo = tk.PhotoImage(file='./images/logos/A0D.png')
        self.wildfire = tk.PhotoImage(file='./images/logos/wildfire.png')
        self.border_hor = tk.PhotoImage(file='./images/gui/border_h.png')
        self.border_ver = tk.PhotoImage(file='./images/gui/border_v.png')
        self.tech_title = tk.PhotoImage(file='./images/gui/titlebar-middle.png')
        self.left_arrow = tk.PhotoImage(file='./images/gui/titlebar-left.png')
        self.right_arrow = tk.PhotoImage(file='./images/gui/titlebar-right.png')
# ----- Resources -----
        self.icon_food = tk.PhotoImage(file='./images/icons/resources/food.png')
        self.icon_wood = tk.PhotoImage(file='./images/icons/resources/wood.png')
        self.icon_stone = tk.PhotoImage(file='./images/icons/resources/stone.png')
        self.icon_metal = tk.PhotoImage(file='./images/icons/resources/metal.png')
        self.icon_population = tk.PhotoImage(file='./images/icons/resources/population.png')
        self.icon_time = tk.PhotoImage(file='./images/icons/resources/time_small.png')
        self.icon_small_food = tk.PhotoImage(file='./images/icons/resources/small_food.png')
        self.icon_small_wood = tk.PhotoImage(file='./images/icons/resources/small_wood.png')
        self.icon_small_stone = tk.PhotoImage(file='./images/icons/resources/small_stone.png')
        self.icon_small_metal = tk.PhotoImage(file='./images/icons/resources/small_metal.png')
        self.icon_small_population = tk.PhotoImage(file='./images/icons/resources/small_population.png')




Gui = Interface()

Gui.top_bar()
Gui.main_loop()
