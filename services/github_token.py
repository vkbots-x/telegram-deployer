import aiohttp


async def validate_github_token(token: str):

    url = "https://api.github.com/user"

    headers = {
        "Authorization": f"token {token}"
    }

    try:

        async with aiohttp.ClientSession() as session:

            async with session.get(
                url,
                headers=headers
            ) as response:

                if response.status == 200:

                    data = await response.json()

                    return True, data.get("login")

                return False, None

    except Exception as e:

        print(f"GITHUB TOKEN VALIDATION ERROR: {e}")

        return False, None
