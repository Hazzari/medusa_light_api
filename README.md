# API microservice "Medusa Light"

___

ТЗ в файле [terms_reference.md](terms_reference.md)

___

Запуск проекта:

- Создать и активировать виртуальную среду.
   - Использовать python>=3.10
   
- Установка зависимостей:
  - `python3 -m pip install --upgrade pip pip-tools pre-commit setuptools`
  - `pip install -r requirements.txt`


- Создать файл `./config/.env` по примеру `./config/.env.example` со своими данными


- `make run` для локальной разработке


- `make docker-run` для запуска в Docker
