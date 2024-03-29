## Задание

Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.<br />
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.<br />
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.<br />
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.<br />
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.<br />
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.<br />
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.<br />

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.



## Реализация

```  models.py  ``` - содержит определения моделей Pydantic <br />
```  database.py  ``` -  настройки подключения к базе данных и определения таблиц <br />
```  app.py  ``` - приложение Flask и маршруты для CRUD операций 
