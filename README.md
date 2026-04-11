# Python-framework-GUAP.RU

Python | pytest | Selenium | k6 | Docker

Фреймворк для автоматизации тестирования: API, UI и нагрузочное тестирование.

## Что демонстрирует

| Компонент | Описание |
|----------|---------|
| API automation | REST API тесты с логированием, retry, валидацией ответов |
| UI automation | Selenium Page Object с явными ожиданиями |
| Load testing | k6 сценарии с thresholds |
| SQL validation | Запросы для проверки данных и целостности |
| CI/CD | GitHub Actions: lint → tests → report |
| Docker | Запуск тестов в контейнере |

## Стек

Python 3.11+ | pytest | requests | Selenium | k6 | Docker

## Быстрый старт

```bash
pip install -r requirements.txt
cp .env.example .env

pytest -v
```

## Структура

```
api_client/        # API клиенты с логированием
api_tests/         # API тесты
ui_tests/pages/    # Page Objects
load_tests/        # k6 сценарии
sql_tasks/         # SQL запросы
config/            # Конфигурация
```

## Запуск

```bash
# Все тесты
pytest -v

# Только API
pytest api_tests/ -v

# Только UI
pytest ui_tests/ -v

# По тегам
pytest -m smoke
pytest -m regression
pytest -m critical
```

## Docker

```bash
docker build -t qa-tests .
docker run --rm qa-tests pytest
```

## Контакты

- Telegram: @ssrjkk
- Email: ray013lefe@gmail.com
