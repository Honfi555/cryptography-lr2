from static import INIT_STATE, TAB_BITS


class LFSR:
	"""
	Class for generating pseudo-random number in a bit representation.
	"""
	state: str = ''
	tab_bits: list[int] = []

	def __init__(self, init_state: str, tab_bits: list[int]) -> None:
		if not init_state or not tab_bits:
			raise ValueError('init_state and tab_bits must be set')
		if len(tab_bits) < 2:
			raise ValueError('tab_bits must be at least 2')
		tab_bits.sort()
		if tab_bits[-1] > len(init_state):
			raise ValueError('tab_bits can only contain integers from 0 to {}'.format(len(init_state)))

		self.state = init_state
		self.tab_bits = tab_bits

	def _step(self) -> int:
		new_bit: int = int(self.state[self.tab_bits[0]])
		out_bit: int = new_bit

		for tab_bit in self.tab_bits[1:]:
			new_bit ^= int(self.state[tab_bit])

		self.state: str = self.state[1:] + str(new_bit)
		return out_bit

	def lfsr(self) -> str:
		"""Генерация последовательности с помощью LFSR.

		:return: Сгенерированная последовательность.
		:rtype: Str
		"""
		prn: str = '' # pseudo-random number

		for _ in range(len(self.state)):
			prn += str(self._step())

		return prn


def main() -> None:
	"""Точка запуска файла."""

	print("Начальное состояние:", INIT_STATE)

	lfsr_gen = LFSR(INIT_STATE, TAB_BITS)
	fake_random_numbers: list[str] = []
	fake_random_number = lfsr_gen.lfsr()

	while fake_random_number not in fake_random_numbers:
		fake_random_numbers.append(fake_random_number)
		print("Псевдослучайное число:", fake_random_number)
		fake_random_number = lfsr_gen.lfsr()

	return None


if __name__ == "__main__":
	main()
