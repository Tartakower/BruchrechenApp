"""
Eine App zum Rechnen mit Brüchen
"""

import toga
from toga.style.pack import Pack

from bruchrechenapp.bruch import Bruch
from bruchrechenapp.operator import Operator

class BruchrechenApp(toga.App):
    def startup(self):
        
        main_box = toga.Box(style=Pack(direction='column', alignment='center'))

        row_box = toga.Box(style=Pack(direction='row', alignment='center', padding=10))

        zaehler_1 = createTextInput()
        nenner_1 = createTextInput()
        box_1 = toga.Box(style=Pack(direction='column', padding=10))
        box_1.add(zaehler_1)
        box_1.add(nenner_1)

        auswahl = toga.Selection(items=['+','-','*',':'], style=Pack(font_size=16))
        box_2 = toga.Box(style=Pack(direction='column', padding=10))
        box_2.add(auswahl)

        zaehler_2 = createTextInput()
        nenner_2 = createTextInput()
        box_3 = toga.Box(style=Pack(direction='column', padding=10))
        box_3.add(zaehler_2)
        box_3.add(nenner_2)

        def berechne(rechen_button):
            try:
                op = Operator(auswahl.value)
                b1 = Bruch(int(zaehler_1.value), int(nenner_1.value))
                b2 = Bruch(int(zaehler_2.value), int(nenner_2.value))
                b = op.berechne(b1, b2)
                zaehler_res.value = b.zaehler
                nenner_res.value = b.nenner
            except ValueError:
                zaehler_res.value = '?'
                nenner_res.value = '?'

        rechnen_button = toga.Button("=", on_press=berechne, style=Pack(padding=5, font_size=16))
        box_4 = toga.Box(style=Pack(direction='column', padding=10))
        box_4.add(rechnen_button)

        zaehler_res = createTextInput()
        nenner_res = createTextInput()
        box_5 = toga.Box(style=Pack(direction='column', padding=10))
        box_5.add(zaehler_res)
        box_5.add(nenner_res)

        row_box.add(box_1)
        row_box.add(box_2)
        row_box.add(box_3)
        row_box.add(box_4)
        row_box.add(box_5)

        def loesche(widget):
            zaehler_1.value = ''
            nenner_1.value = ''
            zaehler_2.value = ''
            nenner_2.value = ''
            zaehler_res.value = ''
            nenner_res.value = ''

        clear_button = toga.Button("Neue Aufgabe", on_press=loesche, style=Pack(width=180, padding=5, font_size=16))

        main_box.add(row_box)
        main_box.add(clear_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def createTextInput() -> toga.TextInput:
    return toga.TextInput(style=Pack(width=60, text_align="center", padding=5, font_size=16))

def main():
    return BruchrechenApp()
