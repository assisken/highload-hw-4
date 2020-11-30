# Лабораторная работа №4 по Highload

## Зависимости

- Ruby (для команды `ruby`, `gem`)
- Python 3 (для команды `python3`)
- Pip (для команды `pip3`)

## Как установить сервис А (Python)

```bash
$ pip3 install -r requirements.txt
```

## Как установить сервис А (Ruby)

```bash
$ cd server
$ gem install bundler
$ bundle install
```

## Как запустить сервис А (Python)

```bash
$ python3 app.py
```

## Как запустить сервис Б (Ruby)

```bash
$ ruby server.rb
```

## Как использовать GraphQL

[Запускаете](#как-запустить-сервис-а-python) сервис на питоне,
переходите на: [localhost:5000/graphql](http://localhost:5000/graphql)

Далее вбиваете следующие запросы.

Всё работает, ответ выдаёт номер телефона, код и результат `SUCCESS`:

```graphql
query VerifyPhone {
  phone(number: "70000000000", code: 1) {
    number
    code
    validationResult
  }
}
```

Выдаёт номер телефона, код и результат `INCORRECT_CODE`:

```graphql
query VerifyPhone {
  phone(number: "70000000000", code: 2) {
    number
    code
    validationResult
  }
}
```

Выдаёт номер телефона, код и результат `NUMBER_NOT_FOUND`:

```graphql
query VerifyPhone {
  phone(number: "1234", code: 1) {
    number
    code
    validationResult
  }
}
```