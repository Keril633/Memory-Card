from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

def show_result():
    if button.text() == 'Ответить':
        for ans in (ans_1, ans_2, ans_3, ans_4):
            if ans.isChecked():
                button.setText('Следующий вопрос')
                answer_group.show()
                group_answers.hide()
                if ans.text() == 'Смурфы' or ans.text() == 'Python' or ans.text() == 'H2O' or ans.text() == '206' or ans.text() == 'Розовые':
                    is_correct.setText('Правильно!')
                else:
                    is_correct.setText('Неправильно!')
    else:
        set_question()
        answer_group.hide()
        group_answers.show()
        button.setText('Ответить')

questions = [
                {'question':'Какой народности не существует?', 
                'answer1':'Смурфы',
                'answer2':'Энцы',
                'answer3':'Алеуты',
                'answer4':'Чулымцы',
                'correct':'Смурфы'
                },
                {'question':'На каком языке программирования написана эта программа?', 
                'answer1':'Python',
                'answer2':'C++',
                'answer3':'HTML',
                'answer4':'Java',
                'correct':'Python'
                },
                {'question':'Химическая формула воды?',
                'answer1':'H2O',
                'answer2':'CO2',
                'answer3':'H3PO4',
                'answer4':'HCl',
                'correct':'H2O'
                },
                {'question':'Сколько костей у человека?',
                'answer1':'206',
                'answer2':'204',
                'answer3':'210',
                'answer4':'208',
                'correct':'206'
                },
                {'question':'Какого цвета получатся цветы, если скрестить красные и белые цветы?',
                'answer1':'Розовые',
                'answer2':'Белые',
                'answer3':'Красные',
                'answer4':'Желтые',
                'correct':'Розовые'
                }
]

app = QApplication([])

answer_all = 0
answer_right = 0

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,200)

question = QLabel('')

group_answers = QGroupBox('Варианты ответов:')

ans_1 = QRadioButton('')
ans_2 = QRadioButton('')
ans_3 = QRadioButton('')
ans_4 = QRadioButton('')

ans_layout1 = QVBoxLayout()

ans_layout1.addWidget(ans_1, alignment=Qt.AlignCenter)
ans_layout1.addWidget(ans_2, alignment=Qt.AlignCenter)

ans_layout2 = QVBoxLayout()

ans_layout2.addWidget(ans_3, alignment=Qt.AlignCenter)
ans_layout2.addWidget(ans_4, alignment=Qt.AlignCenter)

ans_layout = QHBoxLayout()

ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)
group_answers.setLayout(ans_layout)

answer_group = QGroupBox('Результат:')
is_correct = QLabel('Правильно!')

answer_line = QVBoxLayout()
answer_line.addWidget(is_correct, alignment=Qt.AlignCenter)
answer_group.setLayout(answer_line)
answer_group.hide()

button = QPushButton('Ответить')
button.clicked.connect(show_result)

line = QVBoxLayout()
line.addWidget(question, alignment=Qt.AlignCenter)
line.addWidget(group_answers, alignment=Qt.AlignCenter)
line.addWidget(answer_group)
line.addWidget(button, alignment=Qt.AlignCenter)

main_win.setLayout(line)
main_win.show()

def set_question():
    cur_question = randint(0, len(questions) - 1)
    text_question, a1, a2, a3, a4, q = questions[cur_question].values()
    question.setText(text_question)
    ans_1.setText(a1)
    ans_2.setText(a2)
    ans_3.setText(a3)
    ans_4.setText(a4)
    main_win.q = q

set_question()

app.exec_()