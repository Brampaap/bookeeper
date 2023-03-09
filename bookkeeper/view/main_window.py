from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout

from bookkeeper.view.expense_view import ExpenseWidget
from bookkeeper.view.budget_view import BudgetWidget


class MainWindow(ExpenseWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Программа для ведения бюджета")
        self.setFixedSize(800, 1000)

        self.layout = QVBoxLayout()
        self.layout.addWidget(ExpenseWidget())
        # self.layout.addWidget(BudgetWidget)