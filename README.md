### BookStore

BookStore - это учебный проект на Django, разработанный студентами для учебной цели. Он представляет собой веб-приложение для управления книжным магазином.

**Технологии:**

**Backend:**

- **Язык программирования:** Python
- **Фреймворк:** Django
- **Библиотеки:** Django REST Framework, drf-yasg, rest_framework_simplejwt
- **База данных:** SQLite

**Frontend:**

- **Фреймворк:** HTML, CSS, JavaScript
- **Фреймворк для интерфейса:** Bootstrap
- **Библиотеки:** JQuery

**Аутентификация и авторизация:**

- JSON Web Tokens (JWT)

**Интерфейс:**

Интерфейс приложения представлен в виде веб-страниц с использованием современных средств стилизации и визуализации, обеспечивающих удобство использования и приятный пользовательский опыт. В приложении реализованы различные страницы для управления задачами, комментариями, профилем пользователя и другими функциями.

**Основные модули и приложения:**

1. **MainSource:** Основные представления и модели для управления книгами и профилями пользователей.
2. **bookapp:** Модели и сериализаторы для работы с книгами.
3. **orderapp:** Модели и представления для управления заказами пользователей.
4. **reviewapp:** Модели и представления для управления отзывами пользователей о книгах.
5. **shoppingapp:** Модели и представления для управления корзиной покупок пользователей.
6. **userapp:** Модели и представления для управления профилями пользователей.
7. **utils:** Вспомогательные функции и утилиты.

**Запуск проекта:**

1. Убедитесь, что у вас установлен Python и Django.
2. Клонируйте репозиторий с проектом.
3. Установите зависимости, выполнив команду `pip install -r requirements.txt`.
4. Примените миграции, используя команду `python manage.py migrate`.
5. Запустите сервер разработки, выполните `python manage.py runserver`.
6. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`.

**Дополнительная информация:**

Проект BookStore был разработан в рамках учебной программы и предназначен для демонстрации навыков работы с Django, включая создание моделей, представлений, маршрутов, аутентификации и авторизации, а также для практического применения знаний веб-разработки.
