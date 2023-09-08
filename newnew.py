# from datetime import datetime

# today = datetime.now()

# date_time = today.strftime("%Y-%m-%d-%H-%M-%S")
# print(date_time)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://rai:sparta@cluster0.nzkhgpt.mongodb.net/')
db = client.dbsparta

db.diary.update_one({'content':"qwe"}, {'$set' : {"file" : "static/default-image.jpg"}})