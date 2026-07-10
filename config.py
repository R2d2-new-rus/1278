"""
config.py
Конфигурация проекта KAD Scraper
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# Загружаем .env если он существует
load_dotenv()

# ----------------------------
# Пути проекта
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"
DB_DIR = BASE_DIR / "database"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
DB_DIR.mkdir(exist_ok=True)

# ----------------------------
# Настройки браузера
# ----------------------------

HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

SLOW_MO = int(os.getenv("SLOW_MO", "100"))

TIMEOUT = int(os.getenv("TIMEOUT", "30000"))

# ----------------------------
# Настройки поиска
# ----------------------------

COURT_NAME = "Арбитражный суд Челябинской области"

DATE_FROM = "01.07.2026"

DATE_TO = "31.07.2026"

MIN_SUM = 3_000_000

MAX_SUM = 25_000_000

DEFENDANT_PREFIX = "АО"

# ----------------------------
# Экспорт
# ----------------------------

EXCEL_FILE = OUTPUT_DIR / "cases.xlsx"

CSV_FILE = OUTPUT_DIR / "cases.csv"

SQLITE_FILE = DB_DIR / "cases.db"

# ----------------------------
# Логи
# ----------------------------

LOG_FILE = LOG_DIR / "kad_scraper.log"

# ----------------------------
# Повторные попытки
# ----------------------------

MAX_RETRIES = 5

RETRY_WAIT = 3

# ----------------------------
# Паузы
# ----------------------------

PAGE_DELAY = 1.5

CARD_DELAY = 1.0

# ----------------------------
# User-Agent
# ----------------------------

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/138.0 Safari/537.36"
)
