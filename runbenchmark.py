from src import *


async def main():
    for model in ['openai/gpt-5-chat']:
        await run_experiment(model, "single", 1)

if __name__ == "__main__":
    
    asyncio.run(main())