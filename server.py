

from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()


client = MongoClient("mongodb+srv://imirzanomanbaig:passpass123@classuse.wlp94al.mongodb.net/?appName=classUse")


db = client["testdb"]
admins = db["admins"]


@app.post("/add_admin")
async def add_admin(request: Request):
    admin = await request.json()
    data = {
        "admin_id": admin.get("admin_id"),
        "name": admin.get("name"),
        "email": admin.get("email"),
        "role": admin.get("role"),
        "phone": admin.get("phone"),
        "permissions": admin.get("permissions"),
        "last_login": admin.get("last_login"),
    }
    admins.insert_one(data)
    return {"message": "Admin added successfully"}


@app.get("/admins")
def get_admins():
    data = list(admins.find({}, {"_id": 0}))
    return {"admins": data}
