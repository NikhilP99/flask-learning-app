import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "very_secret_key"

    MONGODB_SETTINGS = { 'db' : "Enrollment"}