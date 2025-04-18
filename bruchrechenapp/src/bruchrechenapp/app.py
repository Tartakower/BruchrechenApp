"""
Eine App zum Rechnen mit Brüchen
"""

import toga
from toga.style.pack import Pack

from bruchrechenapp.bruch import Bruch
from bruchrechenapp.operator import Operator

class BruchrechenApp(toga.App):
    def startup(self):
        
        COLUMN = "column"
        ROW = "row"

        main_box = toga.Box(style=Pack(direction='column', align_items='center'))

        row_box = toga.Box(style=Pack(direction='row'), align_items='center', margin=50)

        zaehler_1 = toga.TextInput(style=Pack(width=40, text_align="center", margin=5))
        nenner_1 = toga.TextInput(style=Pack(width=40, text_align="center", margin=5))
        box_1 = toga.Box(style=Pack(direction='column'), align_items='center', margin=10)
        box_1.add(zaehler_1)
        box_1.add(nenner_1)

        auswahl = toga.Selection(items=['+','-','*',':'])
        box_2 = toga.Box(style=Pack(direction='column'), align_items='center', margin=10)
        box_2.add(auswahl)

        zaehler_2 = toga.TextInput(style=Pack(width=40, text_align="center", margin=5))
        nenner_2 = toga.TextInput(style=Pack(width=40, text_align="center", margin=5))
        box_3 = toga.Box(style=Pack(direction='column'), align_items='center', margin=10)
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

        rechnen_button = toga.Button("=", on_press=berechne, style=Pack(margin=5))
        box_4 = toga.Box(style=Pack(direction='column'), align_items='center', margin=10)
        box_4.add(rechnen_button)

        zaehler_res = toga.TextInput(style=Pack(width=40, text_align="center", margin=5))
        nenner_res = toga.TextInput(style=Pack(width=40, text_align="center", margin=5))
        box_5 = toga.Box(style=Pack(direction='column'), align_items='center', margin=10)
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

        clear_button = toga.Button("Löschen", on_press=loesche, style=Pack(margin=5))

        main_box.add(row_box)
        main_box.add(clear_button)

        # beispiel_box = toga.Box(style=Pack(direction=ROW, margin=20))
        # beispiel_operand_1 = toga.Box(style=Pack(direction=COLUMN))
        # beispiel_operand_1.add(toga.Label("1"))
        # beispiel_operand_1.add(toga.Label("-"))
        # beispiel_operand_1.add(toga.Label("2"))
        # beispiel_box.add(beispiel_operand_1)
        # beispiel_box.add(toga.Label("*", style=Pack(margin=20)))
        # beispiel_operand_2 = toga.Box(style=Pack(direction=COLUMN))
        # beispiel_operand_2.add(toga.Label("2"))
        # beispiel_operand_2.add(toga.Label("-"))
        # beispiel_operand_2.add(toga.Label("3"))
        # beispiel_box.add(beispiel_operand_2)

        # bsp_ergebnis_zaehler = toga.TextInput(readonly=True, style=Pack(width=40,text_align="center"))
        # bsp_ergebnis_nenner = toga.TextInput(readonly=True, style=Pack(width=40,text_align="center"))
        # def calculate(widget):
        #     try:
        #         op: Operator = Operator('*')
        #         b = op.berechne(Bruch(1,2), Bruch(2,3))
        #         bsp_ergebnis_zaehler.value = b.zaehler
        #         bsp_ergebnis_nenner.value = b.nenner
        #     except ValueError:
        #         bsp_ergebnis_zaehler.value = "?"
        #         bsp_ergebnis_nenner.value = "?"

        # berechnen = toga.Button("=", on_press=calculate, style=Pack(margin=20))
        # beispiel_box.add(berechnen)

        # beispiel_ergebnis = toga.Box(style=Pack(direction=COLUMN))
        # beispiel_ergebnis.add(bsp_ergebnis_zaehler)
        # beispiel_ergebnis.add(toga.Label("-"))
        # beispiel_ergebnis.add(bsp_ergebnis_nenner)
        # beispiel_box.add(beispiel_ergebnis)

        # zaehler_1 = toga.TextInput(style=Pack(width=40,text_align="center"))
        # nenner_1 = toga.TextInput(style=Pack(width=40,text_align="center"))
        # eingabe_bruch_1 = toga.Box(style=Pack(direction=COLUMN), margin=20)
        # eingabe_bruch_1.add(zaehler_1)
        # eingabe_bruch_1.add(toga.Label(" "))
        # eingabe_bruch_1.add(nenner_1)

        # eingabe_box = toga.Box(style=Pack(direction=ROW), margin=(20, 20))
        # eingabe_box.add(eingabe_bruch_1)

        # auswahl = toga.Selection(items=['+','-','*',':'])
        # auswahl_box = toga.Box(style=Pack(direction='column', margin=20, align_items="end"))
        # auswahl_box.add(auswahl)
        # eingabe_box.add(auswahl_box)

        # zaehler_2 = toga.TextInput(style=Pack(width=40,text_align="center"))
        # nenner_2 = toga.TextInput(style=Pack(width=40,text_align="center"))
        # eingabe_bruch_2 = toga.Box(style=Pack(direction=COLUMN), margin=20)
        # eingabe_bruch_2.add(zaehler_2)
        # eingabe_bruch_2.add(toga.Label(" "))
        # eingabe_bruch_2.add(nenner_2)
        # eingabe_box.add(eingabe_bruch_2)

        # main_box.add(beispiel_box)
        # main_box.add(eingabe_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return BruchrechenApp()
