import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

config={
    "db": {
            "mongo_url" : os.environ.get('MONGO_URL'),
            "db_name" : os.environ.get('DATABASE_NAME'),
    }
}