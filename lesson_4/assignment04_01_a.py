# Завдання: налаштувати flask на локальній машині
#
# 1. інсталювати flask
#
#    > python3 -m pip install flask
#    або
#    > sudo python3 -m pip install flask
#    або, для віндоувс
#    > py -3 -m pip install flask
#    для перевірки що пакет було встановлено
#    > python3 -m flask --version
#    або, для віндоувс
#    > py -3 -m flask --version
# 2. інсталювати postman (опціонально, але бажано)
# 3. запустити завдання на виконання (сервер повинен залишитись запущеним)
# 4. надіслати запит та отримати відповідь
#
#    у браузері набрати http://localhost:5000/hello
#    та побачити World! у відповідь

import random
from flask import Flask

app = Flask(__name__)

_NAMES = [
    "John", "Joseph", "William", "Cory", "Adam", "Homer"
]



@app.route("/hello", strict_slashes=False)
def hello():
    return "<h2>World!</h2>"


@app.route("/class/qautomation", strict_slashes=False)
def students():
    students = [random.choice(_NAMES) for _ in range(random.randint(10, 30))]
    ratings = {
        student: tuple(random.randint(5, 10) for i in range(10))
        for student in students
    }
    return {
        "result": {
            "students": students,
            "ratings": ratings,
        }
    }


if __name__ == "__main__":
    app.run(debug=True)