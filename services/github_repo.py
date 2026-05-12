import aiohttp


async def get_repo_info(repo_url: str):

    try:

        repo_url = repo_url.strip().replace(
            "https://github.com/",
            ""
        )

        owner, repo = repo_url.split("/")

        repo = repo.replace(".git", "")

        return owner, repo

    except:
        return None, None


async def validate_repo_access(
    token: str,
    repo_url: str
):

    owner, repo = await get_repo_info(repo_url)

    if not owner:
        return False, "Invalid repository URL"

    url = f"https://api.github.com/repos/{owner}/{repo}"

    headers = {
        "Authorization": f"token {token}"
    }

    async with aiohttp.ClientSession() as session:

        async with session.get(
            url,
            headers=headers
        ) as response:

            if response.status == 200:

                data = await response.json()

                return True, data

            return False, None


async def get_authenticated_user(
    token: str
):

    url = "https://api.github.com/user"

    headers = {
        "Authorization": f"token {token}"
    }

    async with aiohttp.ClientSession() as session:

        async with session.get(
            url,
            headers=headers
        ) as response:

            if response.status == 200:

                data = await response.json()

                return data.get("login")

            return None


async def fork_repository(
    token: str,
    repo_url: str
):

    owner, repo = await get_repo_info(repo_url)

    if not owner:
        return False

    url = f"https://api.github.com/repos/{owner}/{repo}/forks"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    async with aiohttp.ClientSession() as session:

        async with session.post(
            url,
            headers=headers
        ) as response:

            return response.status in [202, 201]
