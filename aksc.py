"""
Automatic key selection cipher (AKSC) realization.
"""

from static import PLAINTEXT, AKSC_KEY as KEY, ALFABET_POWER


def encrypt(plaintext: str, key: str, n: int) -> str:
	"""
	Encrypts the given plaintext using the automatic key selection cipher (AKSC) method.


	:param plaintext: The text to be encrypted.
	:type plaintext: str
	:param key: The initial key used for encryption.
	:type key: str
	:param n: Alphabet power (number of unique characters).
	:type n: int

	:return: The resulting ciphertext after encryption.
	:rtype: str

	:raises ValueError: If plaintext or key is an empty string.
	:raises ValueError: If plaintext is less than 2 characters long.
	:raises ValueError: If key is not a single character.
	"""
	if not plaintext or not key:
		raise ValueError("Plaintext and key must be non-empty strings.")

	if len(plaintext) < 2:
		raise ValueError("Plaintext must be at least 2 characters long.")

	if len(key) != 1:
		raise ValueError("Key must be a single character.")

	ciphertext: list[str] = [""]  * len(plaintext)

	for i, x in enumerate(plaintext):
		ciphertext[i] = chr((ord(x) + ord(key)) % n)
		key = x

	return "".join(ciphertext)


def decrypt(ciphertext: str, key: str, n: int) -> str:
	"""
	Decrypts the given ciphertext using the automatic key selection cipher (AKSC) method.

	:param ciphertext: The text to be decrypted.
	:type ciphertext: str
	:param key: The initial key used for decryption.
	:type key: str
	:param n: Alphabet power (number of unique characters).
	:type n: int

	:return: The resulting plaintext after decryption.
	:rtype: str

	:raises ValueError: If ciphertext or key is an empty string.
	:raises ValueError: If ciphertext is less than 2 characters long.
	:raises ValueError: If key is not a single character.
	"""
	if not ciphertext or not key:
		raise ValueError("Ciphertext and key must be non-empty strings.")

	if len(ciphertext) < 2:
		raise ValueError("Ciphertext must be at least 2 characters long.")

	if len(key) != 1:
		raise ValueError("Key must be a single character.")


	plaintext: list[str] = [""] * len(ciphertext)

	for i, y in enumerate(ciphertext):
		plaintext[i] = chr((ord(y) - ord(key)) % n)
		key = plaintext[i]

	return "".join(plaintext)



def main() -> None:
	"""Точка запуска файла."""

	print("Открытое сообщение: ", PLAINTEXT)
	print("Зашифрованные данные: ", encoded_data := encrypt(PLAINTEXT, KEY, ALFABET_POWER))
	print("Дешифрованные данные: ", decrypt(encoded_data, KEY, ALFABET_POWER))

	return None


if __name__ == "__main__":
	main()
