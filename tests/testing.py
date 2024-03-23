import sys
import os
import asyncio


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rankgun import RankGun

Api_Token = sys.argv[1]


async def main():
    workspace = RankGun(Api_Token, 1)

    attempt1 = await workspace.promote(username="RankGunTests")
    attemp2 = await workspace.demote(username="RankGunTests")

    if attempt1["status_code"] != 200 or attemp2["status_code"] != 200:
        raise Exception("Something went wrong")
    else:
        print("All went well")


async def run_main():
    await main()


asyncio.run(run_main())
