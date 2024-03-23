import requests

BaseUrl = "https://api.rankgun.works"

RequestsSession = requests.Session()


def request(method, endpoint, data=None):
    response = RequestsSession.request(
        method,
        f"{BaseUrl}{endpoint}",
        json=data,
    )
    return response.json()


class RankGun:
    """A client for the RankGun API."""

    def __init__(self, api_token, workspace_id):
        self.api_key = api_token
        self.workspace_id = workspace_id
        RequestsSession.headers.update(
            {"api-token": api_token, "Content-Type": "application/json"}
        )

    async def promote(self, username=None, user_id=None):
        """
        Promotes a user. +1 Rank
        """
        data = {"workspace_id": self.workspace_id}

        if username is not None:
            data["username"] = username
        elif user_id is not None:
            data["user_id"] = user_id

        return request("POST", "/roblox/promote", data)

    async def demote(self, username=None, user_id=None):
        """
        Demotes a user. -1 Rank
        """
        data = {"workspace_id": self.workspace_id}

        if username is not None:
            data["username"] = username
        elif user_id is not None:
            data["user_id"] = user_id

        return request("POST", "/roblox/demote", data)

    async def set_rank(self, rank, username=None, user_id=None):
        """
        Sets rank of a user
        """
        data = {"workspace_id": self.workspace_id, "rank": rank}

        if username is not None:
            data["username"] = username
        elif user_id is not None:
            data["user_id"] = user_id

        return request("POST", "/roblox/set-rank", data)

    async def exile(self, username=None, user_id=None):
        """
        Exiles a user
        """
        data = {"workspace_id": self.workspace_id}

        if username is not None:
            data["username"] = username
        elif user_id is not None:
            data["user_id"] = user_id

        return request("POST", "/roblox/exile", data)

    async def shout(self, shout_text):
        """
        Updates the shout of a group
        """

        return request(
            "POST",
            "/roblox/shout",
            {"shout_text": shout_text, "workspace_id": self.workspace_id},
        )
