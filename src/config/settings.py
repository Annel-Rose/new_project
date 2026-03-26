import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass

# print(Path(__file__))
# print(Path(__file__).resolve())
# print(Path(__file__).resolve().parents)
# print(list(Path(__file__).resolve().parents))
# print(Path(__file__).resolve().parents[2])

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"

# print(ENV_FILE)

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)


@dataclass(frozen=True)
class DatabaseSettings:
    host:str=os.getenv("DB_HOST", "localhost")
    port=int(os.getenv("DB_PORT", "3306"))
    user=os.getenv("DB_USER", "root")
    password=os.getenv("DB_PASSWORD", "")
    name=os.getenv("DB_NAME", "school_managment")

DB_SETTINGS = DatabaseSettings()
APP_NAME = os.getenv("APP_NAME", "school managment")