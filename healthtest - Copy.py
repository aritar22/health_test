# from PyQt5.QtCore import Qt, QTimer, QRegExp
# from PyQt5.QtGui import QIntValidator
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGroupBox

# app = QApplication([])
# win = QWidget()

# win.resize(800, 600)
# win.setWindowTitle("Ruffier Cardiac Health Test")

# main_layout = QVBoxLayout()

# # create screen 1 interface
# screen1 = QVBoxLayout()
# instructions = QLabel("Test Instructions")
# screen1btn = QPushButton("Begin Test")
# screen1.addWidget(instructions)
# screen1.addWidget(screen1btn)

# # create screen 2 interface
# screen2 = QVBoxLayout()
# scr2_widgets = {
#     "name_label": QLabel("Enter your full name:"),
#     "name_input": QLineEdit(),
#     "age_label": QLabel("Enter your age:"),
#     "age_input": QLineEdit(),
#     "instructions1": QLabel("Lie on you back and take your pulse for 15 seconds. Click the 'start first test' button to start the timer. Write down the result in the appropriate feild."),
#     "test_1": QPushButton("Start the first test"),
#     "instructions2": QLabel("perfomr 30 squats in 45 secionds. To do this , click on the 'Start doing squats' button"),
#     "test_2": QPushButton("Start doing squats"),
#     "instructions3": QLabel("Instructions"),
#     "test_3": QPushButton(""),
#     "results_btn": QPushButton("Show Results")
# }

# int_validator = QIntValidator()

# scr2_widgets["age_input"].setValidator(int_validator)
# scr2_widgets["p1_input"].setValidator(int_validator)
# scr2_widgets["p2_input"].setValidator(int_validator)
# for widget in scr2_widgets.values():
#     screen2.addWidget(widget)

# scr2_widgets["results_btn"].clicked.connect(lambda: on_scr2_btn())
# timer = QTimer()
# time_label = QLabel()
# timer2 = QTimer()
# time_label2 = QLabel()
# timer3 = QTimer()
# time_label3 = QLabel()
# screen2.addWidget(time_label)
# screen2.addWidget(time_label2)
# screen2.addWidget(time_label3)
# time_elapsed = 0
# time_elapsed2 = 0
# time_elapsed3 = 0
# def start_timer():
#     timer.start(1000)
#     global time_elapsed
#     time_elapsed = 0
#     timer.timeout.connect(update_timer)

# def update_timer():
#     global time_elapsed
#     time_elapsed += 1
#     time_label.setText(f"Time Elapsed: {time_elapsed} seconds")
#     if time_elapsed > 5:
#         time_label.setText("Enter pulse, then begin test 2.")
#         timer.stop()
# def start_timer2():
#     timer2.start(1000)
#     global time_elapsed2
#     time_elapsed2 = 0
#     timer2.timeout.connect(update_timer2)

# def update_timer2():
#     global time_elapsed2
#     time_elapsed2 += 1
#     time_label2.setText(f"Time Elapsed: {time_elapsed2} seconds")
#     if time_elapsed2 > 5:
#         time_label2.setText("Enter pulse, then begin test 3.")
#         timer2.stop()
# def start_timer3():
#     timer3.start(1000)
#     global time_elapsed3
#     time_elapsed3 = 0
#     timer3.timeout.connect(update_timer3)

# def update_timer3():
#     global time_elapsed3
#     time_elapsed3 += 1
#     time_label3.setText(f"Time Elapsed: {time_elapsed3} seconds")
#     if time_elapsed3 > 5:
#         time_label3.setText("Done!")
#         timer3.stop()
# scr2_widgets["test_1"].clicked.connect(start_timer)
# scr2_widgets["test_2"].clicked.connect(start_timer2)
# scr2_widgets["test_3"].clicked.connect(start_timer3)

# class TestWin(QWidget):
#     def timer_sits(self):
#         time = QTime(0,0,30)
#         self.tesdt.timeout.connect(self.timer2Event)
#         self.timer.start(1500)
#     def timer2Event(self):
#         self.text_timer.setText(time.toString("hh:mm:ss")[6:8])

# class TestWin(QWidget):
#     def timer3Event(self):
#         if int(time.toString("hh:mm:ss")[6:8]) <= 15:
#             self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
#         elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
#             self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
#         else:
#             self.text_timer.setStyleSheet()
# def on_scr1_btn():
#     scr1.hide()
#     scr2.show()
#     scr3.hide()

# def on_scr2_btn():
#     # Add logic to handle screen 2 results button functionality
#     pass

# screen1btn.clicked.connect(on_scr1_btn)

# # create screen 3 interface
# screen3 = QVBoxLayout()
# # Add widgets for screen 3 here if needed

# scr1 = QGroupBox()
# scr2 = QGroupBox()
# scr3 = QGroupBox()

# scr1.setLayout(screen1)
# # scr2.setLayout(screen2)
# scr3.setLayout(screen3)

# main_layout.addWidget(scr1)
# main_layout.addWidget(scr2)
# main_layout.addWidget(scr3)

# scr1.show()
# scr2.hide()
# scr3.hide()

# def on_scr1_btn():
#     scr1.hide()
#     scr2.show()
#     scr3.hide()

# def on_scr2_btn():
#     scr1.hide()
#     scr2.hide()
#     scr3.show()

# screen1btn.clicked.connect(on_scr1_btn)

# win.setLayout(main_layout)
# win.show()
# app.exec_()