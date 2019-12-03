# mongodb

## Операции
```
db.createCollection("users") // добавление коллекции
db.users
    .drop() // удаление коллекции
    .insertOne({ "name": "Mike" }) // добавить запись
    .insertMany([{ "name": "Mike" }, { "name": "Alexey" }]) // добавить несколько записей
    .updateOne({ "name": "Mike" }, { $set: { surname: "Petrov" } }) // обновить запись
    .replaceOne({ "name": "Mike" }, { surname: "Petrov" }) // заменить запись
    .deleteOne({ "name": "Mike" }) // удалить запись
```
## Вывод
```
db.users.find() // вывести все записи
db.users
    .find() // вывести все записи
    .find().limit(n) // вывести n записей
    .find({}, { _id: 0 }) // вывести все записи без поля _id
    .find({ name: "Mike" }, {}) // вывести все записи с фильтром поля name = "Mike"
    .find({ "names.1": "Mike" }, {}) // вывести все записи с фильтром массива names и первый элемент = "Mike"
    .find({ "names": { $elemMatch: { $lte: "a" } }}, {}) // вывести все записи с фильтром массива names по равенству строк
    .find({ $or: [{ name: "Mike" }, { surname: "Petrov" }]}, {}) // вывести все записи с фильтром поля name = "Mike"
    .find().sort({ name: 1 })  // вывести все записи по возрастанию поля name (-1 по убыванию)
```
## Поиск
```
db.users
    .createIndex({ name: "text" }) // создать индекс
    .find({ $text: { $search: "Mike" }}) // вывести все записи по поиску
    .find({ $text: { $search: "Mike" }}, { score: { $meta: "textScore" }}) // вывести все записи по поиску + процент совпадения
```
## Счёт
```
db.users
    .count({ name: "Mike" }) // посчитать записи
    .distinct({ "name" }) // уникальные значения
    .aggregate([
        { $match: { name: "Mike" }},
        { $group: { _id: "$name", age: { $sum: "$age" } }}
    ]) // уникальные значения
```
## Дополнительно (объединение запросов)
```
db.users
    .bulkWrite([
        {
            insertOne: {
                "document": { "name": "Mike" }
            }
        },
        {
            deleteOne: {
                filter: { name: "Mike" }
            }
        },
        {
            updateOne: {
                filter: { name: "Mike" },
                update: { $set: { surname: "Petrov" } }
            }
        },
        {
            replaceOne: {
                filter: { name: "Mike" },
                replacement: { name: "Alexey" }
            }
        }
    ])
```
## Фильтр
```
$gt // greater than (<)
$lt // less than (>)
$eq // equal (===)
$ne // equal (!==)
$gte // (<=)
$lte // (>=)
$or // или
$in // соответствуют
$nin // не соответствуют
$exists // существование
$size // размер массива/объекта
```
