from src import *


async def main():
    await run_experiment("z-ai/glm-4.5", "3_tools", 3)

if __name__ == "__main__":
    asyncio.run(main())