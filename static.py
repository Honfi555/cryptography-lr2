"""
Static configuration variables for the cipher scripts.
"""

import os

from dotenv import load_dotenv

load_dotenv('.env')

PLAINTEXT: str = os.getenv('PLAINTEXT')

AKSC_KEY: str = os.getenv('AKSC_KEY')
ALFABET_POWER: int = int(os.getenv('ALFABET_POWER'))

INIT_STATE: str = os.getenv('INIT_STATE')
TAB_BITS: list[int] = list(map(int, os.getenv('TAB_BITS').split()))
