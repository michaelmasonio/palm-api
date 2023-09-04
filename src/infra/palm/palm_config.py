import os
from dotenv import load_dotenv


def load_config():
    # Load the environment variables from .env file
    load_dotenv()

    # Access the configuration values using os.getenv
    api_key = os.getenv("PALM_API_KEY")

    config = {
        "api_key": api_key,
    }

    return config
