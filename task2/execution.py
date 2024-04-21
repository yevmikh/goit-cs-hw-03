import argparse

from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f'mongodb://localhost:27017/'

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['hw03-02cats']

parser = argparse.ArgumentParser(description='Add a new cat')

parser.add_argument('--action', help='[create, read, update, delete]')
parser.add_argument('--id', help='ID of cat')
parser.add_argument('--name', help='name of cat')
parser.add_argument('--age', help='age of cat')
parser.add_argument('--features', help='features of cat', nargs='+')

args = vars(parser.parse_args())

action = args['action']
cat_id = args['id']
name = args['name']
age = args['age']
features = args['features']


def read():
    cats = db.cats.find()
    return cats


def create(name, age, features):
    return db.cats.insert_one({
        'name': name,
        'age': age,
        'features': features
    })
def update(cat_id, name, age, features):
    return db.cats.update_one({'_id': ObjectId(cat_id)}, {'$set': {'name': name, 'age': age, 'features': features}})
def delete(cat_id):
    return db.cats.delete_one({'_id': ObjectId(cat_id)})



if __name__ == '__main__':
    match action:
        case 'create':
            cat_result = create(name, age, features)
            print(cat_result.inserted_id)
        case 'read':
            [print(cat) for cat in read()]
        case 'update':
            cat_result = update(cat_id, name, age, features)
            print(cat_result.modified_count)
        case 'delete':
            cat_result = delete(cat_id)
            print(cat_result.deleted_count)
        case _:
            print('Invalid action')


