from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGroupBox, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QIntValidator, QFont

app = QApplication([])
win = QWidget()

win.resize(800, 600)
win.setWindowTitle("Ruffier Cardiac Health Test")

main_layout = QVBoxLayout()

screen1 = QVBoxLayout()
instructions = QLabel("The Ruffier Cardiac Health Test is a 3-part test designed to evaluate cardiovascular health.\n"
                      "It is calculated based on measuring the pulse of the patient as they lie on their back, perform exercise, and rest.\n"
                      "Cardiovascular fitness is categorized as High, Above Average, Average, Satisfactory, or Low ")

font = QFont()
font.setPointSize(15)
instructions.setFont(font)

screen1btn = QPushButton("Begin Test")
screen1.addWidget(instructions)
screen1.addWidget(screen1btn)

screen2 = QVBoxLayout()
scr2_widgets = {
    "name_label": QLabel("Enter your full name:"),
    "name_input": QLineEdit(),
    "age_label": QLabel("Enter your age:"),
    "age_input": QLineEdit(),
    "instructions1": QLabel("Lie on your back and take your pulse for 15 seconds. Click the 'start first test' button to start the timer. Write down the result in the appropriate field."),
    "test_1": QPushButton("Start the first test"),
    "p1_input": QLineEdit(),
    "instructions2": QLabel("Perform 30 squats in 45 seconds. To do this, click on the 'Start doing squats' button"),
    "test_2": QPushButton("Start doing squats"),
    "p2_input": QLineEdit(),
    "instructions3": QLabel("Sit down for 1 minute and write your result"),
    "test_3": QPushButton("Sit down"),
    "p3_input": QLineEdit(),
    "results_btn": QPushButton("Show Results"),
}

int_validator = QIntValidator()

scr2_widgets["age_input"].setValidator(int_validator)
scr2_widgets["p1_input"].setValidator(int_validator)
scr2_widgets["p2_input"].setValidator(int_validator)
scr2_widgets["p3_input"].setValidator(int_validator)

for widget in scr2_widgets.values():
    screen2.addWidget(widget)

timer = QTimer()
time_label = QLabel()
timer2 = QTimer()
time_label2 = QLabel()
timer3 = QTimer()
time_label3 = QLabel()
screen2.addWidget(time_label)
screen2.addWidget(time_label2)
screen2.addWidget(time_label3)
time_elapsed = 0
time_elapsed2 = 0
time_elapsed3 = 0


def start_timer():
    global time_elapsed
    timer.start(1000)
    time_elapsed = 0
    timer.timeout.connect(update_timer)


def update_timer():
    global time_elapsed
    time_elapsed += 1
    time_label.setText(f"Time Elapsed: {time_elapsed} seconds")
    if time_elapsed > 15:
        time_label.setText("Enter pulse, then begin test 2.")
        timer.stop()


def start_timer2():
    global time_elapsed2
    timer2.start(1000)
    time_elapsed2 = 0
    timer2.timeout.connect(update_timer2)


def update_timer2():
    global time_elapsed2
    time_elapsed2 += 1
    time_label2.setText(f"Time Elapsed: {time_elapsed2} seconds")
    if time_elapsed2 > 45:
        time_label2.setText("Enter pulse, then begin test 3.")
        timer2.stop()


def start_timer3():
    global time_elapsed3
    timer3.start(1000)
    time_elapsed3 = 0
    timer3.timeout.connect(update_timer3)


def update_timer3():
    global time_elapsed3
    time_elapsed3 += 1
    time_label3.setText(f"Time Elapsed: {time_elapsed3} seconds")
    if time_elapsed3 > 60:
        time_label3.setText("Done!")
        timer3.stop()


scr2_widgets["test_1"].clicked.connect(start_timer)
scr2_widgets["test_2"].clicked.connect(start_timer2)
scr2_widgets["test_3"].clicked.connect(start_timer3)


class TestWin(QWidget):
    def timer_sits(self):
        time = QTime(0, 0, 30)
        self.test.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])


class TestWin(QWidget):
    def timer3Event(self):
        time = QTime()
        if 15 < int(time.toString("hh:mm:ss")[6:8]) <= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif 45 < int(time.toString("hh:mm:ss")[6:8]) <= 60:
            self.text_timer.setStyleSheet("color: rgb(255, 0, 0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")


def interpret_results(age, index):
    result_label = QLabel()
    result = "not calculated"
    ranges = (1, 2, 3, 4)
    if 7 <= age <= 8:
        ranges = [0.5, 6, 11, 15]
    elif 9 <= age <= 10:
        ranges = [2, 7.5, 12.5, 16.5]
    elif 11 <= age <= 14:
        ranges = [5, 10.5, 15.5, 19.5]
    elif age >= 15:
        ranges = [6.5, 12, 17, 21]
    else:
        result = "Age must be 7 or above"

    if index < ranges[0]:
        result = "High"
    elif ranges[0] < index <= ranges[1]:
        result = "above average"
    elif ranges[1] < index <= ranges[2]:
        result = "Average"
    elif ranges[2] < index <= ranges[3]:
        result = 'satisfactory'
    elif index > ranges[3]:
        result = 'Low'

    result_label.setText("Ruffier index: " + str(index) + '\n' + "Cardiac fitness: " + result)
    return result_label


def calculate_results():
    p1 = int(scr2_widgets["p1_input"].text())
    p2 = int(scr2_widgets["p2_input"].text())
    p3 = int(scr2_widgets["p3_input"].text())
    ruffier_index = ((p1 + p2 + p3) * 4 - 200) / 10
    print(ruffier_index)
    return ruffier_index


screen3 = QVBoxLayout()
result_display_label = QLabel()
screen3.addWidget(result_display_label)

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


screen1btn.clicked.connect(on_scr1_btn)


def on_scr2_btn():
    if all(scr2_widgets[field].text() for field in ["name_input", "age_input", "p1_input", "p2_input", "p3_input"]):
        scr3.show()
        scr1.hide()
        scr2.hide()
        index = calculate_results()
        age = int(scr2_widgets["age_input"].text())
        result_label = interpret_results(age, index)
        result_display_label.setText(result_label.text())
    else:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Please fill in all required fields before proceeding to results.")
        msg_box.setWindowTitle("Incomplete Form")
        msg_box.exec_()


scr2_widgets["results_btn"].clicked.connect(on_scr2_btn)

win.setLayout(main_layout)
win.show()
app.exec_()
