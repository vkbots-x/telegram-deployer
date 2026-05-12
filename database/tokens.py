from database.mongo import db

tokens_collection = db.tokens


async def save_github_token(user_id: int, token: str):

    await tokens_collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "github_token": token
            }
        },
        upsert=True
    )


async def get_github_token(user_id: int):

    user = await tokens_collection.find_one(
        {"user_id": user_id}
    )

    if not user:
        return None

    return user.get("github_token")
