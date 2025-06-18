import flet as ft
from flet_core import MainAxisAlignment

import controller
from controller import SpellChecker

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.dd_mode = ft.Dropdown(label="Mode", on_change=self.dropdown_changed)
        self.modality = "Default"
        self.dd_lang = ft.Dropdown(label="Language", on_change=self.dropdown_lang_changed)
        self.lang = None
        self.tf = ft.TextField(label= "Testo")
        self.btnTraduci = ft.ElevatedButton(text="Traduci!", on_click= lambda e: self.handle_translate())
        self.sc = SpellChecker(self)

        self.tempo = None
        self.lvOut = None
        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment= MainAxisAlignment.SPACE_EVENLY)
        )

        # Add your stuff here
        op1 = ft.dropdown.Option(key= "Default", text= "Default")
        op2 = ft.dropdown.Option(key= "Linear", text= "Linear")
        op3 = ft.dropdown.Option(key= "Dichotomic", text= "Dichotomic")

        op11 = ft.dropdown.Option(key="italian", text="Italian")
        op22 = ft.dropdown.Option(key="english", text="English")
        op33 = ft.dropdown.Option(key="spanish", text="Spanish")

        for op in [op1, op2, op3]:
            self.dd_mode.options.append(op)

        for op in [op11, op22, op33]:
            self.dd_lang.options.append(op)

        row1 = ft.Row(controls= [self.dd_mode, self.dd_lang], alignment= MainAxisAlignment.SPACE_EVENLY)
        row2 = ft.Row(controls= [self.tf, self.btnTraduci], alignment= MainAxisAlignment.SPACE_EVENLY)

        self.page.add(row1, row2)

        self.update()


    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def handle_translate(self):
        result = self.sc.handleSentence(self.tf.value, self.lang, self.modality)
        print(result)

    def dropdown_changed(self, e):
        self.modality = e.control.value
        print(self.modality)

    def dropdown_lang_changed(self, e):
        self.lang = e.control.value
        print(self.lang)

    def add_output(self, tempo, errate):
        if tempo is None or errate is None:
            return
        if self.lvOut is not None:
            self.page.controls.remove(self.lvOut)
        if self.tempo is not None:
            self.page.controls.remove(self.tempo)

        self.tempo = ft.Text(f"il processo ha impiegato: {tempo}")
        self.lvOut = ft.ListView()
        for err in errate:
            self.lvOut.controls.append(ft.Text(f"{err}"),)
        self.page.controls.append(self.tempo)
        self.page.controls.append(self.lvOut)
        self.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()
