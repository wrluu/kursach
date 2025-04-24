from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent / 'logs' / 'app.log'
BASE_DIR = Path(__file__).resolve().parent
EXCEL_PATH = BASE_DIR / 'data' / 'my_operations.xls'
JSON_PATH = BASE_DIR / 'user_settingss.json'
REPORTS_PATH = BASE_DIR / 'reports.json'
