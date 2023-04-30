import aiohttp

BASE_URL = "http://api.rankgun.works"


class RankGun:
    """A client for the RankGun API."""

    def __init__(self, api_token, workspace_id):
        self.api_key = api_token
        self.workspace_id = workspace_id
        self.session = aiohttp.ClientSession(headers={"api-token": self.api_key})

    async def _get(self, endpoint, params=None):
        """Make a GET request to the RankGun API."""
        url = f"{BASE_URL}{endpoint}"
        async with self.session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()

    async def _post(self, endpoint, params=None):
        """Make a GET request to the RankGun API."""
        url = f"{BASE_URL}{endpoint}"
        async with self.session.post(url, params=params) as response:
            response.raise_for_status()
            return await response.json()

    async def get_status(self):
        """Get the status of the RankGun API."""
        endpoint = "/status"
        return await self._get(endpoint)

    async def promote(self, username=None, User_Id=None):
        """Promote a user. +1 rank"""
        endpoint = "/ranking/promote"
        params = {"workspace_id": self.workspace_id}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return await self._post(endpoint, params=params)

    async def demote(self, username=None, User_Id=None):
        """Demote a user. -1 Rank"""
        endpoint = "/ranking/demote"
        params = {"workspace_id": self.workspace_id}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return await self._post(endpoint, params=params)

    async def setrank(self, rank, username=None, User_Id=None):
        """Set the rank of a user. * Rank"""
        endpoint = "/ranking/set-rank"
        params = {"workspace_id": self.workspace_id, "rank": rank}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return await self._post(endpoint, params=params)

    async def exile(self, username=None, User_Id=None):
        """Removes players from group."""
        endpoint = "/ranking/exile"
        params = {"workspace_id": self.workspace_id}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return await self._post(endpoint, params=params)

    async def shout(self, shout_text):
        """Shouts to group."""
        endpoint = "/utils/shout"
        params = {"workspace_id": self.workspace_id, "shout_text": shout_text}
        return await self._post(endpoint, params=params)
