from static import PLAINTEXT, SSC_KEY as KEY


def encrypt(plaintext: str, key: str) -> str:
    ciphertext = []
    for i, ch in enumerate(plaintext):
        k = key[i % len(key)]
        ciphertext.append(chr(ord(ch) ^ ord(k)))
    return "".join(ciphertext)


def decrypt(ciphertext: str, key: str) -> str:
    return encrypt(ciphertext, key)


def main() -> None:
    print("Открытое сообщение:", PLAINTEXT)
    encoded = encrypt(PLAINTEXT, KEY)
    print("Зашифрованные данные (в hex):", encoded.encode().hex())
    decoded = decrypt(encoded, KEY)
    print("Дешифрованные данные:", decoded)


if __name__ == "__main__":
    main()
