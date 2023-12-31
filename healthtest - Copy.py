from PyQt5.QtCore import Qt, QTimer, QRegExp
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGroupBox

app = QApplication([])
win = QWidget()

win.resize(800, 600)
win.setWindowTitle("Ruffier Cardiac Health Test")

main_layout = QVBoxLayout()

# create screen 1 interface
screen1 = QVBoxLayout()
instructions = QLabel("Test Instructions")
screen1btn = QPushButton("Begin Test")
screen1.addWidget(instructions)
screen1.addWidget(screen1btn)

# create screen 2 interface
screen2 = QVBoxLayout()
scr2_widgets = {
    "name_label": QLabel("Enter your full name:"),
    "name_input": QLineEdit(),
    "age_label": QLabel("Enter your age:"),
    "age_input": QLineEdit(),
    "instructions1": QLabel("Instructions"),
    "test_1": QPushButton("Start the test"),
    "p1_input": QLineEdit(),
    "instructions2": QLabel("Instructions"),
    "results_btn": QPushButton("Show Results")
}

int_validator = QIntValidator()

scr2_widgets["age_input"].setValidator(int_validator)
scr2_widgets["p1_input"].setValidator(int_validator)
for widget in scr2_widgets.values():
    screen2.addWidget(widget)

scr2_widgets["results_btn"].clicked.connect(lambda: on_scr2_btn())
timer = QTimer()
time_label = QLabel()
screen2.addWidget(time_label)

time_elapsed = 0

def start_timer():
    timer.start(1000)
    global time_elapsed
    time_elapsed = 0
    timer.timeout.connect(update_timer)

def update_timer():
    global time_elapsed
    time_elapsed += 1
    time_label.setText(f"Time Elapsed: {time_elapsed} seconds")

scr2_widgets["test_1"].clicked.connect(start_timer)

def on_scr1_btn():
    scr1.hide()
    scr2.show()
    scr3.hide()

def on_scr2_btn():
    # Add logic to handle screen 2 results button functionality
    pass

screen1btn.clicked.connect(on_scr1_btn)

# create screen 3 interface
screen3 = QVBoxLayout()
# Add widgets for screen 3 here if needed

scr1 = QGroupBox()
scr2 = QGroupBox()
scr3 = QGroupBox()

scr1.setLayout(screen1)
scr2.setLayout(screen2)
scr3.setLayout(screen3)

main_layout.addWidget(scr1)
main_layout.addWidget(scr2)
main_layout.addWidget(scr3)

scr1.show()
scr2.hide()
scr3.hide()

def on_scr1_btn():
    scr1.hide()
    scr2.show()
    scr3.hide()

def on_scr2_btn():
    scr1.hide()
    scr2.hide()
    scr3.show()

screen1btn.clicked.connect(on_scr1_btn)

win.setLayout(main_layout)
win.show()
app.exec_()