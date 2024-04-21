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

def find_cat_by_name(name):
    return db.cats.find_one({"name": name})


def create(name, age, features):
    return db.cats.insert_one({
        'name': name,
        'age': age,
        'features': features
    })


def update(cat_id, name, age, features):
    return db.cats.update_one({'_id': ObjectId(cat_id)}, {'$set': {'name': name, 'age': age, 'features': features}})

def update_cat_age_by_name(name, new_age):
    return db.cats.update_one({"name": name}, {"$set": {"age": new_age}})


def add_feature_to_cat(name, new_feature):
    return db.cats.update_one({"name": name}, {"$push": {"features": new_feature}})

def delete(cat_id):
    return db.cats.delete_one({'_id': ObjectId(cat_id)})

def delete_cat_by_name(name):
    return db.cats.delete_one({"name": name})

def delete_all_cats():
    return db.cats.delete_many({})





if __name__ == '__main__':
    match action:
        case 'create':
            cat_result = create(name, age, features)
            print(cat_result.inserted_id)
        case 'read':
            [print(cat) for cat in read()]
        case 'read_by_name':
            cat = find_cat_by_name(name)
            if cat:
                print(cat)
            else:
                print("No cat found with the name:", name)
        case 'update':
            cat_result = update(cat_id, name, age, features)
            print(cat_result.modified_count)
        case 'update_age':
            cat_result = update_cat_age_by_name(name, int(age))
            print(cat_result.modified_count)
        case 'add_feature':
            cat_result = add_feature_to_cat(name, features[0])
            print(cat_result.modified_count)
        case 'delete':
            cat_result = delete(cat_id)
            print(cat_result.deleted_count)
        case 'delete_by_name':
            cat_result = delete_cat_by_name(name)
            print(cat_result.deleted_count)
        case 'delete_all':
            cat_result = delete_all_cats()
            print(cat_result.deleted_count)
        case _:
            print('Invalid action')





























