<h1> FastApi + GraphQL(Strawberry) </h1>

## Description

- Стек обязательный к использованию:
- VM: Doker (желательно добавить CI/CD)
- PL: Python
- Packaging/Dependency management: Poetry
- Freamework: FastApi + GraphQL(Strawberry)
- DB: Postgresql
- Замметки:
- PK - primary key
- PR - private repository

## ТЗ
- Создать простое API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.

## Создать сущности
###  "Работник", с полями:
- имя – char 255
- номер телефона – char 255 (username)
- торговая точка – ForeignKey к "Торговая точка" (обязательно к заполнению)
### "Заказчик", с полями:
- имя – char 255
- номер телефона – char 255
- торговая точка – ForeignKey к "Торговая точка" (обязательно к заполнению)
###  "Торговая точка"
- название
- сотрудники – ForeignKey к "Работник" (обязательно к заполнению)
### "Заказ"
- дата/время – создания
- дата/время – окончания – после которой, заказ не актуален 
- куда – ForeignKey к "Торговая точка"
- автор – ForeignKey к "Заказчик"
- статус – char [‘started’, ‘ended’, ‘in process’, ‘awaiting’, ‘canceled’]
- исполнитель – ForeignKey к "Работник"

### "Посещение"
- дата/время – создания
- исполнитель – ForeignKey к "Работник"
- заказ – OneToOne к "Заказ"
- автор – ForeignKey к "Заказчик"
- куда – ForeignKey к "Торговая точка

## Due to lack of time, I wasn't able to create all the CRUD methods, my apologies. If you have the opportunity to give me a little more time to work on this project,it would be nice

## Сделать методы

### Для упрощения задания, вместо полноценной авторизации передавать в каждый запрос номер телефона Работника.
- получить список Торговых точек привязанных к переданному номеру телефона
в ответе список Торговых точек (желательно с фильтрацией):
PK
Название
##
- выполнить CRUD по сущности “Заказ” (автором может быть, только “Заказчик”)
сделать валидацию: “Заказчик” может создать заказ только на свою “торговую точку”
сделать валидацию: Исполнителем должен быть Работник привязанным к “Торговой точке”
желательно добавить фильтрацию списка по GET запросу
##
- выполнить CRUD по сущности “Посещение” (автором может быть, только “Заказчик”)
сделать валидацию: Заказчик может создать “Посещение” только на свою “торговую точку” и если срок “Заказа” не истек
сделать валидацию: “Посещение” может создаваться, если ранее уже не было иной записи по PK “Заказа”
сделать валидацию: Исполнителем должен быть Работник привязанным к Заказу
желательно добавить фильтрацию списка
## 
- Cделать отдельный PUT метод запроса для изменения статуса “Заказа”

### Админка
- Работник, Заказчик, Торговая точка, Заказ, Посещение
- создание
- редактирование
- удаление
- поиск по имени Работника
- поиск по номеру Работника
- поиск по названию Торговой точки


To run the project in your local environment::

  1. Clone the repository::
```
  $ git clone https://github.com/syedfaisalsaleeem/FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate.git
  $ cd FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate
```
  2. Create and activate a virtual environment::
```
  $ virtualenv env -p python3
  $ source env/bin/activate
```
  3. Install requirements::
```
  $ pip install -r requirements.txt
```
  4. Fill the /envs/.env file to connect your DB
```
    HOST_URL=0.0.0.0
    HOST_PORT=5000
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_SERVER=
    POSTGRES_PORT=
    POSTGRES_DB=
```
  5.Run the application::
```
  $ uvicorn src.app:app --reload
```

## Migrations

To run the project in your local environment::

```
$ alembic revision --autogenerate -m "migration string"
$ alembic upgrade head
```
