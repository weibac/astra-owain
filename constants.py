import os
import dotenv

DEFAULT_MODEL = "gpt-3.5-turbo-1106"
DEFAULT_TEMPERATURE = 0.1

N_TEST_CALLS = 10

ALPHABET_P = 0.5
ALPHABET_N = 5

DIGITS_P = 0.8
DIGITS_N = 10

ALPHABET_WORDS_P = 0.0010
ALPHABET_WORDS_N = 10


# Secrets
# a .env file with the API key must be in the same directory as this file
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
