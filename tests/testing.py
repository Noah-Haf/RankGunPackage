import rankgun
import sys
import asyncio

Api_Token = sys.argv[1]


async def main():
    print("let's go")
    Workspace = rankgun.RankGun(Api_Token, 1)

    Attempt1 = await Workspace.promote(username="RankGunTests")
    Attempt2 = await Workspace.demote(username="RankGunTests")

    print(Attempt1)
    if Attempt1["status_code"] != 200 or Attempt2["status_code"] != 200: 
        raise Exception("Something went wrong")
    else:
        print("All went well")

async def run_main():
    await main()

asyncio.run(run_main())
