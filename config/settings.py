import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 10000))
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")