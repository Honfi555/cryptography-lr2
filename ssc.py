from typing import Iterable, Iterator

from static import PLAINTEXT, SEED, TAB_BITS
from lfsr import LFSR


def _bits_to_byte(ks_bits: Iterator[str]) -> int:
	b = 0
	for _ in range(8):
		bit = next(ks_bits)
		bit = int(bit)
		b = (b << 1) | (bit & 1)
	return b


def encrypt_bytes(plaintext: Iterable[int], keystream_bits: Iterator[str]) -> bytes:
	out = bytearray()
	for pt_byte in plaintext:
		ks_byte = _bits_to_byte(keystream_bits)
		out.append(pt_byte ^ ks_byte)
	return bytes(out)


def decrypt_bytes(cyphertext: Iterable[int], keystream_bits: Iterator[str]) -> bytes:
	return encrypt_bytes(cyphertext, keystream_bits)


def encrypt(text: str, keystream_bits: Iterator[str]) -> bytes:
	return encrypt_bytes((ord(ch) for ch in text), keystream_bits)


def decrypt(cipher: bytes, keystream_bits: Iterator[str]) -> str:
	return "".join(chr(b) for b in encrypt_bytes(cipher, keystream_bits))


def main() -> None:
	"""Точка запуска файла."""

	lfsr = LFSR(seed=SEED, tab_bits=TAB_BITS)
	print("Открытое сообщение: ", PLAINTEXT)
	print("Зашифрованные данные: ", encoded_data := encrypt(PLAINTEXT, lfsr.lfsr_gen()).hex())
	lfsr = LFSR(seed=SEED, tab_bits=TAB_BITS)
	print("Дешифрованные данные: ", decrypt(bytes.fromhex(encoded_data), lfsr.lfsr_gen()))

	return None


if __name__ == "__main__":
	main()
