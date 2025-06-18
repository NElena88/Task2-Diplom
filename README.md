
## Дипломный проект. Задание 2: API-тесты для Stellar Burgers
<hr>

## Студентка: Елена Нурыева

## <h>Когорта: #21</h>
<hr>

## <h>Project: Stellar Burgers API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла          | Содержание файла                  |
|-------------------------|-----------------------------------|
| allure_results.dir      | Папка с отчетами Allure           |
| Tests dir               | Директория с тестами              |
| conftest.py             | Фикстуры                          |
| test_auth_user.py       | Тесты на авторизацию пользователя |
| test_create_user.py     | Тесты на создание пользователя    |
| test_create_order.py    | Тесты на создание заказа          |
| create_order_methods.py | http клиент к order методам       |
| create_user_methods.py  | http клиент к user методам        |
| curl.py                 | Файл с URL                        |
| data.py                 | Файл с body запросов              |
| generators.py           | Генератор данных                  |
| helpers.py              | Хэлпер для тела запросов          |
| requirements.txt        | Файл с зависимостями              |



