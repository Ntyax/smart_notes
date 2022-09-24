from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QTextEdit, QMessageBox)

import json

app = QApplication([])


notes = {
    "Назва замітки1" : "Текст замітки",
    "Назва замітки2" : "Текст замітки",
    "Назва замітки3" : "Текст замітки",

}


win = QWidget()
win.resize(700, 500)
win.setWindowTitle("Smart Notes")
win.setStyleSheet("background-color: #9bfa96; color: #8a4fd1")

#віджети вікна
text_field = QTextEdit()
notes_list = QListWidget()
note_title = QLineEdit()

note_title.setPlaceholderText("Введіть назву замітки")
text_field.setPlaceholderText("Введіть текст замітки")

text_field.setStyleSheet("background-color: #ffffff")
note_title.setStyleSheet("background-color: #ffffff")

new_note_btn = QPushButton("Нова замітка")
delete_btn = QPushButton("Видалити замітку")
save_btn = QPushButton("Зберегти")

list_lb = QLabel("Список заміток")

#напрямні лінії
main_line = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

row1 = QHBoxLayout()

row1.addWidget(new_note_btn)
row1.addWidget(delete_btn)

col1.addLayout(row1)
col1.addWidget(save_btn)
col1.addWidget(list_lb)
col1.addWidget(notes_list)

col2.addWidget(note_title)
col2.addWidget(text_field)

main_line.addLayout(col1, stretch=1)
main_line.addLayout(col2, stretch=2)

win.setLayout(main_line)

def show_note():
    key = notes_list.selectedItems()[0].text()
    print(notes[key])
    text_field.setText(notes[key])
    note_title.setText(key)

def save_note():
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False)

def create_note():
    title = note_title.text()
    text = text_field.toPlainText()
    if title != "" and text != "":
        notes[title] = text
        notes_list.clear()
        notes_list.addItems(notes)
        save_note()
    else:
        err = QMessageBox()
        err.setText("Додайте назву та текст замітки!")
        err.show()
        err.exec_()


def new_note():
    note_title.setText("")
    text_field.setText("")



def del_note():
    if note_title.text() in notes:
        del notes[note_title.text()]
    notes_list.clear()
    notes_list.addItems(notes)
    save_note()


with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)


notes_list.addItems(notes)
notes_list.itemClicked.connect(show_note)

save_btn.clicked.connect(create_note)
delete_btn.clicked.connect(del_note)
new_note_btn.clicked.connect(new_note)




win.show()
app.exec_()