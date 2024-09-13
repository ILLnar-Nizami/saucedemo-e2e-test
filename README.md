# Saucedemo.com E2E UI Test

Этот проект содержит E2E UI тест для saucedemo.com использующий Selenium and Python.

## Предварительные требования

- Python 3.8+
- Chrome browser
- ChromeDriver (убедитесь, что он есть в вашем PATH)

## Установка

1. Склонировать этот репозиториц:
   ```
   git clone https://github.com/ILLnar-Nizami/saucedemo-e2e-test.git
   cd saucedemo-e2e-test
   ```

2. Создать virtual environment и активировать его:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Установить необходимые пакеты:
   ```
   pip install -r requirements.txt
   ```

## Запустить тест
```
pytest tests/test_saucedemo.py
```

## Важно

- Убедитесть, что установлена последняя версия ChromeDriver и находится в system PATH.
- Этот тест использует стандартный тестовый аккаунт saucedemo.com. Если учетные данные другие, обновите их в тестовом файле test_saucedemo.py.
