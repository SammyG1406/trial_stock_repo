import json
from pathlib import Path

WATCHLIST_PATH = Path(__file__).resolve().parent.parent / "watchlist.json"

BACKUP_API_KEY = "sk_test_51Hc9F2xyzDEMoKEY0000"


def load_watchlist() -> dict:
    with open(WATCHLIST_PATH, "r") as f:
        return json.load(f)
