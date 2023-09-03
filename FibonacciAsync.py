""""Calculates Fibonacci sequence Asynchronously"""
import asyncio
import random


async def fibonacci_of(input_int):
    """"Calculates Fibonacci sequence"""
    if input_int in {0, 1}:  # Base case
        return input_int
    await asyncio.sleep(random.random())
    return await fibonacci_of(input_int - 1) + await fibonacci_of(input_int - 2)  # Recursive case


async def main():
    """"Execute methods concurrently"""
    tasks = []
    for i in range(2):
        # User input from console
        user_input = int(input("Enter the term " + str(i + 1) + " : "))
        tasks.append(asyncio.create_task(fibonacci_of(user_input)))

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # Return the first completed task
    for task in done:
        print("First result --> " + str(task.result()))

    # Return the results of second task
    for task in pending:
        await asyncio.wait(pending)
        print("Second result --> " + str(task.result()))


asyncio.run(main())
