

## Генератор фейковых анкет

Создание фейковых анкет с использованием библиотеки Faker.

## Установка

Установка и обновление происходит через 
[pip](https://pip.pypa.io/en/stable/quickstart/):

`pip install Faker`

## Простой пример генерации анкеты:


Например, пусть в файле `template.txt` лежит следующий шаблон:


`{name} живёт в {town}. Профессия - {job}.`

Передадим информацию из библиотеки Faker в шаблон:

```python
import file_operations
from faker import Faker
from random import *


context = {
  "name": fake.first_name(),
  "town": fake.city(),
  "job": fake.job()
}


file_operations.render_template("template.txt", "result.txt", context)
```

Создастся новый файл `result.txt`, в котором будет запись подобного
вида:

`Сергей живёт в Улан-Удэ. Профессия - нейрохирург.`

## Результат

Полная реализация кода даст 10 анкет со случайными значениями. 

Пример анкеты:

![profile](profiles/result.png)