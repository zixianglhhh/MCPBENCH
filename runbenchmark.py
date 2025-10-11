from src import *


async def main():
    await run_experiment("gpt-4o", "pro_more_tools", 5)

if __name__ == "__main__":
    asyncio.run(main())