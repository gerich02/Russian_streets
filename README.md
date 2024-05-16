# Хакатон "Улицы России"
## Доступ к документации Swagger по ссылкам:
##### /swagger/ - Вернёт документацию в UI Swagger
##### /redoc/ - Вернёт документацию в UI Redoc
##### /swagger.json/ - Вернёт файл в формате JSON
##### /swagger.yaml/ - Вернёт файл в формате YAML


## Установка приложения:

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине. Проверить наличие можно выполнив команды:

```bash
docker --version && docker-compose --version
```
</details>

<br>

Клонируйте репозиторий с GitHub и введите данные для переменных окружения (в файле env_example значения даны для примера, но их можно оставить):

```bash
git clone git@github.com:pdyakovlev/Russia_streets_hackathon.git
cd Russia_streets_hackathon
cp env_example .env
nano .env
```


<br>

## Запуск приложения:

1. Из корневой директории проекта выполните команду:
```bash
docker compose up
```
  Проект будет развернут в docker-контейнерах по адресу http://localhost

  Администрирование приложения может быть осуществлено через админ панель по адресу http://localhost/admin

<h4 id="t1">Учетные данные для входа в админ-зону:</h4>
<ul>
  <li>login: adm
  <li>password: admpw
</ul><br>

## ВАЖНО!!!
Если появляются проблемы с файлом start.sh  - выполните команду в директории с файлом:

```bash
sed -i 's/\r$//' start.sh
```


2. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:

```bash
docker compose down
```

Если также необходимо удалить том базы данных:
```bash
docker compose down -v
```

