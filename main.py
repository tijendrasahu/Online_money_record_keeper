from pymongo import MongoClient
from bson.objectid import ObjectId
from pytz import timezone
from datetime import datetime
import const

# --------------connecting to database-------------------------------
client = MongoClient(const.url)
db = client.get_database("kHATA")

try:
    collection = db.Records
    print("[Connected to Server Successfully]")
except Exception as e:
    print(e)


class customer:

    def __init__(self):
        pass

    @staticmethod
    def add_new_data(cid, name, transfer=0, balance=0):
        data = {
            "c_id": f"{cid}",
            "name": f"{name}",
            "transfer": transfer,
            "Balance": 0
        }
        collection.insert_one(data)
        collection.update_one({"name": name}, {"$inc": {"total": balance}})
        print(f"{name} Added Successfully")

    @staticmethod
    def gen_CID():
        cid = collection.find_one({"_id": ObjectId('66dac9590f2c7d90fa0adfff')})
        cid = cid["cid"] + 1
        collection.update_one({"_id": ObjectId('66dac9590f2c7d90fa0adfff')}, {'$set': {'cid': cid}})
        return int(cid)

    @staticmethod
    def bal(amt):
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M')
        amt = {ind_time: amt}
        return amt

    @staticmethod
    def total(new_amt, name):
        collection.update_one({"name": name}, {"$inc": {"total": new_amt}})
        return "BALANCE UPDATED"

    @staticmethod
    def search(name, action=0):
        results = collection.find_one({"name": f"{name}"})

        if action != 0:
            collection.update_one({"name": name}, {"$inc": {"total": action}})
            return "BALANCE UPDATED"

        for i in results["transfer"]:
            print(i)

        results = f"{results["name"]} and total Balance is :: {results["total"]}"
        return results

    @staticmethod
    def acc_del(name):
        collection.delete_one({"name": f'{name}'})
        return f"{name} removed Successfully"
