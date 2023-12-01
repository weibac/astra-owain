import os
import dotenv

# Plaintext
DEFAULT_MODEL = "gpt-4"
DEFAULT_TEMPERATURE = 0.1

# Secrets
# .env file is in the same directory as this file
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
