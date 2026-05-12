from database.mongo import db

users_collection = db.users


async def get_user(user_id: int):
    return await users_collection.find_one(
        {"user_id": user_id}
    )


async def create_user(user_id: int):
    existing = await get_user(user_id)

    if existing:
        return existing

    data = {
        "user_id": user_id,
        "github_token": None,
        "koyeb_token": None,
        "render_token": None,
        "heroku_token": None,
        "projects": []
    }

    await users_collection.insert_one(data)

    return data


async def update_user_token(
    user_id: int,
    field: str,
    value: str
):
    await users_collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                field: value
            }
        }
    )


async def update_user_state(
    user_id: int,
    data: dict
):
    await users_collection.update_one(
        {"user_id": user_id},
        {
            "$set": data
        }
    )
