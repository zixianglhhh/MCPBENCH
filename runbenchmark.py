from src import *


async def main():
    await run_experiment("gpt-4o", "sequential")

if __name__ == "__main__":
    asyncio.run(main())