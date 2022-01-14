from decouple import config
from pymongo import MongoClient

# Fetching DB_URI from .env
URI = config('DB_URI') or 'mongodb://127.0.0.1:27017/cowrywise_task_db'

client = MongoClient(URI)