from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = f'mongodb://localhost:27017/'

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['hw03-02cats']

try:
        db.cats.insert_many([

        {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"],
        },

        {
            "name": "mursik",
            "age": 5,
            "features": ["ходить на лоток ", "не дає себе гладити", "білий"],
        },

        {
            "name": "bimba",
            "age": 1,
            "features": ["ходить мімо", "кричить ", "чорний"],
        },

        {
            "name": "simba",
            "age": 2,
            "features": ["ходить куди хоче", "цaрь тварин ", "рудий"],
        },
    ])

except Exception as e:
    print(e)