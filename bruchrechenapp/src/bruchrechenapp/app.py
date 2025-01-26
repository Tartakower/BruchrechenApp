"""
Eine App zum Rechnen mit Brüchen
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class BruchrechenApp(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        beispiel_box = toga.Box(style=Pack(direction=ROW, padding=(20,20)))
        beispiel_operand_1 = toga.Box(style=Pack(direction=COLUMN))
        beispiel_operand_1.add(toga.Label("1"))
        beispiel_operand_1.add(toga.Label("-"))
        beispiel_operand_1.add(toga.Label("2"))
        beispiel_box.add(beispiel_operand_1)
        beispiel_box.add(toga.Label("*", style=Pack(padding=(20,20))))
        beispiel_operand_2 = toga.Box(style=Pack(direction=COLUMN))
        beispiel_operand_2.add(toga.Label("2"))
        beispiel_operand_2.add(toga.Label("-"))
        beispiel_operand_2.add(toga.Label("3"))
        beispiel_box.add(beispiel_operand_2)
        beispiel_box.add(toga.Label("=", style=Pack(padding=(20,20))))
        beispiel_ergebnis = toga.Box(style=Pack(direction=COLUMN))
        beispiel_ergebnis.add(toga.Label("1"))
        beispiel_ergebnis.add(toga.Label("-"))
        beispiel_ergebnis.add(toga.Label("3"))
        beispiel_box.add(beispiel_ergebnis)
        main_box.add(beispiel_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return BruchrechenApp()
