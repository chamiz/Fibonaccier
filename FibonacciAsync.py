import asyncio
import random


async def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    await asyncio.sleep(random.random())
    return await fibonacci_of(n - 1) + await fibonacci_of(n - 2)  # Recursive case


async def main():
    tasks = []
    for i in range(2):
        # User input from console
        user_input = int(input("Enter the term " + str(i + 1) + " : "))
        tasks.append(asyncio.create_task(fibonacci_of(user_input)))

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # Return the first completed task
    for task in done:
        print("First result --> " + task.result().__str__())

    # Return the results of second task
    for task in pending:
        await asyncio.wait(pending)
        print("Second result --> " + task.result().__str__())

asyncio.run(main())
