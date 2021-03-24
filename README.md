## Требования
- Python 3.8
## Установка
Скачиваем репозиторий

`git clone https://github.com/Vladf8/AutotradeTestTask`

Устанавливаем зависимости
```
cd AutotradeTestTask
python3 -m pip install -r requirements
```
Создаем и применяем миграции для базы данных
```
python3 manage.py makemigrations
python3 manage.py migrate

```
Запускаем приложение

`python3 manage.py runserver`
## Модель Dealer
Поле  | Описание | Тип данных |
----- | -------- | ---------- |
id  | Уникальное значение для каждого Dealer | Serial |
ogrn | Основной государственный регистрационный номер. Уникален для каждого Dealer | Big Integer |
name | Имя Dealer | varchar(300) |
city | Город в котором расположен Dealer | varchar(300) |
address | Адрес по которому находится Dealer | varchar(300) |

## Описание эндпоинтов Dealer
### [POST] /autotrade/dealer/create/
Данные, которые требуется передать в теле запроса:
- ogrn
- name
- city
- address

**Пример запроса:**

*Curl:*

`curl -d "name=aaa&city=aaa&address=len&ogrn=1111" http://127.0.0.1:8000/autotrade/dealer/create/`

*Python:*

```
from requests import post

request = post(
    url='http://127.0.0.1:8000/autotrade/dealer/create/',
    data={
        'ogrn': 22232,
        'name': 'test',
        'city': 'test',
        'address': 'test'
    }
)
```

**Пример ответа:**

В ответе приходит статус операции и если она была успешна, то id созданного Dealer

`{"success": true, "dealer_id": 5}`

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`
### [DELETE] /autotrade/dealer/delete/
Данные, которые требуется передать в виде параметров запроса:
- id

**Пример запроса:**

*Curl:*

`curl -X "DELETE" http://127.0.0.1:8000/autotrade/dealer/delete/?id=4`

*Python:*

```
from requests import delete


request = delete(
    url='http://127.0.0.1:8000/autotrade/dealer/delete/',
    params={
        'id': 5
    }
)
```

**Пример ответа:**

Если операция выполнена успешно, то приходит статус выполненой операции.

`{"success": true}`

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`
### [POST] /autotrade/dealer/update/
В виде параметра запроса требуется передать id Dealer, которое требуется обновить.

А в теле запроса передаются все параметры, которые требуется обновить.

**Пример запроса:**

*Curl:*

`curl -d "name=bbb&city=bbb&address=bbb" http://127.0.0.1:8000/autotrade/dealer/update/?id=6`

*Python:*
```
from requests import post


request = post(
    url='http://127.0.0.1:8000/autotrade/dealer/update/',
    data={
        'name': 'ccc',
        'city': 'ccc',
        'address': 'ccc'
    },
    params={
        'id': 6
    }
)
```

**Пример ответа:**

В ответе приходит статус выполенной оперции и данные обновленного Dealer.
```
{"success": true, 
 "new_dealer": {
        "id": 6, 
        "ogrn": 7777, 
        "name": "bbb", 
        "city": "bbb", 
        "address": "bbb"
        }
 }
```

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`
### [GET] /autotrade/dealer/get/
В виде параметра в запросе передается id Dealer, информацию о котором требуется получить.

**Пример запроса:**

*Curl:*

`curl http://127.0.0.1:8000/autotrade/dealer/get/?id=6`

*Python:*

```
from requests import get


request = get(
    url='http://127.0.0.1:8000/autotrade/dealer/get/',
    params={
        'id': 6
    }
)
```

**Пример ответа:**

В случае успешного запроса, в ответе приходит статус выполненной операции и данные о запрашиваемом Dealer.
```
{"success": true, 
 "dealer": {
     "id": 6, 
     "ogrn": 7777, 
     "name": "ccc", 
     "city": "ccc", 
     "address": "ccc"
     }
 }
```

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`
## Модель Auto
Поле  | Описание | Тип данных |
----- | -------- | ---------- |
id | Уникальное значение для кажного Auto | Serial |
car_brand | Автомобильная марка | varchar(300) |
model_name | Название модели | varchar(300) |
vin | Идентификационный номер транспортного средства. Уникален для каждого | varchar(17) |
top_speed | Максимальная скорость | Integer |
weight | Масса | Integer |
mileage | Пробег | Integer |
horsepower | Количество лошадиных сил | Integer |
dealer | Ссылка на Dealer, которому принадлежит авто | Dealer id |

## Описание эндпоинтов Auto
### [POST] /autotrade/auto/create/
Данные, которые требуется передать в теле запроса:
- car_brand
- model_name
- vin
- top_speed
- weight
- mileage
- horsepower
- dealer

**Пример запроса:**

*Curl:*

`curl -d "car_brand=test&model_name=test&vin=test&top_speed=150&weight=1500&mileage=0&horsepower=150&dealer=6" http://127.0.0.1:8000/autotrade/auto/create/`

*Python:*

```
from requests import post


request = post(
    url='http://127.0.0.1:8000/autotrade/auto/create/',
    data={
        'car_brand': 'test',
        'model_name': 'test',
        'vin': 'test1',
        'top_speed': '160',
        'weight': '2000',
        'mileage': '100',
        'horsepower': '200',
        'dealer': 6
    }
)
```

**Пример ответа:**

В ответе приходит статус выполненой операции и id cозданного Auto.

`{"success": true, "auto_id": 4}`

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`
### [DELETE] /autotrade/auto/delete/
Требуется передать id Auto в виде параметра запроса.

**Пример запроса:**

*Curl:*

`curl -X "DELETE" http://127.0.0.1:8000/autotrade/auto/delete/?id=3`

*Python:*
```
from requests import delete


request = delete(
    url='http://127.0.0.1:8000/autotrade/auto/delete/',
    params={
        'id': 4
    }
)
```

**Пример ответа:**

В ответе передатся статус выполненой операции.

`{"success": true}`

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`
### [POST] /autotrade/auto/update/

В виде параметра запроса требуется передать id Dealer, которое требуется обновить.

А в теле запроса передаются все параметры, которые требуется обновить.

**Пример запроса:**

*Curl:*

`curl -d "car_brand=test&model_name=test&vin=test&top_speed=150&weight=1500&mileage=0&horsepower=150&dealer=6" http://127.0.0.1:8000/autotrade/auto/update/?id=5`

*Python:*

```
from requests import post


request = post(
    url='http://127.0.0.1:8000/autotrade/auto/update/',
    data={
        'car_brand': 'test1',
        'model_name': 'test1',
        'vin': 'new_vin',
        'top_speed': 300,
        'weight': 2000,
        'mileage': 200,
        'horsepower': 200,
        'dealer': 6
    },
    params={
        'id': 5
    }
)
```

**Пример ответа:**

В ответе приходит статус выполенной оперции и данные обновленного Auto.

```
{"success": true, 
 "new_auto": {
    "id": 5, 
    "car_brand": "test1", 
    "model_name": "test1", 
    "vin": "new_vin", 
    "top_speed": "300", 
    "weight": "2000", 
    "mileage": "200", 
    "horsepower": "200", 
    "dealer_id": 6
    }
 }
```

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`
### [GET] /autotrade/auto/get/

В виде параметра в запросе передается id Auto, информацию о котором требуется получить.

**Пример запроса:**

*Curl:*

`curl http://127.0.0.1:8000/autotrade/auto/get/?id=5`

*Python:*

```
from requests import get


request = get(
    url='http://127.0.0.1:8000/autotrade/auto/get/',
    params={
        'id': 5
    }
)
```

**Пример ответа:**

В случае успешного запроса, в ответе приходит статус выполненной операции и данные о запрашиваемом Auto.

```
{"success": true, 
 "auto": {
 "id": 5, 
 "car_brand": "test", 
 "model_name": "test", 
 "vin": "test", 
 "top_speed": 150, 
 "weight": 1500, 
 "mileage": 0, 
 "horsepower": 150, 
 "dealer_id": 6
    }
}
```

В случае ошибки в ответе приходит, что оперция не  выполнена и описание ошибки

`{"success": false, "error": "error description"}`