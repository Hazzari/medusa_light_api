# Тестовое | Backend

Перед вами тестовое задание для кандидатов на вакансию backend–разработчика в
команду приложения [Практика](http://praktika.app). Надеемся, у вас всё
получится. Желаем успеха!

# **Продуктовые требования**

---

Необходимо разработать простой backend для новостного сервиса под кодовым
названием Medusa Light. Сервис должен содержать 2 модуля:

### Модуль 1: w**eb–интерфейс администратора**

Этот модуль должен дать администратору возможность добавлять новости для
публикации. Каждая новость должна иметь 3 настраиваемых реквизита:

- дата публикации (в формате ДД.ММ.ГГГГ)
- заголовок публикации (не более 256 символов)
- текстовый контент (без ограничений по символам)

Авторизация не важна (можно делать, а можно не делать). Поддержка Markup не
требуется. Возможность редактировать новости не требуется.

### Модуль 2: REST API интерфейс

Этот модуль даёт сервису доступ к списку новостей через REST API. Нужно
реализовать HTTP–метод GET `http://[HOST]:[PORT]/news`, который возвращает
JSON–объект:

```json
[
  {
    "date": "2021-12-09", "subject": "Заголовок новости 1", "content": "Содержание новости 1"
  },
  {
    "date": "2021-12-08", "subject": "Заголовок новости 2", "content": "Содержание новости 2"
  },
  ...
]
```

Список новостей должен быть отсортирован по дате (сначала новые, потом старые).
Авторизация к REST API не требуется.

# Технические требования к реализации

---

- Сервис должен быть развёрнут на виртуальной машине с OS `Linux` на любом
  хостинге. Желательно использовать `Debian` или `Ubuntu`.
- Сервис должен хранить данные в `PostgreSQL`. Настраивать бэкап не нужно.
- Код бэкэнда должен быть написан на `Python 3` с использованием `Django`.
- Для развёртывания сервиса необходимо создать образ `Docker`, который содержит
  PostgreSQL и сам сервис.
- Необязательное требование: ****`Swagger`–документация к REST API.

# Артефакты для проверки задания

---

Пришлите результаты на [hi@praktika.app](mailto:hi@praktika.app) с темой
«Тестовое задание | Backend». К письму прикрепите резюме или ссылку на свой
профиль. Не забудьте добавить:

- URL на интерфейс администрирования, который открывается через браузер.
- URL на метод REST API — проверять будем путём запуска утилиты curl.
- Доступ по ssh к виртуальной машине, на которой развёрнут Docker–образ.
- Исходный код сервиса или URL на git–репозиторий.

На эту же почту можно присылать вопросы. Очень ждём!
