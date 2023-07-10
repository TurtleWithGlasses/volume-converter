from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys


class WeightCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weight Calculator")
        grid = QGridLayout()

        self.kg_label = QLabel("KG: ")
        self.kg_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Weight")
        calculate_button.clicked.connect(self.calculate_weight)
        self.output_label = QLabel("")

        grid.addWidget(self.kg_label, 0, 0)
        grid.addWidget(self.kg_line_edit, 0, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)


    def calculate_weight(self):
        kg_weight = float(self.kg_line_edit.text())
        converted_weight = kg_weight * 2.20462
        self.output_label.setText(f"Your weight is {converted_weight:.2f} pounds")


app = QApplication(sys.argv)
weight_calculator = WeightCalculator()
weight_calculator.show()
sys.exit(app.exec())