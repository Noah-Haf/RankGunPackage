import requests
BASE_URL = "https://api.rankgun.works"


class RankGun:
    """A client for the RankGun API."""

    def __init__(self, api_token, workspace_id):
        self.api_key = api_token
        self.workspace_id = workspace_id


    def _request(self, method, endpoint, params=None, data=None):
        url = f"{BASE_URL}{endpoint}"
        response = requests.request(method, url, params=params, data=data, headers={"api-token": self.api_key})
        response.raise_for_status()
        return response.json()



    def get_status(self):
        """Get the status of the RankGun API."""
        endpoint = "/status"
        return self._request("GET", endpoint)

    def promote(self, username=None, User_Id=None):
        """Promote a user. +1 rank"""
        endpoint = "/ranking/promote"
        params = {"workspace_id": self.workspace_id}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return self._request("POST", endpoint, params=params)

    def demote(self, username=None, User_Id=None):
        """Demote a user. -1 Rank"""
        endpoint = "/ranking/demote"
        params = {"workspace_id": self.workspace_id}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return self._request("POST", endpoint, params=params)

    def setrank(self, rank, username=None, User_Id=None):
        """Set the rank of a user. * Rank"""
        endpoint = "/ranking/set-rank"
        params = {"workspace_id": self.workspace_id, "rank": rank}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return self._request("POST", endpoint, params=params)

    def exile(self, username=None, User_Id=None):
        """Removes players from group."""
        endpoint = "/ranking/exile"
        params = {"workspace_id": self.workspace_id}

        if username is not None:
            params["username"] = username
        elif User_Id is not None:
            params["user_id"] = User_Id
        return self._request("POST", endpoint, params=params)

    def shout(self, shout_text):
        """Shouts to group."""
        endpoint = "/utils/shout"
        params = {"workspace_id": self.workspace_id, "shout_text": shout_text}
        return self._request("POST", endpoint, params=params)