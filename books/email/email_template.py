new_book = {
    'subject': """Регистрация новой книги""",
    'message': """Сообщение от сервиса Books. Создание новой записи""",
    'html_message': """<h2>Здравствуйте</h2><p>Произошла регистрация новой книги</p>""",
}

deleted_book = {
    'subject': """Книга {TITLE} была удалена""",
    'message': """Сообщение от сервиса Books. Удаление записи""",
    'html_message': """<h2>Здравствуйте</h2><p>Произошло удаление книги {TITLE}</p>"""
}

saved_book = {
    'subject': """Книга {TITLE} была сохранена""",
    'message': """Сообщение от сервиса Books. Сохранение записи""",
    'html_message': """<h2>Здравствуйте</h2><p>Произошло сохранение книги {TITLE}</p>"""
}

testing_message = {
    'subject': """Книга {TITLE}. Это сообщение для тестирования""",
    'message': """Сообщение от сервиса Books. Тестирование сохранения""",
    'html_message': """<h2>Здравствуйте</h2><p>Производится тестирование сохранение книги {TITLE}</p>"""
}

from_email = 'my_email@my.me'
testing_email = 'testing_email@testing_email.email'
recipient_list = ['recipient@recipient.email']
