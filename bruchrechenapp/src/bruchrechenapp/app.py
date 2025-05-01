"""
Eine App zum Rechnen mit Brüchen
"""

import toga
from toga.style.pack import Pack

from bruchrechenapp.bruch import Bruch
from bruchrechenapp.operation import Operator

class BruchrechenApp(toga.App):

    def __init__(self, formal_name: str | None = None, app_id: str | None = None, app_name: str | None = None):
        super().__init__(formal_name, app_id, app_name)
        self.zaehler_1 = createTextInput()
        self.nenner_1 = createTextInput()
        self.auswahl = toga.Selection(items=['+','-','*',':'], style=Pack(font_size=16))
        self.zaehler_2 = createTextInput()
        self.nenner_2 = createTextInput()
        self.zaehler_res = createTextInput()
        self.nenner_res = createTextInput()

    def startup(self):
        
        main_box = toga.Box(style=Pack(direction='column', alignment='center'))

        row_box = toga.Box(style=Pack(direction='row', alignment='center', padding=10))

        box_1 = toga.Box(style=Pack(direction='column', alignment='center', padding=10, flex=0.2))
        box_1.add(self.zaehler_1)
        box_1.add(toga.Divider(direction=0, style=Pack(height=5, background_color='black')))
        box_1.add(self.nenner_1)
        
        box_2 = toga.Box(style=Pack(direction='column',  alignment='center',padding=10))
        box_2.add(self.auswahl)

        box_3 = toga.Box(style=Pack(direction='column',  alignment='center',padding=10, flex=0.2))
        box_3.add(self.zaehler_2)
        box_3.add(toga.Divider(direction=0, style=Pack(height=5, background_color='black')))
        box_3.add(self.nenner_2)

        rechnen_button = toga.Button(text="=", on_press=self.berechne, style=Pack(padding=5, font_size=16))
        box_4 = toga.Box(style=Pack(direction='column',  alignment='center',padding=10))
        box_4.add(rechnen_button)

        box_5 = toga.Box(style=Pack(direction='column',  alignment='center', padding=10, flex=0.2))
        box_5.add(self.zaehler_res)
        box_5.add(toga.Divider(direction=0, style=Pack(height=5, background_color='black')))
        box_5.add(self.nenner_res)

        row_box.add(box_1)
        row_box.add(box_2)
        row_box.add(box_3)
        row_box.add(box_4)
        row_box.add(box_5)

        clear_button = toga.Button(text="Neue Aufgabe", on_press=self.loesche, style=Pack(width=180, padding=5, font_size=16))

        main_box.add(row_box)
        main_box.add(clear_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def berechne(self, button: toga.Button):
        try:
            op = Operator(self.auswahl.value)
            b1 = Bruch(int(self.zaehler_1.value), int(self.nenner_1.value))
            b2 = Bruch(int(self.zaehler_2.value), int(self.nenner_2.value))
            b = op.berechne(b1, b2)
            self.zaehler_res.value = b.zaehler
            self.nenner_res.value = b.nenner
        except ValueError:
            self.zaehler_res.value = '?'
            self.nenner_res.value = '?'

    def loesche(self, button: toga.Button):
        self.zaehler_1.value = ''
        self.nenner_1.value = ''
        self.zaehler_2.value = ''
        self.nenner_2.value = ''
        self.zaehler_res.value = ''
        self.nenner_res.value = ''

def createTextInput() -> toga.TextInput:
    return toga.TextInput(style=Pack(width=60, text_align="center", padding=5, font_size=16, background_color='yellow'))

def main():
    return BruchrechenApp()
