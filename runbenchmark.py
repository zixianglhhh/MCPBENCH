from src import *


async def main():
    # You can also customize the concurrency level and the number of servers for each agent by
    # specifying the corresponding parameters in the run_experiment function. 
    # For example, you can specify the concurrency level as 5 and the number of servers as 20 by calling the run_experiment function as follows:
    # await run_experiment("your_model_name", "general_test", concurrency=5, num_servers=20)
    await run_experiment("qwen/qwen3-32b", "general_test")

if __name__ == "__main__":
    asyncio.run(main())
