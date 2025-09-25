# Cryptography LR2 — алгоритмы и запуск

Этот репозиторий содержит четыре учебных модуля:
- **AKSC** — шифр с автоматическим выбором ключа (autokey по открытому тексту);
- **LFSR** — регистр сдвига с линейной обратной связью (генератор ключевого потока);
- **SSC** — простой потоковый шифр (XOR с повторяющимся ключом);
- **SSK** — синхронный потоковый шифр на базе LFSR (XOR-шифрование байт-строка).

> Проект учебный. Реализации **не предназначены** для защиты реальных данных.

---

## Быстрый старт

### Установка зависимостей
Зависимости управляются через `pyproject.toml` и `uv.lock`:
```bash
pip install uv
uv sync
```

### Переменные окружения
Создайте и заполните `.env`:
```bash
cp .env.example .env
```

Общие:
- `SECRET_DATA` — произвольная строка
- `ALFABET_POWER` — мощность алфавита (int), например `1_114_111`

AKSC:
- `AKSC_KEY` — начальный ключ (один символ)

SSC:
- `SSC_KEY` — строка-ключ для XOR (повторяется по кругу)

SSK / LFSR:
- `SEED` — двоичная строка начального состояния регистра
- `TAB_BITS` — номера разрядов обратной связи (целые, через пробел)

### Запуск примеров
```bash
python3 aksc.py
```
```bash
python3 ssc.py
```
```bash
python3 ssk.py
```

---

## Краткая сводка по шифрам

| Алгоритм | Синхронность | Ключевая модель | Тип шифра |
|---|---|---|---|
| **AKSC** (autokey по открытому тексту) | **Несинхронный**: ключ на шаге *i* зависит от предыдущего **открытого** символа | **Одноключевой**: один начальный ключ (1 символ), далее ключ генерируется из текста | **Потоковый**: помесимвольная обработка |
| **SSC** (XOR с повторяющимся ключом) | **Синхронный**: поток ключа повторяется циклически, не зависит от текста | **Одноключевой**: секрет — строка `SSC_KEY` | **Потоковый**: побайтное XOR |
| **SSK** (XOR с ключевым потоком LFSR) | **Синхронный**: ключевой поток не зависит от текста/шифртекста, определяется `SEED` и `TAB_BITS` | **Одноключевой**: секрет — пара (`SEED`, `TAB_BITS`) | **Потоковый**: побайтное XOR |

> Примечание: **LFSR** сам по себе не является шифром, а генератором псевдослучайной последовательности, используемой в *SSK* как ключевой поток.

---

## Описания и интерфейсы

### 1) AKSC — шифр с автоматическим выбором ключа
Файл: `aksc.py`  
Идея: на шаге *i* шифруем `y[i] = (ord(x[i]) + ord(k)) mod n`, после чего **обновляем ключ** `k = x[i]`. Для расшифрования: `x[i] = (ord(y[i]) - ord(k)) mod n`, далее `k = x[i]`.  

Интерфейс:
```python
encrypt(plaintext: str, key: str, n: int) -> str
decrypt(ciphertext: str, key: str, n: int) -> str
```

### 2) SSC — простой потоковый шифр (XOR с повторяющимся ключом)
Файл: `ssc.py`  
Идея: ключ повторяется циклически по длине текста. На шаге *i* используется символ `key[i % len(key)]`.

Интерфейс:
```python
encrypt(plaintext: str, key: str) -> str
decrypt(ciphertext: str, key: str) -> str
```

### 3) LFSR — генератор ключевого потока
Файл: `lfsr.py`  
Идея: регистр сдвига, новый бит — XOR выбранных разрядов (taps).  

Интерфейс:
```python
LFSR(seed: str, tab_bits: list[int])
lfsr() -> str           # выдает блок длиной len(seed)
lfsr_gen() -> Iterator  # бесконечный генератор бит ('0'/'1')
```

### 4) SSK — синхронный потоковый шифр на базе LFSR
Файл: `ssk.py`  
Идея: формируем байты ключевого потока, собирая по 8 бит из `LFSR.lfsr_gen()`, затем применяем XOR с текстом.

Интерфейс:
```python
encrypt(text: str, keystream_bits: Iterator[str]) -> bytes
decrypt(cipher: bytes, keystream_bits: Iterator[str]) -> str
```

---

## Примеры использования

### AKSC
```python
from aksc import encrypt, decrypt
from static import PLAINTEXT, AKSC_KEY, ALFABET_POWER

cipher = encrypt(PLAINTEXT, AKSC_KEY, ALFABET_POWER)
plain  = decrypt(cipher, AKSC_KEY, ALFABET_POWER)
```

### SSC
```python
from ssc import encrypt, decrypt
from static import PLAINTEXT, SSC_KEY

cipher = encrypt(PLAINTEXT, SSC_KEY)
plain  = decrypt(cipher, SSC_KEY)
```

### SSK
```python
from ssk import encrypt, decrypt
from lfsr import LFSR
from static import SEED, TAB_BITS

l = LFSR(SEED, TAB_BITS)
cipher_hex = encrypt("hello", l.lfsr_gen()).hex()

l = LFSR(SEED, TAB_BITS)
plain = decrypt(bytes.fromhex(cipher_hex), l.lfsr_gen())
```

---

## Замечания по безопасности
- **AKSC**, простой XOR (**SSC**) и одиночный **LFSR** уязвимы и применяются только для обучения.
- Для реальной защиты нужны современные алгоритмы: AES-GCM, ChaCha20-Poly1305 и т.п.

---

## Лицензия
MIT.
