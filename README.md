# Cryptography lr2

## Включает шифры:
- Шифр с автоматическим выбором ключа


## Переменные среды
Для создания .env файла выполните команду:
```bash
    cp .env.example .env
```

### Общие
- SECRET_DATA (str)
- ALFABET_POWER (int) = 1_114_111

### Шифр с автоматическим выбором ключа
- AKSC_KEY (str)


## Зависимости
Для хранения зависимостей используются файлы pyproject.toml и uv.lock
Установка зависимостей и настройка виртуального окружения:
```bash
  pip install uv
  uv sync
```

## Режим запуска
```bash
    source ./venv/bin/activate
    python3 caesar_cipher.py
```