from src import *


async def main():
    # Configuration is now loaded from configs/config.json
    # You can modify configs/config.json to change:
    # - model: The model to test
    # - tasks_type: Type of tasks (day, pro, or general_test)
    # - concurrency: Number of concurrent requests
    # - num_servers: Number of servers for agent construction
    # 
    # You can also override config values by passing parameters:
    # await run_experiment(model="your_model", concurrency=5, num_servers=20)
    await run_experiment()

if __name__ == "__main__":
    asyncio.run(main())
