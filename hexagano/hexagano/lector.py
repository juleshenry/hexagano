from surrealdb import Surreal
import asyncio
import pprint

async def leer():
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use((ns:="dev_v1"), (db_name:="headlines"))  # namespace, database
        return(
            await db.query(
                f"""
        select * from {db_name};
        """
            )
        )

if __name__ == "__main__":
    hl_dict = asyncio.run(
        leer()
    )[0]['result']
    pprint.pprint(hl_dict)
