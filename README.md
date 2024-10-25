# Мой проект
Сервис для хранения товаров.

### Как настроить проект
1. Скачайте и установите <font><u>python 3.7</u></font> и <font><u>PostgreSQL</u></font>.
2. Активируйте виртуальную среду установленного питона.
3. Параметры для подключения к БД пропишите в <font color='gray'>*/server/server/db_settings.py*</font> файле.
4. Установите зависимости с помощью команды `pip install -r requirements.txt `.

### Как запустить проект
1. `python manage.py migrate`
2. `python manage.py runserver`

### Как запустить тестирование проекта
1. `python manage.py test`

