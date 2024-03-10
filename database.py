from pymongo import MongoClient
from config import DATABASE_URL, DATABASE_NAME


myclient = MongoClient(DATABASE_URL)
mydb = myclient[DATABASE_NAME]
col = mydb["URL Shortner"]


def new_user(id, name):
    return dict(
        _id=id,
        name=name,
        shortner="gplink",
        api=dict(
            gplink="",
            atglinks="",
            shareus="",
            gyanilinks=""
        )
    )


async def add_user(id, name):
    user = new_user(id, name)
    col.insert_one(user)


async def update_user(id, name):
    filter_query = {"_id": id}
    update_query = {"$set": {"name": name}}
    col.update_one(filter_query, update_query)
    

async def get_user(id):
    query = col.find_one({"_id": id})
    return query
    
    
async def is_user_exist(id):
    query = col.find_one({"_id":id})
    return bool(query)


async def add_api(id, type, api):
    filter_query = {"_id": id}
    update_query = {"$set": {f"api.{type}": api}}
    col.update_one(filter_query, update_query)
    
    
async def update_api(id, type, api):
    filter_query = {"_id": id}
    update_query = {"$set": {f"api.{type}": api}}
    col.update_one(filter_query, update_query)


async def update_shortner(id, shortner):
    filter_query = {"_id": id}
    update_query = {"$set": {"shortner": shortner}}
    col.update_one(filter_query, update_query)
    
async def get_api(id):
    query = col.find_one({"_id":id})
    return query.get('api')