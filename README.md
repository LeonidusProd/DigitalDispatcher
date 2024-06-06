# Digital Dispatcher

## Version 1.2

Дипломный проект.

**Цель создания проекта:** Проект представляет из себя программный комплекс, предназначенный для полуавтоматической
обработки аварийных заявок.

**Целевой пользователь системы:** домоуправляющие компании.

**Програмный состав проекта:**

* Back-end приложение (Dgango REST API) - главное серверное приложение
* Web-приложение (Vue.js) - браузерный интерфейс, предназначенный для взаимодействия диспетчера и системы
* Telegram чат-бот (ResidentBot, Aiogram) - интерфейс на базе чат-бота платформы Telegram, предназначенный
  для взаимодействия жителя и системы
* Telegram чат-бот (EmlpoyeesBot, Aiogram) - интерфейс на базе чат-бота платформы Telegram, предназначенный
  для взаимодействия мастера и системы

**Роли пользователей:**

* Администратор
* Диспетчер
* Житель
* Мастер (человек, оказывающий услуги непосредственно на месте возникновения аварийной ситуации)

**Основные функциональные возможности:**

* Создание аварийной заявки любым пользователем чат-бота "ResidentBot"
* Отображение информации о заявках в браузерном интерфейсе
* Создание задач для мастеров в браузерном интерфейсе
* Просмотр и управление задачами в чат-боте "EmlpoyeesBot" пользователем, зарегистрированным в системе как мастер
* Настройка системы через браузерный интерфейс пользователем, зарегистрированным как администратор

**Используемые технологии:**

* Django (Django Rest Framework)
* PostgreSQL
* Vue.js
* Aiogram
* Docker / Docker Compose
* Nginx

## Запуск проекта

<details>
<summary>
<strong>
Локально
</strong>
</summary>

### Склонировать репозиторий:
```sh
git clone https://github.com/LeonidusProd/DigitalDispatcher.git
```

<details>
<summary>
<strong>
База данных (Подготовка БД PostgreSQL)
</strong>
</summary>

### 1. Установить PostgreSQL:
- Для Windows
  Скачать дистрибутив [PostgreSQL](https://postgrespro.ru/windows) и установить в соответствии с инструкцией
  (задать логин и пароль суперпользователя (по умолчанию - postgres), для локального использования можно отключить
  "Разрешить подключения с любых IP-адресов")

### 2. Открыть SQL Shell или запустить psql:
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

<details>
<summary>
Для удаления БД (при наличии ошибок) выполнить:
</summary>

```sh
DROP DATABASE digitaldispatcher;
```
</details>
</details>

<details>
<summary>
<strong>
Backend приложение
</strong>
</summary>

### 1. Перейти в дирректорию приложения:
```sh
cd backend
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

### 5. Создать и провести миграции БД:
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```

### 6. Загрузить фикстуры:
```sh
python manage.py loaddata digdispdata.json
```

### 7. Запустить тестовый web-сервер:
```sh
python manage.py runserver
```
По умолчанию сервер будет запущен по адресу [127.0.0.1:8000](http://127.0.0.1:8000)
</details>

<details>
<summary>
<strong>
Web-приложение
</strong>
</summary>

### 1. Перейти в дирректорию приложения:
```sh
cd front
```

### 2. Установить менеджер пакетов npm:
```sh
npm install
```

### 2. Запустить сборку проекта и тестовый сервер:
```sh
npm run serve
```
По умолчанию сервер будет запущен по адресу [127.0.0.1:8080](http://127.0.0.1:8000)
</details>

<details>
<summary>
<strong>
Чат бот (ResidentBot)
</strong>
</summary>

### 1. Перейти в дирректорию приложения:
```sh
cd residentsBot
```

### 2. Установить и активировать виртуальное окружение:
```sh
python -m venv .venv
```
```sh
.venv\Scripts\activate
```

### 3. Обновить pip и установить зависимости python:
```sh
pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```

### 4. Запустить приложение:
```sh
python run.py
```
</details>

<details>
<summary>
<strong>
Чат бот (EmlpoyeesBot)
</strong>
</summary>

### 1. Перейти в дирректорию приложения:
```sh
cd emlpoyeesBot
```

### 2. Установить и активировать виртуальное окружение:
```sh
python -m venv .venv
```
```sh
.venv\Scripts\activate
```

### 3. Обновить pip и установить зависимости python:
```sh
pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```

### 4. Запустить приложение:
```sh
python run.py
```
</details>
</details>

<details>
<summary>
<strong>
Через Docker/DockerCompose
</strong>
</summary>

### Собрать билд и поднять контейнер
```sh
docker-compose -f docker-compose.yml up -d --build
```
</details>

<details>
<summary>
<strong>
Полезные команды
</strong>
</summary>

### Создание дампа базы данных
```sh
python -Xutf8 manage.py dumpdata --indent=2 --exclude sessions --exclude contenttypes --exclude admin.logentry --exclude auth.permission -o digdispdata.json
```
</details>