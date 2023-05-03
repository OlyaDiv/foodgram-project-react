# Cайт Foodgram («Продуктовый помощник»)
![example workflow](https://github.com/OlyaDiv/foodgram-project-react/actions/workflows/main.yml/badge.svg)
### Описание
На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
### Адрес
- http://158.160.106.155/
- http://158.160.106.155/admin/
- http://158.160.106.155/api/docs/
### Технологии
Python, Django, djangorestframework, nginx, gunicorn, docker-compose, workflow
### Запуск проекта
1. Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone git@github.com:OlyaDiv/foodgram-project-react.git
cd foodgram-project-react
```
2. Установите и активируйте виртуальное окружение:
```
python3 -m venv venv
. venv/Scripts/activate
```
3. Установите зависимости
```
pip install -r requirements.txt
```
### Подготовка сервера
1. Подключитесь к серверу:
```
ssh admin@84.201.161.196
# admin: имя пользователя, под которым будет выполнено подключение к серверу
# 84.201.161.196: ip-адрес сервера 
```
2. Установите docker и docker-compose
```
sudo apt install docker.io
sudo apt install docker-compose
```
3. Скопируйте файлы docker-compose.yaml и nginx/default.conf из вашего проекта на сервер в home/<ваш_username>/docker-compose.yaml и home/<ваш_username>/nginx/default.conf соответственно.
### Подготовка секретных данных
В репозитории на Github добавьте данные в Settings - Secrets - Actions secrets:
```
DOCKER_USERNAME - имя пользователя DockerHub
DOCKER_PASSWORD - пароль пользователя DockerHub
HOST - ip-адрес сервера
USER - имя пользователя для подключения к серверу
SSH_KEY - приватный ssh-ключ (публичный должен быть на сервере)
PASSPHRASE - кодовая фраза для ssh-ключа
DB_ENGINE - django.db.backends.postgresql
DB_HOST - db
DB_PORT - 5432
DB_NAME - имя БД
POSTGRES_USER - пользователь БД
POSTGRES_PASSWORD - пароль для БД
```
### Запуск workflow
При выполнении команды git push проект заливается в репозиторий и начинается проверка проекта согласно описанным операциям:
* проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8);
* сборка и доставка докер-образа на Docker Hub;
* автоматический деплой проекта на боевой сервер

На Github в репозитории во вкладке Actions можно увидеть процесс проверки проекта по workflow.
### После деплоя
1. Выполните миграции
```
sudo docker-compose exec backend python manage.py migrate
```
2. Создайте суперпользователя:
```
sudo docker-compose exec backend python manage.py createsuperuser
```
3. Соберите статику:
```
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
3. Добавьте список ингредиентов ingredients.json:
```
sudo docker-compose exec backend python manage.py load_data
```
