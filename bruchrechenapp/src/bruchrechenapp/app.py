"""
Eine App zum Rechnen mit Brüchen
"""

import toga
from toga.style.pack import Pack


class BruchrechenApp(toga.App):
    def startup(self):
        
        COLUMN = "column"
        ROW = "row"

        main_box = toga.Box(style=Pack(direction=COLUMN))

        beispiel_box = toga.Box(style=Pack(direction=ROW, margin=20))
        beispiel_operand_1 = toga.Box(style=Pack(direction=COLUMN))
        beispiel_operand_1.add(toga.Label("1"))
        beispiel_operand_1.add(toga.Label("-"))
        beispiel_operand_1.add(toga.Label("2"))
        beispiel_box.add(beispiel_operand_1)
        beispiel_box.add(toga.Label("*", style=Pack(margin=20)))
        beispiel_operand_2 = toga.Box(style=Pack(direction=COLUMN))
        beispiel_operand_2.add(toga.Label("2"))
        beispiel_operand_2.add(toga.Label("-"))
        beispiel_operand_2.add(toga.Label("3"))
        beispiel_box.add(beispiel_operand_2)
        beispiel_box.add(toga.Label("=", style=Pack(margin=20)))
        beispiel_ergebnis = toga.Box(style=Pack(direction=COLUMN))
        beispiel_ergebnis.add(toga.Label("1"))
        beispiel_ergebnis.add(toga.Label("-"))
        beispiel_ergebnis.add(toga.Label("3"))
        beispiel_box.add(beispiel_ergebnis)

        zaehler_1 = toga.TextInput(style=Pack(width=40,text_align="center"))
        nenner_1 = toga.TextInput(style=Pack(width=40,text_align="center"))
        zaehler_2 = toga.TextInput(style=Pack(width=40,text_align="center"))
        nenner_2 = toga.TextInput(style=Pack(width=40,text_align="center"))
        eingabe_box = toga.Box(style=Pack(direction=ROW), margin=(20, 20))
        eingabe_bruch_1 = toga.Box(style=Pack(direction=COLUMN))
        eingabe_bruch_1.add(zaehler_1)
        eingabe_bruch_1.add(toga.Label("----"))
        eingabe_bruch_1.add(nenner_1)
        eingabe_box.add(eingabe_bruch_1)
        eingabe_bruch_2 = toga.Box(style=Pack(direction=COLUMN))
        eingabe_bruch_2.add(zaehler_2)
        eingabe_bruch_2.add(toga.Label("----"))
        eingabe_bruch_2.add(nenner_2)
        eingabe_box.add(eingabe_bruch_2)

        main_box.add(beispiel_box)
        main_box.add(eingabe_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return BruchrechenApp()
