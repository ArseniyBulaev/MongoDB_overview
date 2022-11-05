# Лабораторная работа 1: работа с документоориентированными хранилищами на примере MongoDB

В рамках данной лабораторной работы вам предлагается инициализировать собственный инстанс (или
кластер) MongoDB, реализовать автоматическую процедуру наполнения хранилища тестовыми данными, а
также сгенерировать несколько отчётов/агрегаций с помощью MongoDB Query Language.

## Создание инстанса/кластера MongoDB

В качестве вашего тестового инстанса MongoDB предлагается использовать (на выбор):

* Тестовый MongoDB кластер на платформе [MongoDB Atlas](https://www.mongodb.com/atlas/database)
  (кнопка `Try Free` в верхнем правом углу страницы)
* Тестовый MongoDB инстанс внутри локально запущенного Docker-контейнера на основе
  [официального Docker-образа MongoDB](https://hub.docker.com/r/amd64/mongo/)

### Создание тестового бесплатного кластера MongoDB

Здесь всё просто - необходимо следовать пошаговым инструкциям на сайте [MongoDB Atlas](https://www.mongodb.com/atlas/database)

### Создание инстанса MongoDB внутри запущенного локально Docker-контейнера

Для данного способа создания MongoDB инстанса нам потребуется [Docker Desktop](https://www.docker.com/products/docker-desktop/)
После того, как Docker установлен на локальную машину, для запуска MongoDB контейнера на базе
официального образа Docker потребуется всего одна команда:

```
docker run -d -p 27017:27017 --name mongo amd64/mongo
```

## Клиент MongoDB

В рамках данной работы для взаимодействия с MongoDB предлагаются следующие варианты клиентских
приложений:

* [mongosh](https://www.mongodb.com/docs/mongodb-shell/) - CLI утилита для взаимодействия с MongoDB
* [MongoDB Compass](https://www.mongodb.com/products/compass) - GUI утилита для взаимодействия с
  MongoDB

Примечание: если вы используете локальный инстанс MongoDB запущенный в docker-контейнере, для работы
с MongoDB через `mongosh` вам достаточно запустить эту утилиту внутри контейнера в интерактивном
режиме:

```
docker exec -it mongo mongosh
```

## Структура хранилища

Имя тестовой БД в рамках данной лабораторной работы значения не имеет, для определённости будем
называть её `test`.

Внутри хранилища `test` у нас будут определены две коллекции данных:

* `students` - список студентов
* `courses` - список дисциплин

Структура коллекции `students`:
```
{
  "_id": auto_generated_id,
  "first_name": text,
  "last_name": text,
  "age": int,
  "group": text,
  "grades": [
    {
      "course_id": int (refers to `courses._id`),
      "grade": int
    },
    ...
  ]
```

Структура коллекции `courses`:
```
{
  "_id": int,
  "name": text,
  "lecturer_first_name": text,
  "lecturer_last_name": text
}
```
## Наполнение хранилища тестовыми данными

В рамках данной активности вы не ограничены какими-либо техническими средствами: данные можно
сгенерировать как вручную в Excel/текстовом редакторе, так и с помощью автоматизированного решения
на любом имеющемся в доступе языке программирования: bash script, python, ruby, любой другой на ваш
выбор.

Требования к данным:

* Примерное количество записей в коллекции `students` - до тысячи записей (100-200 будет
  оптимально)
* Примерное количество записей в коллекции `courses` - десятки штук (от 10 до 100)
* Примерное количество записей в подколлекции `students.grades` - от пяти до десяти записей для
  каждого студента

## Отчёты

* Средний балл по каждому предмету
* Средний балл по каждому студенту
* Топ-10 наиболее успевающих студентов (по среднему баллу)
* Список всех студентов, аттестованных как минимум по семи предметам
* Список преподавателей, отсортированный в порядке убывания количества оценок, которое они поставили
  студентам

## Критерии приёма работы

Pull-Request в `main` ветку данного репозитория, содержащий:
* Скрипт генерации данных (либо готовый текстовый документ содержащий данные)
* Пять `.mql` файлов, содержащие каждый по одному запросу (для каждого из отчётов)

