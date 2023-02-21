'''
class Control:
    def __init__(self):
       
        self.combo = ttk.Combobox(
            self.frm_emblem,
            values = self.Cv.names_sp,
            font = 'Times 14',
            state = 'readonly'
            )

#   ----- Resourses -----
    def resourses_panel(self):
        self.img_food = tk.PhotoImage(file=self.img.icon_food)
        self.img_wood = tk.PhotoImage(file=self.img.icon_wood)
        self.img_stone = tk.PhotoImage(file=self.img.icon_stone)
        self.img_metal = tk.PhotoImage(file=self.img.icon_metal)
        self.img_population = tk.PhotoImage(file=self.img.icon_population)
        self.img_time = tk.PhotoImage(file=self.img.icon_time)
        self.frm_resources = tk.Frame(
            self.root,
            background=self.col.golden,
            bd=2
        )
        self.frm_resources.pack(side='top', anchor='w')
        self.lbl_food = tk.Label(
            self.frm_resources,
            image=self.img_food,
            text='Food',
            font='Castellar 10',
            bg=self.dark,
            fg=self.high_golden,
            compound='bottom'
        ).pack(side='left')
        self.lbl_wood = tk.Label(
            self.frm_resources,
            image=self.img_wood,
            text='Wood',
            font='Castellar 10',
            bg=self.dark,
            fg=self.high_golden,
            compound='bottom'
        ).pack(side='left')
        self.lbl_stone = tk.Label(
            self.frm_resources,
            image=self.img_stone,
            text='Stone',
            font='Castellar 10',
            bg=self.dark,
            fg=self.high_golden,
            compound='bottom'
        ).pack(side='left')
        self.lbl_metal = tk.Label(
            self.frm_resources,
            image=self.img_metal,
            text='Metal',
            font='Castellar 10',
            bg=self.dark,
            fg=self.high_golden,
            compound='bottom'
        ).pack(side='left')
        self.lbl_population = tk.Label(
            self.frm_resources,
            image=self.img_population,
            text='Population',
            font='Castellar 10',
            bg=self.dark,
            fg=self.high_golden,
            compound='bottom'
        ).pack(side='left')
        self.lbl_time = tk.Label(
            self.frm_resources,
            image=self.img_time,
            text='Time',
            font='Castellar 10',
            bg=self.dark,
            fg=self.high_golden,
            compound='bottom'
        ).pack(side='left')

#   ----- Emblems Panel -----
    def show_emblem(self, civname):
        self.btn_close.place(x=4,y=4)
        self.frm_emblem.place(x=self.w/2-102, y=26)
        self.can_emblem.create_image(0, 0, image=self.img.background)
        self.can_emblem.create_image(0, 3, image=self.img.border_hor)
        self.can_emblem.create_image(3, 0, image=self.img.border_ver)
        self.can_emblem.create_image(0, 147, image=self.img.border_hor)
        self.can_emblem.create_image(207, 0, image=self.img.border_ver)
        self.combo.pack(side='bottom',expand=False, fill='x', anchor='n')
        self.can_emblem.pack()
        self.btn_prev_emblem.pack(side='left', anchor='s')
        self.btn_next_emblem.pack(side='right', anchor='s')
        #self.btn_open_emblem.configure(command=lambda:self.show_emblem(civname))
        for i, c in enumerate(self.Cv.group):
            if civname == c.name or civname == c.name_sp:
                civ_id = i
                img_emblem = tk.PhotoImage(file=c.emblem)
                print(f"Emblema en pantalla: {civ_id} {civname} {self.Cv.group[civ_id].emblem}")
                self.btn_next_emblem.config(comman=lambda:self.next_emblem(civ_id))
                self.btn_prev_emblem.config(comman=lambda:self.prev_emblem(civ_id))
                tk.Canvas().create_image(
                    102,
                    72,
                    image = img_emblem
                )
                lbl_emblem = tk.Label(
                    self.frm_emblem,
                    text = f'{c.name_sp}',
                    background = self.col.high_guinda,
                    foreground = self.col.silver,
                    font = 'Times 13',
                    relief = 'raised',
                    border = 2,
                    pady = 2,
                    name = 'lbl_emblem'
                )
                lbl_emblem.pack(side='bottom', expand=True, fill='x', anchor='n')

    def prev_emblem(self, civ_id):
        if civ_id == 0:
            civ_id = 14
            civname = self.Cv.group[civ_id].name
            print(f"p1.- Anterior emblema: {civ_id} {civname}")
            self.show_emblem(civname)
            self.btn_open_emblem.configure(command=lambda:self.show_emblem(civname))
        elif civ_id >= 0:
            civ_id -= 1
            civname = self.Cv.group[civ_id].name
            print(f"p2.- Anterior emblema: {civ_id} {civname}")
            self.show_emblem(civname)
            self.btn_open_emblem.configure(command=lambda:self.show_emblem(civname))
 

    def next_emblem(self, civ_id):
        if civ_id == 14:
            civ_id = 0
            civname = self.Cv.group[civ_id].name
            print(f"n2.- Siguiente emblema: {civ_id} {civname}")
            self.show_emblem(civname)
            self.btn_open_emblem.configure(command=lambda:self.show_emblem(civname))
        elif civ_id <= 14:
            civ_id += 1
            civname = self.Cv.group[civ_id].name
            print(f"n1.- Siguiente emblema: {civ_id} {civname}")
            self.show_emblem(civname)
            self.btn_open_emblem.configure(command=lambda:self.show_emblem(civname))


    def hide_emblem(self):
        self.frm_emblem.place_forget()
        self.btn_close.place_forget()

        self.btn_open_emblem = tk.Button(
            self.frm_tool_bar,
            text = "Civilizaciones",
            command = self.show_emblem,
            background = self.col.golden,
            foreground = self.col.silver,
            font = 'Times 11',
            width = 12,
            height = 1,
            cursor = 'hand2',
            activebackground = self.col.dark_golden,
            activeforeground = self.col.white,
            relief = 'raised',
            overrelief = 'groove',
            border = 1
        )

        self.btn_prev_emblem = tk.Button(
            self.frm_emblem,
            image = self.img.left_arrow,
            command = self.prev_emblem,
            background = self.col.golden,
            height = 23,
            cursor = 'hand2',
            activebackground = self.col.guinda,
            relief = 'raised',
            overrelief = 'sunken'
        )

        self.btn_next_emblem = tk.Button(
            self.frm_emblem,
            image = self.img.right_arrow,
            command = self.next_emblem,
            background = self.col.golden,
            height = 23,
            cursor = 'hand2',
            activebackground = self.col.guinda,
            relief = 'raised',
            overrelief = 'sunken'
        )

        self.btn_close = tk.Button(
            self.frm_emblem,
            text = 'X',
            command = self.hide_emblem,
            background = self.col.guinda,
            foreground = self.col.silver,
            font = 'Times 11',
            width = 3,
            height = 1,
            cursor = 'hand2',
            activebackground = self.col.dark_guinda,
            activeforeground = self.col.guinda,
            overrelief = 'raised',
            relief = 'groove',
            border=2
        )
        self.btn_exit = tk.Button(
            self.frm_tool_bar,
            text = 'Salir',
            command = self.root.destroy,
            background = self.col.high_guinda,
            foreground = self.col.silver,
            font = 'Times 11',
            width = 5,
            height = 1,
            cursor = 'hand2',
            activebackground = self.col.dark_guinda,
            activeforeground = self.col.high_guinda,
            overrelief = 'groove',
            relief = 'raised',
            border = 1
        )
'''