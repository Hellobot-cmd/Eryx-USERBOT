from Zaid.database import dbb

clone_db = dbb.clone


async def save_clone(user_id, data: dict):
    await clone_db.update_one(
        {"_id": user_id},
        {"$set": data},
        upsert=True
    )


async def get_clone(user_id):
    return await clone_db.find_one({"_id": user_id})


async def delete_clone(user_id):
    await clone_db.delete_one({"_id": user_id})
