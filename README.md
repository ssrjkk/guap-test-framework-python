# API & UI Test Framework

Python | pytest | Selenium | k6 | Docker

Тестовый фреймворк для автоматизации проверки веб-сайта guap.ru и его API.

## Что тестируется

| Тип | Сайт | Описание |
|-----|------|---------|
| API | guap.ru | REST API университета |
| UI | guap.ru | Главный сайт ГУАП |
| UI | lk.guap.ru | Личный кабинет студента |

---

## Структура

```
├── .env                     # Конфигурация окружения
├── .env.example             # Пример конфигурации
├── .github/workflows/ci.yml # CI/CD pipeline
├── Dockerfile               # Docker для тестов
├── conftest.py              # Глобальные фикстуры
├── config/
│   └── settings.py          # Конфигурация (из .env)
├── api_client/
│   ├── base.py              # BaseApiClient с логированием
│   └── clients.py           # Клиенты: GuapApiClient, GenericApiClient
├── tests_data/
│   └── factories.py         # Data Factory для тестовых данных
├── api_tests/
│   ├── conftest.py          # API фикстуры
│   └── test_api_clients.py  # API тесты
├── ui_tests/
│   ├── conftest.py          # UI фикстуры, скриншоты
│   ├── pages/               # Page Objects
│   │   ├── base_page.py     # Базовый класс с явными ожиданиями
│   │   ├── guap_page.py     # GUAP страницы
│   │   └── metro_page.py    # Metro SPb страницы
│   └── test_pages.py        # UI тесты
├── load_tests/              # k6 нагрузочные тесты
│   ├── api_basic.js
│   └── api_crud.js
└── sql_tasks/
    └── guap_db_queries.sql  # SQL: валидация данных, edge cases
```

---

## Стек

- **Python 3.11+** — основной язык
- **pytest 8.x** — тестовый фреймворк
- **requests** — HTTP клиент
- **Selenium 4.x** — UI автоматизация
- **python-dotenv** — конфигурация
- **allure-pytest** — отчетность
- **k6** — нагрузочное тестирование
- **Docker** — контейнеризация

---

## Запуск

### Установка

```bash
pip install -r requirements.txt
cp .env.example .env
```

### Тесты

```bash
# Все тесты
pytest -v

# API (guap.ru)
pytest api_tests/ -v

# UI (guap.ru)
pytest ui_tests/ -v

# По тегам
pytest -m smoke         # Smoke
pytest -m regression    # Regression
pytest -m critical      # Critical path
pytest -m negative      # Negative
```

### Allure

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## Конфигурация (.env)

```env
BASE_URL=https://guap.ru
ENV=local
BROWSER=chrome
TIMEOUT_EXPLICIT=10
TIMEOUT_PAGE_LOAD=30
HEADLESS=true
LOG_LEVEL=INFO
```

---

## Архитектура

### API Client Layer

Тест → API Client (method) → BaseApiClient → requests.Session

### Page Object Model

Тест → Page Object → BasePage → Selenium WebDriver

### Test Data Layer

Тест → Factory → DataBuilder → Уникальные данные

---

## Docker

```bash
docker build -t qa-tests .
docker run --rm qa-tests pytest api_tests/ -v
docker run --rm qa-tests pytest ui_tests/ -v
```

---

## CI/CD

GitHub Actions: lint → api-tests → ui-tests → report → summary

---

## Тестовые стратегии

| Тег | Назначение |
|-----|------------|
| `@pytest.mark.smoke` | Smoke тесты |
| `@pytest.mark.regression` | Regression |
| `@pytest.mark.critical` | Critical path |
| `@pytest.mark.negative` | Negative |
| `@pytest.mark.slow` | Медленные |

---

## Контакты

- Telegram: @ssrjkk
- Email: ray013lefe@gmail.com
- GitHub: https://github.com/ssrjkk
