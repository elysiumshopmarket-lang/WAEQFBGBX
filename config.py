"""Liest alle Einstellungen aus der .env-Datei."""
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
load_dotenv(BASE_DIR / ".env")


def _int(name: str, default: int = 0) -> int:
    raw = os.getenv(name, "").split("#")[0].strip()
    try:
        return int(raw)
    except ValueError:
        return default


def _id_list(name: str) -> list[int]:
    ids = []
    for part in os.getenv(name, "").split("#")[0].split(","):
        part = part.strip()
        if part.isdigit() and int(part) != 0:
            ids.append(int(part))
    return ids


TOKEN = os.getenv("DISCORD_TOKEN", "").strip()
GUILD_ID = _int("GUILD_ID")
LOG_CHANNEL_ID = _int("LOG_CHANNEL_ID")
VERSE_CHANNEL_IDS = _id_list("VERSE_CHANNEL_ID")

TZ = ZoneInfo(os.getenv("TIMEZONE", "Europe/Berlin").split("#")[0].strip())
VERSE_HOUR = _int("VERSE_HOUR", 0)
VERSE_MINUTE = _int("VERSE_MINUTE", 0)

DEFAULT_VOLUME = max(0, min(200, _int("DEFAULT_VOLUME", 100)))
IDLE_DISCONNECT_SECONDS = _int("IDLE_DISCONNECT_SECONDS", 300)


def now() -> datetime:
    return datetime.now(TZ)
