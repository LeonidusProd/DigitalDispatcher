# Digital Dispatcher V1

Дипломный проект.  

**Цель создания проекта:**  

[//]: # (Целью создания веб-сайта является предоставление информации о )

[//]: # (деятельности и выступлениях уличных артистах и повышение их )

[//]: # (популярности среди городского населения.)

**Основные функциональные возможности и типовые страницы:**

[//]: # (* Главная страница)

[//]: # (* Регистрация, авторизация, восстановление пароля )

[//]: # (* Личный кабинет пользователя )

[//]: # (* Каталог артистов)

[//]: # (* Детальная страница артиста )

[//]: # (* Интерактивный календарь событий)

[//]: # (* Модуль администрирования)

**Роли пользователей**   

[//]: # (* Администратор)

[//]: # (* Неавторизованные пользователь)

[//]: # (* Авторизованный пользователь)

[//]: # (* Артист)

**Используемые технологии:**
* Django
* Django Rest Framework
* PostgreSQL
* Vue.js


## Начало работы 
### 1. Склонировать репозиторий:

```sh
git clone https://github.com/LeonidusProd/DigitalDispatcher_V1.git
```


### 2. Установить виртуальное окружение:

```sh
python -m venv .venv
```
`.venv` - путь к виртуальному окружению

### 3. Активировать виртуальное окружение:

- Для Windows

```sh
.venv\Scripts\activate
```

- Для Linux и MacOS

```sh
source venv/bin/activate
```

### 4. Обновить pip и установить зависимости python:

```sh
pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```

## Подготовка БД PostgreSQL
### 1. Установить PostgreSQL:
- Для Windows

    Скачать дистрибутив [PostgreSQL](https://postgrespro.ru/windows) и установить в соответствии с инструкцией
   (задать логин и пароль суперпользователя (по умолчанию - postgres), для локального использования можно отключить 
"Разрешить подключения с любых IP-адресов")
### 2. Открыть SQL Shell или запустить psql из папки /bin/ установленного PostgreSQL:

```sh
psql -U postgres
```
и ввести запрашиваемый пароль суперпользователя
### 3. Создать нового пользователя для проекта

```sh
CREATE USER digitaldispatcher WITH PASSWORD '1234';
```

### 4. Создать БД и задать владельца

```sh
CREATE DATABASE digitaldispatcher OWNER=digitaldispatcher;
```

### 5. Проверить наличие созданной БД, открыв список существующих:

```sh
\l
```

Для удаления БД (при наличии ошибок) выполнить:

```sh
DROP DATABASE digitaldispatcher;
```

## Работа с проектом: перед началом работы

### 0.1. Пересоздать БД (если уже работали над проектом):
Необходимо, так как могла измениться структура и наполнение базы данных  
В SQL Shell или psql:

```sh
DROP DATABASE digitaldispatcher;
```
```sh
CREATE DATABASE digitaldispatcher OWNER=digitaldispatcher;
```

### 0.2. Загрузить обновление рабочей ветки (dev). Создать ветку из dev для выполнения задачи.

### 1. Провести миграции БД:

```sh
python manage.py migrate
```

### 2. Загрузить фикстуры:

```sh
python manage.py loaddata digdispdata.json
```

### 3. Запустить тестовый web-сервер:

```sh
python manage.py runserver
```
По умолчанию сервер будет запущен по адресу [127.0.0.1:8000](http://127.0.0.1:8000)

## Работа с проектом: при завершении работы

### 1. Создать миграции БД (если изменялась структура бд):
Удалить все файлы (кроме ```__init__.py```) из папок "migrations" в папке каждого приложения.  

Создать миграции для каждого приложения:

```sh
python manage.py makemigrations api_v1
```

[//]: # (```sh)

[//]: # (python manage.py makemigrations Users)

[//]: # (```)

### 2. Создать дамп базы данных (если изменялось наполнение бд):

```sh
python -Xutf8 manage.py dumpdata --indent=2 --exclude sessions --exclude contenttypes --exclude admin.logentry --exclude auth.permission -o digdispdata.json
```

### 3. Создать и запушить коммит. Commit Message заполнить согласно правил:

1) Сообщения коммитов должны быть следующей структуры:

    ```
   <тип>: <описание>.
   <тип>: <описание>.
   ...
   ```
2) Возможные типы коммитов:
   * fix - исправление бага
   * add - добавление новой функции
   * update - изменение функции

### 4. Создать Pull Request из своей ветки в ветку !dev!

## Запуск проекта через Docker
### Собрать билд и поднять контейнер
```sh
docker-compose -f docker-compose.yml up -d --build
```
