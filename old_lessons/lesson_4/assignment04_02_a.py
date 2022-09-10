# Завдання: інсталювати requests на локальній машині
#
# 1. інсталювати requests
#
#    > python3 -m pip install requests
#    або
#    > sudo python3 -m pip install requests
#    або, для віндоувс
#    > py -3 -m pip install requests
#    для перевірки що пакет було встановлено
#    > python3 -m requests --version
#    або, для віндоувс
#    > py -3 -m requests --version
# 2. запустити розробницький сервер flask (з попереднього завадання)
# 3. виконати поточний скрипт (python assignment04_02_a.py)
#    та побачити World! у відповідь

import requests


def main():
    response = requests.get("http://127.0.0.1:5000/hello")
    print(response.text)
    print(response.url)


if __name__ == "__main__":
    main()
