import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-transportation-secret")
    JSON_SORT_KEYS = False
