# Cryptography lr2

## Включает:
- Шифр с автоматическим выбором ключа
- Генератор псевдослучайных чисел

## Переменные среды
Для создания .env файла выполните команду:
```bash
    cp .env.example .env
```

### Общие
- SECRET_DATA (str)
- ALFABET_POWER (int) = 1_114_111

### Шифр с автоматическим выбором ключа (Automatic key selection cipher)
- AKSC_KEY (str)

### Регистр сдвига с линейной обратной связью(РСЛОС)/Генератор псевдослучайных чисел|Linear Feedback Shift Registers (LFSR)
- INIT_STATE (str) - binary representation
- TAB_BITS (str) - numbers separated by spaces


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
    python3 aksc.py
```
```bash
    source ./venv/bin/activate
    python3 lfsr.py
```
