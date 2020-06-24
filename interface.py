"""The program creating the main GUI acting as the interface."""
from PySide2 import QtWidgets as QW
from PySide2 import QtCore as QC
from PySide2 import QtGui as QG
from logic import Logic


class Calculator(QW.QWidget):  # The Calculator class is a custom QT Widget
    """The calculator widget, containing the actual calculator GUI."""

    def __init__(self, parent=None):
        """Initialise the Calculator."""
        QW.QWidget.__init__(self, parent)

        # The display and adjusting properties
        # Using QLabel, wanted to use QLCDNumber, but can't display everything
        self.display = QW.QLabel('0')  # Initially setting the display to 0
        self.display.setAlignment(QC.Qt.AlignRight)  # Aligns right, standard
        self.display_font = QG.QFont("Arial", 40)
        self.display.setFont(self.display_font)

        # Initialising the logic class
        self.logic = Logic(self.display)  # Passing the display, to be updated

        # Creating all the buttons in the calculator
        self.button_0 = QW.QPushButton('0')
        self.button_1 = QW.QPushButton('1')
        self.button_2 = QW.QPushButton('2')
        self.button_3 = QW.QPushButton('3')
        self.button_4 = QW.QPushButton('4')
        self.button_5 = QW.QPushButton('5')
        self.button_7 = QW.QPushButton('7')
        self.button_6 = QW.QPushButton('6')
        self.button_8 = QW.QPushButton('8')
        self.button_9 = QW.QPushButton('9')
        self.button_negative = QW.QPushButton('+/-')
        self.button_decimal_point = QW.QPushButton('.')
        self.button_equal = QW.QPushButton('=')
        self.button_plus = QW.QPushButton('+')
        self.button_minus = QW.QPushButton('-')
        self.button_multiply = QW.QPushButton('×')
        self.button_divide = QW.QPushButton('÷')
        self.button_clear_entry = QW.QPushButton('CE')
        self.button_global_clear = QW.QPushButton('C')
        self.button_delete = QW.QPushButton('⌫')

        # Creating a group for the buttons, and connecting them to the handler
        self.group_buttons = QW.QButtonGroup()
        self.group_buttons.buttonClicked.connect(self.logic.button_press)

        # A list of all the buttons, simplifying iterating through them
        # Put into sublist based on rows, to make it clearer where buttons are
        button_list = [
            [self.button_clear_entry, self.button_global_clear,
             self.button_delete, self.button_divide],
            [self.button_7, self.button_8, self.button_9,
             self.button_multiply],
            [self.button_4, self.button_5, self.button_6, self.button_minus],
            [self.button_1, self.button_2, self.button_3, self.button_plus],
            [self.button_negative, self.button_0,
             self.button_decimal_point, self.button_equal]
        ]

        # Using the Grid Layout, as the calculator buttons are nicely in a grid
        grid = QW.QGridLayout()
        grid.addWidget(self.display, 1, 1, 1, -1)  # Adds the display
        self.setLayout(grid)

        # Iterates through all the buttons
        for row, sublist in enumerate(button_list, 2):
            for column, button in enumerate(sublist, 1):
                # Addding the button to the button group
                self.group_buttons.addButton(button)
                # Adjusting properties of the buttons
                button.setFixedHeight(50)
                # Puts buttons on the grid, based on positions in button_list
                grid.addWidget(button, row, column)
